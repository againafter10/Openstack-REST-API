#!/usr/bin/env python

################################################################
# reference http://docs.openstack.org/user-guide
#################################################################



############# These libraries are required ###########
import urllib2
import json
import os_client_config
# import glanceclient.v2.client as glclient


nova_client = os_client_config.make_client(
    'compute',
    auth_url='http://localhost:5000',
    username='admin',
    password='admin_user_secret',
    project_name='admin',
    region_name='RegionOne')


glance_client = os_client_config.make_client(
    'image',
    auth_url='http://localhost:5000',
    username='admin',
    password='admin_user_secret',
    project_name='admin',
    region_name='RegionOne')


neutron_client = os_client_config.make_client(
    'network',
    auth_url='http://localhost:5000',
    username='admin',
    password='admin_user_secret',
    project_name='admin',
    region_name='RegionOne')



##################
# A NOVA Example #
##################

print ""
my_instances=nova_client.servers.list()
print "LIST OF INSTANCES"
print "================="
print my_instances
print ""
print ""


####################
# A GLANCE Example #
####################

generator = glance_client.images.list()
imagelist=list(generator)
for nextimage in imagelist:
   decoded = json.dumps(nextimage, sort_keys=True, indent=3)
   print "IMAGE" ; print "=====" ; print decoded ; print "" ; print ""



#####################
# A NEUTRON Example #
#####################

networks = neutron_client.list_networks()
print "NETWORKS"
print "========"

decoded = json.dumps(networks, sort_keys=True, indent=3)
print decoded


print "LIST OF NETWORKS"
print "================"
print  decoded
print ""
print ""



################################################
# A NEUTRON Example with creation of a Network #
################################################


network_name = 'MY-Testnet'
myparameters = {'network': {'name': network_name,'admin_state_up': True}}
mynetwork = neutron_client.create_network(body=myparameters)
net_dict = mynetwork['network']
network_id = net_dict['id']
print('Network %s created' % network_id)




quit()
