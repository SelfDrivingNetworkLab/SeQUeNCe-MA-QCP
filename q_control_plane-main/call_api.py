
from pprint import pprint

from polatis_api import Polatis_API

Polatis_dev1=\
    {
    'username' : 'admin',
    'user_type' : 'admin',
    'interface' : '192.168.56.101',
    'protocol' : 'tl1',
    'login_session' : 'root'
}


Polatis_1 = Polatis_API(Polatis_dev1)
print(Polatis_1.power_monitor_stats())
print(Polatis_1.port_stats())
print(Polatis_1.product_specs())
print('##########################')
Polatis_1.set_OXC([7], [55])
print(Polatis_1.port_OXC_stats())
Polatis_1.set_OXC([8], [54])
print(Polatis_1.port_OXC_stats())
Polatis_1.remove_OXC()
print(Polatis_1.port_OXC_stats())
Polatis_1.logout()
