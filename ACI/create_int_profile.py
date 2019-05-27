import requests
import os
import ssl
import credentials
import time

#export PATH=/usr/local/bin/:$PATH
ssl.OPENSSL_VERSION

# block warning HTTPS InsecureRequestWarning
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

bold = "\033[1m"
normal = "\033[0m"

red = "\033[1m" + "\033[91m"
yellow = "\033[1m" + "\033[93m"
purple = "\033[1m" + "\033[95m"
green = "\033[1m" + "\033[92m"

dict = {'200': green + 'OK' + normal, 
        '400': red + 'Bad Request' + normal, 
        '405':red + 'Method not allowed' + normal};


def login():
    global cookies
    auth_url = credentials.URL + '/api/mo/aaaLogin.xml'
    auth_xml = '<aaaUser name=' + credentials.USER + ' pwd =' + credentials.PASS +'/>'
    session = requests.post(auth_url, data=auth_xml, verify=False)
    cookies = session.cookies
    #print cookies
    return

def create_interface_policy_group_int(name, aep, linklevelpol, cdppol, lldppol):
    interface_policy_group = name + '_INT_POLGRP'
    auth_url = credentials.URL +  '/api/mo/uni.xml'
    xmldata = ( '<polUni>'
                    '<infraInfra>'
                        '<infraFuncP>'
                            '<infraAccPortGrp descr="" dn="uni/infra/funcprof/accportgrp-' + interface_policy_group + '" name="' + interface_policy_group + '" ownerKey="" ownerTag="">'
                                '<infraRsL2IfPol tnL2IfPolName=""/>'
                                '<infraRsQosPfcIfPol tnQosPfcIfPolName=""/>'
                                '<infraRsHIfPol tnFabricHIfPolName="' + linklevelpol + '"/>'
                                '<infraRsL2PortSecurityPol tnL2PortSecurityPolName=""/>'
                                '<infraRsMonIfInfraPol tnMonInfraPolName=""/>'
                                '<infraRsStpIfPol tnStpIfPolName=""/>'
                                '<infraRsQosSdIfPol tnQosSdIfPolName=""/>'
                                '<infraRsAttEntP tDn="uni/infra/attentp-' + aep + '"/>'
                                '<infraRsMcpIfPol tnMcpIfPolName=""/>'
                                '<infraRsQosDppIfPol tnQosDppPolName=""/>'
                                '<infraRsQosIngressDppIfPol tnQosDppPolName=""/>'
                                '<infraRsStormctrlIfPol tnStormctrlIfPolName=""/>'
                                '<infraRsQosEgressDppIfPol tnQosDppPolName=""/>'
                                '<infraRsFcIfPol tnFcIfPolName=""/>'
                                '<infraRsLldpIfPol tnLldpIfPolName="' + lldppol + '"/>'
                                '<infraRsCdpIfPol tnCdpIfPolName="' + cdppol + '"/>'
                            '</infraAccPortGrp>'
                        '</infraFuncP>'
                    '</infraInfra>'
                '</polUni>'
              )
    post = requests.post(auth_url, cookies=cookies, data=xmldata, verify=False)
    print
    print 'Interface Policy Group                  :', bold + interface_policy_group + normal
    print 'Attached Entity Profile                 :', aep
    print 'Link Level Policy                       :', linklevelpol
    print 'CDP Policy                              :', cdppol
    print 'LLDP Policy                             :', lldppol
    print "Status                                  :", dict[str(post.status_code)]
    return

def create_interface_switch_profile(name, node1, node2, from_port, to_port):

    interface_policy_group = name + '_INT_POLGRP'
    interface_profile = name + '_' + node1 + '_INTERFACE_PROFILE'
    interface_selector = name + '_' + node1 + '_INTSEL_' + from_port
    switch_profile = 'SWITCH' + node1 + '_PROFILE'
    switch_profile_selector = 'SWITCH' + node1 + '_' + node2 + '_PROFILE_SELECTOR'

    auth_url = credentials.URL +  '/api/mo/uni.xml'
    xmldata = ( '<polUni>'
                   '<infraInfra>'
                      '<infraAccPortP name="' + interface_profile + '">'
                         '<infraHPortS name="' + interface_selector + '" type="range">'
                            '<infraPortBlk name="line1" fromCard="1" toCard="1" fromPort="' + from_port + '" toPort="' + to_port + '">'
                            '</infraPortBlk>'
                            '<infraRsAccBaseGrp tDn="uni/infra/funcprof/accportgrp-' + interface_policy_group + '" />'
                         '</infraHPortS>'
                      '</infraAccPortP>'
                      '<infraNodeP name="' + switch_profile + '">'
                         '<infraLeafS name="' + switch_profile_selector + '" type="range">'
                            '<infraNodeBlk name="line1" from_="' + node1 + '" to_="' + node1 + '"/>'
                            '<infraNodeBlk name="line2" from_="' + node2 + '" to_="' + node2 + '"/>'
                         '</infraLeafS>'
                         '<infraRsAccPortP tDn="uni/infra/accportprof-' + interface_profile + '" />'
                      '</infraNodeP>'
                   '</infraInfra>'
                '</polUni>'
              )
    post = requests.post(auth_url, cookies=cookies, data=xmldata, verify=False)
    print
    print 'Interface Policy Group                  :', bold + interface_policy_group + normal
    print 'Interface Profile                       :', interface_profile
    print 'Interface Selector                      :', interface_selector
    print 'Switch Profile                          :', switch_profile
    print 'Switch Profile Selector                 :', switch_profile_selector
    print 'Node 1                                  :', node1
    print 'Node 2                                  :', node2
    print 'From Port                               :', from_port
    print 'To Port                                 :', to_port
    print "Status                                  :", dict[str(post.status_code)]
    return



#########################################################################################
print bold + "CREATE_INT" + normal

login()

print
print "---------------------------------------------------------"
print "create Interface Policy Group for INTERFACE"
print "---------------------------------------------------------"
create_interface_policy_group_int('NLSRK03AR011101_VC3_X3', 'AEP_BAREMETAL', '10G_AUTO_ON', 'CDP_DISABLED', 'LLDP_ENABLED')

# Interface Policy Group
# Attached Entity Profile
# Link Level Policy
# CDP Policy
# LLDP Policy



print
print "---------------------------------------------------------"
print "create Switch Profile"
print "---------------------------------------------------------"
create_interface_switch_profile('NLSRK03AR011101_VC3_X3', '113', '113', '11', '11')

# Interface Policy Group
# Interface Profile
# Interface Selector
# Switch Profile
# Switch Profile Selector
# Node 1
# Node 2
# From Port
# To Port

print 
