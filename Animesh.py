from mininet.node import OVSSwitch
from mininet.topo import Topo
from mininet.util import irange, quietRun

class Linear( Topo ):
    "Linear Topology"

    def __init__( self ):
        "Create"

        # Initialize topology
        Topo.__init__( self )

        # Creating switches and hosts
        hosts = [ self.addHost( 'h%s' % h )
                  for h in irange( 1, 10 ) ]
        switches = [ self.addSwitch( 's%s' % s )
                     for s in irange( 1, 9 ) ]

        # Linking switches
        last = None
        for switch in switches:
            if last:
                self.addLink( last, switch )
            last = switch

        # Connecting hosts
        self.addLink( hosts[ 0 ], switches[ 0 ] )
        for host, switch in zip( hosts[ 1: ], switches ):
            self.addLink( host, switch )


class Star( Topo ):
    "Star Topology"

    def __init__( self ):
        "Create"

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        hosts = [ self.addHost( 'h%s' % h )
                  for h in irange( 1, 10 ) ]
        sw = self.addSwitch( 's0' )

        # Add links
        for host in hosts:
            self.addLink( host, sw )


class Mesh( Topo ):
    "Mesh Topology"

    def __init__( self ):
        "Create"

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        hosts = [ self.addHost( 'h%s' % h )
                  for h in irange( 1, 10 ) ]
        switches = [ self.addSwitch( 's%s' % s )
                     for s in irange( 1, 10 ) ]

        # Linking switches
        last = None
        for switch in switches:
            if last:
                self.addLink( last, switch )
            last = switch
        self.addLink(switches[9],switches[0])

        # Add links
        for host, switch in zip( hosts, switches ):
            self.addLink( host, switch )

        for i in range (0,switches.__len__()):
            for j in range (i+1,switches.__len__()):
                self.addLink( switches[i], switches[j] )


class Ring( Topo ):
    "Ring Topology"

    def __init__( self ):
        "Create"

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        hosts = [ self.addHost( 'h%s' % h )
                  for h in irange( 1, 10 ) ]
        switches = [ self.addSwitch( 's%s' % s )
                     for s in irange( 1, 10 ) ]

        # Linking switches
        last = None
        for switch in switches:
            if last:
                self.addLink( last, switch )
            last = switch
        self.addLink(switches[9],switches[0])

        # Add links
        for host, switch in zip( hosts, switches ):
            self.addLink( host, switch )

topos = { 'linear': ( lambda: Linear() ), 'star': ( lambda: Star() ), 'mesh': ( lambda: Mesh() ), 'ring': ( lambda: Ring() ), }