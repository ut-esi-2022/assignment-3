from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import os
import platform
import subprocess
import netifaces as ni
import shutil
import socket
import dns 
import dns.resolver

class HelloWorldService(ServiceBase):

    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>
        @param name the name to say hello to
        @param times the number of times to say hello
        @return the completed array
        """

        for i in range(times):
            yield u'Tere, %s' % name


    @rpc(Unicode, _returns=Unicode)
    def res_name(ctx, domain_name):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>
        @param domain_name the domain name to call host command on
        @return the return of host command
        """
        return os.popen(f'host {domain_name}').read()


    @rpc(Unicode, _returns=Unicode)
    def more_info(ctx, domain_name):
        ns = os.popen(f'dig NS {domain_name}').read()
        mx = os.popen(f'dig MX {domain_name}').read()
        soa = os.popen(f'dig SOA {domain_name}').read()

        return  "NS:\n" + ns + "\nMX:\n" + mx + "\nSOA:\n" + soa

application = Application([HelloWorldService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8090")
    logging.info("wsdl is at: http://localhost:8090/?wsdl")

    server = make_server('127.0.0.1', 8090, wsgi_application)
    server.serve_forever()
