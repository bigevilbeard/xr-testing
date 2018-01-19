#!/usr/bin/python
#
#
from napalm_base import get_network_driver
from prettytable import PrettyTable



Interface_Errors = PrettyTable(['Interface', 'RX Errors', 'Tx Errors', "MAC Address", "Port Up"])
Interface_Errors.padding_width = 1

Interface_Discards = PrettyTable(['Interface', 'RX Discards', 'Tx Discards', "MAC Address","Port Up"])
Interface_Discards.padding_width = 1

driver = get_network_driver('iosxr')
device = driver(hostname='10.4.37.15', username='cisco',
             password='cisco')
device.open()
# print help(device)
# interfaces_counters = device.get_interfaces_counters()
# print interfaces_counters
# interfaces = device.get_interfaces()
# print interfaces


interfaces_counters = device.get_interfaces_counters()
interfaces = device.get_interfaces()

for int, int_data in interfaces_counters.iteritems():
	Interface_Errors.add_row([int, int_data["rx_errors"], int_data["tx_errors"],interfaces[int]["mac_address"],interfaces[int]["is_up"]])
	Interface_Discards.add_row([int, int_data["rx_discards"], int_data["tx_discards"],interfaces[int]["mac_address"],interfaces[int]["is_up"]])

	if int_data["rx_errors"] > 0 or \
	   int_data["tx_errors"] > 0 or \
	   int_data["rx_discards"] > 0 or \
	   int_data["tx_discards"] > 0:
	   print "interface {} has errors" .format(int)

print "=" * 60
print Interface_Errors 
print "=" * 60
print Interface_Discards 