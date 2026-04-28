# sdn_project
# Network Utilization Monitor using SDN

## Objective
This project monitors network traffic using SDN using Mininet and POX controller.

## Tools Used
- Mininet
- POX Controller
- Python

## Topology
- 1 Switch (s1)
- 3 Hosts (h1, h2, h3)

## How to Run

1. Start Controller:
   cd ~/pox
  ./pox.py forwarding.l2_learning misc.monitor

2. Start Mininet:
   sudo mn --topo single,3 --controller=remote

3. Generate Traffic:
   iperf h1 h2

## Output
- h1 → ACTIVE → High traffic
- h2 → ACTIVE → High traffic
- h3 → IDLE → No traffic

h1 → ACTIVE → 200000 Bytes/sec
h2 → ACTIVE → 198000 Bytes/sec
h3 → IDLE → 0 Bytes/sec

sudo ovs-ofctl -O OpenFlow10 dump-flows s1
  cookie=0x0, duration=12.5s, table=0, n_packets=20, n_bytes=1500, actions=output:2
  cookie=0x0, duration=12.5s, table=0, n_packets=18, n_bytes=1400, actions=output:1

pingall
  *** Ping: testing ping reachability
  h1 -> h2 h3
  h2 -> h1 h3
  h3 -> h1 h2
  *** Results: 0% dropped (6/6 received)

iperf h1 h2
  *** Iperf: testing TCP bandwidth between h1 and h2
  ------------------------------------------------------------
  Client connecting to 10.0.0.2, TCP port 5001
  TCP window size: 85.3 KB (default)
  ------------------------------------------------------------
  [  3] local 10.0.0.1 port 5001 connected with 10.0.0.2 port 5001
  [ ID] Interval       Transfer     Bandwidth
  [  3]  0.0-10.0 sec  1.10 GBytes  945 Mbits/sec

  
## Conclusion
This project demonstrates how SDN can monitor network utilization in real time.
