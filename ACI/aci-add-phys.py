#!/usr/bin/env python
"""

//Rob van der Kind - robvand@cisco.com
"""
import acitoolkit.acitoolkit as aci
import csv
import getpass
import sys


def main():
    """
    Main create routine
    :return: None
    """

# Login to the APIC
#session = aci.Session(raw_input("APIC URL: "), raw_input("APIC username: "), getpass.getpass())
session = aci.Session("http://apic-amslab.cisco.com", "admin", "C1sco123")
resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')

if resp.ok:
    print ("\nApic login successful")


#Fabric acccess policy configuration

    # Add VLAN Pool to be used for newly attached hosts
    vlanpool_name = raw_input("\nEnter the VLAN Pool name to be used for the new hosts: ")
    vlanpool = {"fvnsVlanInstP":{"attributes":{
        "dn":"uni/infra/vlanns-[{}]-static".format(vlanpool_name),
        "name":vlanpool_name,
        "allocMode":"static",
        "rn":"vlanns-[{}]-static".format(vlanpool_name),
        "status":"created"},"children":[]}}

    # Add VLANs to VLAN Pool
    vlans_low = 'vlan-' + raw_input("\nEnter the low range for encap block: ")
    vlans_high = 'vlan-' + raw_input("Enter the high range for encap block: ")
    vlans = {"fvnsEncapBlk":{"attributes":{
        "dn":"uni/infra/vlanns-[{}]-static/from-[{}]-to-[{}]".format(vlanpool_name,vlans_low,vlans_high),
        "from":vlans_low,"to":vlans_high,
        "allocMode":"static",
        "rn":"from-[{}]-to-[{}]".format(vlans_low,vlans_high),
        "status":"created"},"children":[]}}

    # Create PhysDom and attach previously created vlan pool
    physdom_name = raw_input("Enter the name for the PhysDom to be created: ")
    physdom = {"physDomP":{"attributes":{
        "dn":"uni/phys-{}".format(physdom_name),
        "name":physdom_name,
        "rn":"phys-{}".format(physdom_name),
        "status":"created"},"children":[{
            "infraRsVlanNs":{"attributes":{
                "tDn":"uni/infra/vlanns-[{}]-static".format(vlanpool_name),
                "status":"created"},"children":[]}}]}}
    # Create AEP and attach previously created PhysDom
    aep_name = raw_input("Enter the name for the AEP to be created: ")
    aep = {"infraInfra":{"attributes":{
        "dn":"uni/infra",
        "status":"modified"},
        "children":[{"infraAttEntityP":{"attributes":{"dn":"uni/infra/attentp-{}".format(aep_name),
            "name":aep_name,
            "rn":"attentp-{}".format(aep_name),
            "status":"created"},
            "children":[{
                "infraRsDomP":{"attributes":{
                    "tDn":"uni/phys-{}".format(physdom_name),
                    "status":"created"},
                    "children":[]}}]}},
                    {"infraFuncP":{
                        "attributes":{
                            "dn":"uni/infra/funcprof",
                            "status":"modified"},
                            "children":[]}}]}}
    # Create Interface Leaf Policy Group (Access Port Group)
    intpolgroup_name = raw_input("Enter the name for the new Interface Policy Group: ")
    intpolgroup = {"infraAccPortGrp":{"attributes":{
        "dn":"uni/infra/funcprof/accportgrp-{}".format(intpolgroup_name),
        "name":intpolgroup_name,
        "rn":"accportgrp-{}".format(intpolgroup_name),
        "status":"created"},
        "children":[{
            "infraRsAttEntP":{"attributes":{
                "tDn":"uni/infra/attentp-{}".format(aep_name),
                "status":"created,modified"},
                "children":[]}}]}}
    # Create Interface Leaf Profile (Access port Profile)
    intprof_name = raw_input("Enter the name for the new Interface Profile: ")
    intprof = {"infraAccPortP":{"attributes":{
        "dn":"uni/infra/accportprof-{}".format(intprof_name),
        "name":intprof_name,
        "rn":"accportprof-{}".format(intprof_name),
        "status":"created,modified"},"children":[]}}
    # Create interface selector and add to interface profile


# Push the changes to the APIC
    # Push Fabric policy to APIC
    # Push VLAN pool
    vlanpool_url = '/api/node/mo/uni/infra/vlanns-[{}]-static.json'.format(vlanpool_name)
    resp = session.push_to_apic(vlanpool_url, vlanpool)
    print ''
    if not resp.ok:
        print('%% Error: Could not push VLAN pool to APIC')
        print(resp.text)
    if resp.ok:
        print ("Succesfully added VLAN Pool {} to ACI fabric").format(vlanpool_name)
    # Add VLANs to VLAN pool
    vlans_url = '/api/node/mo/uni/infra/vlanns-[{}]-static/from-[{}]-to-[{}].json'.format(vlanpool_name,vlans_low,vlans_high)
    resp = session.push_to_apic(vlanpool_url, vlans)
    if not resp.ok:
        print('%% Error: Could not push VLAN encap block to APIC')
        print(resp.text)
    if resp.ok:
        print ("Succesfully added VLAN encap block {} to {} to VLAN Pool {}").format(vlans_low,vlans_high,vlanpool_name)
    # Push PhysDom
    physdom_url = '/api/node/mo/uni/phys-{}.json'.format(physdom_name)
    resp = session.push_to_apic(physdom_url, physdom)
    if not resp.ok:
        print('%% Error: Could not push PhysDom to APIC')
        print(resp.text)
    if resp.ok:
        print ("Succesfully added PhysDom {} to APIC").format(physdom_name)
    # Push AEP
    aep_url = '/api/node/mo/uni/infra.json'
    resp = session.push_to_apic(aep_url, aep)
    if not resp.ok:
        print('%% Error: Could not push AEP to APIC')
        print(resp.text)
    if resp.ok:
        print ("Succesfully added AEP {} to APIC").format(aep_name)
    # Push Interface Leaf Policy Group
    intpolgroup_url = '/api/node/mo/uni/infra/funcprof/accportgrp-{}.json'.format(intpolgroup_name)
    resp = session.push_to_apic(intpolgroup_url, intpolgroup)
    if not resp.ok:
        print('%% Error: Could not push Interface Policy Group to APIC')
        print(resp.text)
    if resp.ok:
        print ("Succesfully added the Interface Policy Group {} to APIC").format(intpolgroup_name)
    # Push Interface Profile
    intprof_url = '/api/node/mo/uni/infra/accportprof-{}.json'.format(intprof_name)
    resp = session.push_to_apic(intprof_url, intprof)
    if not resp.ok:
        print('%% Error: Could not push Interface Policy Group to APIC')
        print(resp.text)
    if resp.ok:
        print ("Succesfully added the Interface Profile {} to APIC").format(intprof_name)
    # Push Interface selector and port

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass