#!/usr/bin/env python
"""
It logs in to the APIC and will create the BDs and EPGs
"""
import acitoolkit.acitoolkit as aci
import csv
import getpass
import sys

def main():
    """
    Main create tenant routine
    :return: None
    """

    # Login to the APIC
session = aci.Session(raw_input("APIC URL: "), raw_input("APIC User Name: "), getpass.getpass())
resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

     # Selecting Tenant
tenants = aci.Tenant.get(session)
print("List of available Tenants:")
for temp_tenant in tenants:
    print(temp_tenant)
tenant_name = raw_input("\nPlease enter the Tenant name: ")
tenant = aci.Tenant(tenant_name)

    # Selecting Application Profile
application_profiles = aci.AppProfile.get(session, tenant)
for temp_app_profile in application_profiles:
    print(temp_app_profile)
app = aci.AppProfile(raw_input("List of Application Profiles: "), tenant)
contexts = aci.Context.get(session, tenant)

    # Selecting VRF or Context for BDs to be created
print("\nList of contexts available under the current Tenant: ")
for temp_context in contexts:
    print(temp_context)
context_name = raw_input("\nPlease enter a context for the new BDs: ")

    # Select VPC path, defaults to node 101 & 102, edit if required
vpcs = aci.PortChannel.get(session)
for vpc in vpcs:
    print (vpc)
vpc_name = raw_input("\nInput the VPC name please: ")
VPC_DN = "topology/pod-1/protpaths-101-102/pathep-[{}]".format(vpc_name)

    # Importing CSV file containing VLAN,VLAN Name
filename = raw_input("Please enter the path to your .CSV: ")
f = open(filename, 'rt')

input_vlan_bd_pairs = []
extended_vlan_count = 0

try:
    reader = csv.reader(f)
    for row in reader:
        input_vlan_bd_pairs.append(row)
finally:
    f.close()

for vlan_bd_pair in input_vlan_bd_pairs:
    vlan_id = vlan_bd_pair[0]
    bd_name = vlan_bd_pair[1]

    # Creating new Bridge domain, change values if required
    new_bridge_domain = aci.BridgeDomain(bd_name, tenant)
    new_bridge_domain.set_arp_flood("yes")
    new_bridge_domain.set_unicast_route("no")
    new_bridge_domain.set_unknown_mac_unicast("flood")
    new_bridge_domain.set_unknown_multicast("flood")
    new_bridge_domain.add_context(aci.Context(context_name, tenant))
    #new_bridge_domain.set  MULTIDEST FLOODING

    # Associate EPG with BD
    epg = aci.EPG(bd_name, app)
    epg.add_bd(new_bridge_domain)

    # Associate path with EPG
    static_binding = {"fvRsPathAtt":{"attributes":{"encap":"vlan-{}".format(vlan_id),
                                                   "tDn": VPC_DN, "instrImedcy":"immediate",
                                                   "status":"created"}}}

    # Push the changes to the APIC
    resp = session.push_to_apic(tenant.get_url(),
                                tenant.get_json())
    epgurl = '/api/node/mo/uni/tn-{}/ap-{}/epg-{}.json'.format(tenant.name, app.name, epg.name)

    if not resp.ok:
        print('%% Error: Could not push configuration to APIC')
        print(resp.text)

    static_binding_server_response = session.push_to_apic(epgurl, static_binding)

    if resp.ok:
        extended_vlan_count = extended_vlan_count + 1
        print("{}/{} Succesfully extended VLAN {} to ACI fabric").format(extended_vlan_count, len(input_vlan_bd_pairs),bd_name)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
