#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel,info
from mininet.node import OVSSwitch
from mininet.cli import CLI

class RingTopo(Topo):
	def build(self, n=2):
		switches=[]
		hosts=[]
		for i in range(n):
			switches.append(self.addSwitch('s%s' % (i+1), cls=OVSSwitch))
			hosts.append(self.addHost('h%s' % (i+1)))
			self.addLink(hosts[i], switches[i])
		for i in range(n):
			self.addLink(switches[i],switches[(i+1)%n])

def simpleTest():
	topo = StarTopo(n=10)
	net = Mininet(topo)
	net.start()
	print "Dumping Host Connections"
	dumpNodeConnections(net.hosts)
	print "Testing network connectivity"
	CLI(net)
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	simpleTest()
