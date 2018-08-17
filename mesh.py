#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel,info
from mininet.node import RemoteController, OVSSwitch
from mininet.cli import CLI

def emptyNet():
	net = Mininet(topo=None, build=False)

	net.addController('c0', controller=RemoteController, ip="10.0.0.1", port=6633)
	h0 = net.addHost('h0', ip='10.0.0.1')
	h1 = net.addHost('h1', ip='10.0.2.1')
	h2 = net.addHost('h2', ip='10.0.2.2')
	h3 = net.addHost('h3', ip='10.0.2.3')
	h4 = net.addHost('h4', ip='10.0.2.4')
	h5 = net.addHost('h5', ip='10.0.2.5')
	h6 = net.addHost('h6', ip='10.0.2.6')
	h7 = net.addHost('h7', ip='10.0.2.7')
	h8 = net.addHost('h8', ip='10.0.2.8')
	h9 = net.addHost('h9', ip='10.0.2.9')
	h10 = net.addHost('h10', ip='10.0.2.10')
	switches=[]
	for i in range(11):
		switches.append(net.addSwitch('s%s' % (i+1), cls=OVSSwitch))
	net.addLink(h0,switches[10])
	hosts=[h1,h2,h3,h4,h5,h6,h7,h8,h9,h10]
	for i in range(10):
		net.addLink(hosts[i],switches[i])
	for i in range(11):
		for j in range(i+1,11):
			net.addLink(switches[i],switches[j])

	net.start()
	
	for i in range(4):
		switches[i].cmd('ifconfig s%s 10.0.1.%s' % (i+1,i+1))

	for i in range(4):
		switches[i].cmd('ovs-vsctl set bridge s%s stp-enable=true' % (i+1))
	CLI(net)
	net.stop()
	
if __name__ == '__main__':
	setLogLevel('info')
	emptyNet()
