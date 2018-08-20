from mininet.node import OVSSwitch
from mininet.topo import Topo
from mininet.util import irange, quietRun

n=10

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

class Star( Topo ):
    "Star Topology"

    def __init__( self ):
        "Create"

        # Initialize topology
        Topo.__init__( self )

        # Creating hosts and switches
        switches=[]
        hosts=[]

        for i in range(n):
            switches.append(self.addSwitch('s%s' % (i+1))) #Adding switches
            hosts.append(self.addHost('h%s' % (i+1))) #Adding hosts
            self.addLink(hosts[i], switches[i]) #linking hosts to corresponding switches
        switches.append(self.addSwitch('s%s' % (n+1))) #creating centre switch
        for i in range(n):
            self.addLink(switches[i],switches[n]) #linking switches

class Mesh( Topo ):
    "Mesh Topology"

    def __init__( self ):
        "Create"

        # Initialize topology
        Topo.__init__( self )

        # Creating hosts and switches
        switches=[]
        hosts=[]
        for i in range(n):
            switches.append(self.addSwitch('s%s' % (i+1), cls=OVSSwitch)) #Adding switches, making them OVS for STP
            hosts.append(self.addHost('h%s' % (i+1))) #Adding hosts
            self.addLink(hosts[i], switches[i]) #linking hosts to corresponding switches
        for i in range(n):
                for j in range(i+1,n):
                    self.addLink(switches[i],switches[j]) #linking switches

class Ring( Topo ):
    "Ring Topology"

    def __init__( self ):
        "Create"

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        switches=[]
        hosts=[]

        for i in range(n):
            switches.append(self.addSwitch('s%s' % (i+1), cls=OVSSwitch)) #Adding switches, making them OVS for STP
            hosts.append(self.addHost('h%s' % (i+1))) #Adding hosts
            self.addLink(hosts[i], switches[i]) #linking hosts to corresponding switches
        for i in range(n):
            self.addLink(switches[i],switches[(i+1)%n]) #linking switches
        self.addLink(switches[0],switches[n-1])

topos = { 'linear': ( lambda: Linear() ), 'star': ( lambda: Star() ), 'mesh': ( lambda: Mesh() ), 'ring': ( lambda: Ring() ), }
