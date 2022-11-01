from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def remoteNet():

    "Create an remote network and add nodes to it."

    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch, waitConnected=True )

    info( '*** Adding remote controller\n' )
    c0 = net.addController( 'c0', controller=RemoteController, ip="192.168.1.16", port=6633)

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )

    info( '*** Adding switch\n' )
    s3 = net.addSwitch( 's3', protocols="OpenFlow13" )

    info( '*** Creating links\n' )
    net.addLink( h1, s3 )
    net.addLink( h2, s3 )

    info( '*** Starting network\n')
    net.start()

    info( '*** Pinging all Hosts\n')
    net.pingAll()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    remoteNet()
