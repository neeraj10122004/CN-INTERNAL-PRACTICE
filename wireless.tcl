set ns [new Simulator]

set tf [open wireless.tr w]
$ns trace-all $tf

set nf [open wireless.nam w]
$ns namtrace-all-wireless $nf 500 500

set topo [new Topography]
$topo load_flatgrid 500 500

create-god 6

set val(chan) Channel/WirelessChannel

$ns node-config -adhocRouting AODV \
		-llType LL \
		-macType Mac/802_11 \
		-ifqType Queue/DropTail/PriQueue \
		-ifqLen 50 \
		-antType Antenna/OmniAntenna \
		-propType Propagation/TwoRayGround \
		-phyType Phy/WirelessPhy \
		-channel [new $val(chan) ] \
		-topoInstance $topo \
		-agentTrace ON \
		-routerTace OFF \
		-macTrace ON \
		-movementTrace OFF

set n0 [$ns node]
set n1 [$ns node]

$n0 set X_ 0
$n0 set Y_ 0
$n0 set Z_ 0

$n1 set X_ 100
$n1 set Y_ 100
$n1 set Z_ 0

$n0 random-motion 0
$n1 random-motion 0

$ns at 0 "$n0 setdest 400 400 40"
$ns at 0 "$n1 setdest 400 400 40"

set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp

set sink [new Agent/TCPSink]
$ns attach-agent $n1 $sink

$ns connect $tcp $sink

set cbr [new Application/Traffic/CBR]
$cbr attach-agent $tcp

$ns at 0 "$cbr start"
$ns at 10 "$cbr stop"

proc finish { } {
global ns nf tf 
$ns flush-trace
close $nf
close $tf
exec nam wireless.nam &
exit 0
}
$ns at 10 "finish"
$ns run
