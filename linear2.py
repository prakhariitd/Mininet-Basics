from mininet.node import OVSSwitch
from mininet.topo import Topo
from mininet.util import irange, quietRun

class Linear(Topo):
    "Linear Topology"

    def __init__( self ):
        "Create"

        # Initialize topology
        Topo.__init__( self )

        # Creating switches and hosts
        switches=[]
        hosts=[]

        for i in range(n): 
            switches.append(self.addSwitch('s%s' % (i+1))) #Adding switches
            hosts.append(self.addHost('h%s' % (i+1))) #Adding hosts
            self.addLink(hosts[i], switches[i]) #linking hosts to corresponding switches
        for i in range(n-1):
            self.addLink(switches[i],switches[i+1]) #linearly linking switches