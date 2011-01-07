'''
This service can be run with the following::

    twistd -ny modbus-udp.tac
'''
from twisted.application import service, internet
from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import DailyLogFile

from pymodbus.constants import Defaults
from pymodbus.server.async import ModbusUdpProtocol
from pymodbus.transaction import ModbusSocketFramer
from pymodbus.internal.ptwisted import InstallManagementConsole

def BuildService():
    '''
    A helper method to build the service
    '''
    context = None
    framer = ModbusSocketFramer
    server = ModbusUdpProtocol(context, framer)
    InstallManagementConsole({ 'server' : server })
    application = internet.UDPServer(Defaults.Port, server)
    return application

application = service.Application("Modbus UDP Server")
service = BuildService()
service.setServiceParent(application)
