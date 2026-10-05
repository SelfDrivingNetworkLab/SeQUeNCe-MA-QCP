
import pypolatis
from pypolatis import PowerMonitorError, CrossConnectionError


class Polatis_API:
    def __init__(self,dev):
        try:
            self.session = pypolatis.Session(dev['username'], dev['user_type'], dev['interface'], dev['protocol'])
            self.session.login(dev['login_session'])
        except pypolatis.SessionError as e:
            print(e)


    def power_monitor_stats(self):
          try:
                buffer=self.session.powerMonitor()

                power_stats=dict.fromkeys(
                    ['intf_power','ports','opm_ports','configuration','alarmState','alarmThreshold','configuration'])
                power_stats['intf_power']=buffer.power()
                power_stats['ports']=buffer.ports()
                power_stats['opm_ports']=buffer.opm_ports
                power_stats['configuration']=buffer.configuration()
                power_stats['alarmState']=buffer.alarmState()
                power_stats['alarmThreshold']=buffer.alarmThreshold()
                power_stats['configuration'] = buffer.configuration() # tuple of (port number, wavelength, offset, average time for a single port)
                return power_stats

          except PowerMonitorError as e:
                print(e)

    def port_stats(self):
        #try:
            buffer=self.session.portManager()

            port_stats=dict.fromkeys(['getPorts','getPortStatus','getPeerPorts','getPortLabels'])
            port_stats['getPorts']=buffer.getPorts()
            port_stats['getPortStatus']=buffer.getPortStatus()
            port_stats['getPeerPorts']=buffer.getPeerPorts()
            port_stats['getPortLabels']=buffer.getPortLabels()
            return port_stats
        # except PortManagerError as e:
        #      print(e)

    def product_specs(self):
        #try:
            buffer=self.session.productInformation()

            specs=dict.fromkeys(
                ['productCode', 'serialNumber', 'softwareVersion', 'switchSize'])
            specs['productCode']=buffer.productCode()
            specs['serialNumber']=buffer.serialNumber()
            specs['softwareVersion']=buffer.softwareVersion()
            specs['switchSize']=buffer.switchSize()
            return specs
        #except ProductInformationError as e:
        #    print(e)

    def initilaize_OXC(self):
        try:
            self.oxc= self.session.crossConnection()
        except CrossConnectionError as e:
            print(e)

    def update_OXC(self):
        try:
            self.oxc= self.session.crossConnection()
        except CrossConnectionError as e:
            print(e)


    def port_OXC_stats(self):
        try:
            if not hasattr(self, 'oxc'):
                self.initilaize_OXC()
            return self.oxc.connection()
        except CrossConnectionError as e:
            print(e)

    def set_OXC(self,ingressPort_lst, egressPort_lst):
        try:
            if not hasattr(self, 'oxc'):
                self.initilaize_OXC()
            self.oxc.setConnection(ingressPort_lst, egressPort_lst)
        except CrossConnectionError as e:
            print(e)

    def remove_OXC(self,ingressPort_lst=None):
        try:
            if not hasattr(self, 'oxc'):
                self.initilaize_OXC()
            self.oxc.removeConnection(ingressPort_lst)
        except CrossConnectionError as e:
            print(e)


    def logout(self):
        self.session.logout()



