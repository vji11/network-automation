import requests
import os
import ssl
import credentials

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
        '403': red + 'Login failed' + normal,
        '405': red + 'Method not allowed' + normal};


def login():
    global cookies
    auth_url = credentials.URL + '/api/mo/aaaLogin.xml'
    auth_xml = '<aaaUser name=' + credentials.USER + ' pwd =' + credentials.PASS +'/>'
    session = requests.post(auth_url, data=auth_xml, verify=False)
    cookies = session.cookies
    #print cookies
    return


def create_static_binding_int(fvTenant, fvAP, fvAEPg, vlan, primary_encap, mode, nodeid, interface, status):
    auth_url = credentials.URL +  '/api/mo/uni.xml'
    xmldata = ( '<polUni>'
                    '<fvTenant name="' + fvTenant + '">'
                        '<fvAp descr="" name="' + fvAP + '" ownerKey="" ownerTag="" prio="unspecified">'
                            '<fvAEPg descr="" isAttrBasedEPg="no" matchT="AtleastOne" name="' + fvAEPg + '" prio="unspecified">'
                                '<fvRsPathAtt descr="" encap="vlan-' + vlan + '" instrImedcy="lazy" mode="' + mode + '" primaryEncap="vlan-' + primary_encap + '" tDn="topology/pod-1/paths-' + nodeid + '/pathep-[eth1/' + interface + ']" status="' + status + '"/>'
		                    '</fvAEPg>'
	                    '</fvAp>'
                    '</fvTenant>'
	            '</polUni>'
              )
              
    post = requests.post(auth_url, cookies=cookies, data=xmldata, verify=False)
    print
    print "Create Static Binding Interface:"
    print "--------------------------------------------------------------"
    print "Tenant                                  :", fvTenant
    print "Create Application Profile              :", fvAP
    print "Create Application EPG                  :", fvAEPg
    print "Vlan                                    :", vlan
    print "Primary Encap                           :", primary_encap
    print "Node-id                                 :", nodeid
    print "Interface                               :", interface
    print "created, modified, deleted              :", status
    print "Status                                  :", bold + dict[str(post.status_code)] + normal
    return


	#<fvRsPathAtt descr="" dn="uni/tn-common/ap-ORCHESTRATION/epg-VLAN1001_HOSTS/rspathAtt-[topology/pod-1/protpaths-101-102/pathep-[int_polgrp_vpc_ESXi_3]]" encap="vlan-100" instrImedcy="lazy" mode="regular" primaryEncap="unknown" tDn="topology/pod-1/protpaths-101-102/pathep-[int_polgrp_vpc_ESXi_3]"/>
    #<fvRsPathAtt descr="" dn="uni/tn-TN_LG_MGMT/ap-APP_OSS_MGMT_SERV_01/epg-EPG_OSS_MGMT_SERV_INB_01/rspathAtt-[topology/pod-1/protpaths-143-144/pathep-[NLCSAPJUMP001_INT_POLGRP]]" encap="vlan-1002" instrImedcy="lazy" mode="regular" primaryEncap="unknown" tDn="topology/pod-1/protpaths-143-144/pathep-[NLCSAPJUMP001_INT_POLGRP]"/>

def create_static_binding_vpc(fvTenant, fvAP, fvAEPg, vlan, primary_encap, mode, nodeid_1, nodeid_2, interface, status):
    auth_url = credentials.URL +  '/api/mo/uni.xml'
    xmldata = ( '<polUni>'
                '<fvTenant name="' + fvTenant + '">'
                '<fvAp descr="" name="' + fvAP + '" ownerKey="" ownerTag="" prio="unspecified">'
                     '<fvAEPg descr="" isAttrBasedEPg="no" matchT="AtleastOne" name="' + fvAEPg + '" prio="unspecified">'
                         '<fvRsPathAtt descr="" encap="vlan-' + vlan + '" instrImedcy="lazy" mode="' + mode + '" primaryEncap="vlan-' + primary_encap + '"  tDn="topology/pod-1/protpaths-' + nodeid_1 + '-' + nodeid_2 + '/pathep-[' + interface + ']" status="' + status + '"/>'
		            '</fvAEPg>'
	            '</fvAp>'
                '</fvTenant>'
	            '</polUni>'
              )
              
    post = requests.post(auth_url, cookies=cookies, data=xmldata, verify=False)
    print
    print "Create Static Binding vPC:"
    print "--------------------------------------------------------------"
    print "Tenant                                  :", fvTenant
    print "Create Application Profile              :", fvAP
    print "Create Application EPG                  :", fvAEPg
    print "Vlan                                    :", vlan
    print "Primary Encap                           :", primary_encap
    print "Node-id 1                               :", nodeid_1
    print "Node-id 2                               :", nodeid_2
    print "Interface                               :", interface
    print "created, modified, deleted              :", status
    print "Status                                  :", bold + dict[str(post.status_code)] + normal
    return


#########################################################################################
print bold + "CREATE STATIC BINDING.PY" + normal

login()

#create_static_binding_int('TN_LG_MGMT', 'APP_OSS_MGMT_SERV_01',  'EPG_OSS_MGMT_SERVER_INB_07', '1xxx', '1xxy', 'untagged' , '211', '5', 'created')

create_static_binding_vpc('TN_LG_MGMT', 'APP_OSS_MGMT_SERV_01', 'EPG_OSS_MGMT_SERVER_INB_04', '1053', '1054', 'untagged', '113', '114', 'NLSRK03AR011101_VC3_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_MGMT', 'APP_OSS_MGMT_SERV_01', 'EPG_OSS_MGMT_SERVER_INB_04', '1053', '1054', 'untagged', '113', '114', 'NLSRK03AR011101_VC4_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_PROD', 'APP_FND_BACKUP_01', 'EPG_FND_BACKUP_01', '3283', '3284', 'untagged', '113', '114', 'NLSRK03AR011101_VC3_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_PROD', 'APP_FND_BACKUP_01', 'EPG_FND_BACKUP_01', '3283', '3284', 'untagged', '113', '114', 'NLSRK03AR011101_VC4_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_PROD', 'APP_FND_NAS_01', 'EPG_FND_CIFS_01', '3266', '3314', 'untagged', '113', '114', 'NLSRK03AR011101_VC3_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_PROD', 'APP_FND_NAS_01', 'EPG_FND_CIFS_01', '3266', '3314', 'untagged', '113', '114', 'NLSRK03AR011101_VC4_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_NONPROD', 'APP_FND_NAS_01', 'EPG_FND_CIFS_01', '3275', '3315', 'untagged', '113', '114', 'NLSRK03AR011101_VC3_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_NONPROD', 'APP_FND_NAS_01', 'EPG_FND_CIFS_01', '3275', '3315', 'untagged', '113', '114', 'NLSRK03AR011101_VC4_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_PROD', 'APP_BSS_QLIKVIEW_01', 'EPG_BSS_QLIKVIEW_PUBLISHER_01', '1169', '1168', 'untagged', '113', '114', 'NLSRK03AR011101_VC3_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_PROD', 'APP_BSS_QLIKVIEW_01', 'EPG_BSS_QLIKVIEW_PUBLISHER_01', '1169', '1168', 'untagged', '113', '114', 'NLSRK03AR011101_VC4_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_PROD', 'APP_BSS_QLIKVIEW_01', 'EPG_BSS_QLIKVIEW_SERVER_01', '1171', '1170', 'untagged', '113', '114', 'NLSRK03AR011101_VC3_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_PROD', 'APP_BSS_QLIKVIEW_01', 'EPG_BSS_QLIKVIEW_SERVER_01', '1171', '1170', 'untagged', '113', '114', 'NLSRK03AR011101_VC4_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_NONPROD', 'APP_BSS_QLIKVIEW_01', 'EPG_BSS_QLIKVIEW_PUBLISHER_01', '1173', '1172', 'untagged', '113', '114', 'NLSRK03AR011101_VC3_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_NONPROD', 'APP_BSS_QLIKVIEW_01', 'EPG_BSS_QLIKVIEW_PUBLISHER_01', '1173', '1172', 'untagged', '113', '114', 'NLSRK03AR011101_VC4_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_NONPROD', 'APP_BSS_QLIKVIEW_01', 'EPG_BSS_QLIKVIEW_SERVER_01', '1175', '1174', 'untagged', '113', '114', 'NLSRK03AR011101_VC3_INT_POLGRP', 'deleted')
create_static_binding_vpc('TN_LG_NONPROD', 'APP_BSS_QLIKVIEW_01', 'EPG_BSS_QLIKVIEW_SERVER_01', '1175', '1174', 'untagged', '113', '114', 'NLSRK03AR011101_VC4_INT_POLGRP', 'deleted')

# fvTenant                  = Tenant
# fvAP                      = Application Profile
# fvAEPg                    = Application EPG
# vlan
# mode                      = regular (= trunk), native (= Access 802.1p), untagged (= Access untagged)
# node-id
# interface
# status                    = created, modified, deleted



# fvTenant                  = Tenant
# fvAP                      = Application Profile
# fvAEPg                    = Application EPG
# vlan
# primary_vlan              = unkown or vlan number
# mode                      = regular (= trunk), native (= Access 802.1p), untagged (= Access untagged)
# nodeid_1
# nodeid_2
# interface
# status                    = created, modified, deleted

print
