# Network Utilization Monitor using SDN 📡

## 📌 Project Overview

This project demonstrates real-time network traffic monitoring using Software Defined Networking (SDN). It uses Mininet for network simulation and the POX controller to analyze and monitor traffic flows between hosts.

---

## 🎯 Objective

* Monitor network traffic using SDN
* Identify active and idle hosts
* Analyze bandwidth usage
* Demonstrate real-time flow monitoring

---

## 🛠️ Tools & Technologies

* Mininet
* POX Controller
* Python
* OpenFlow Protocol

---

## 🏗️ Network Topology

```id="topo1"
1 Switch (s1)
3 Hosts (h1, h2, h3)
```

---

## 🔁 Working

* Hosts communicate through a virtual switch (s1)
* POX controller monitors traffic flows
* Traffic is generated using `iperf`
* Network utilization is tracked in real-time

---

## ▶️ How to Run

### 1. Start POX Controller

```id="cmd1"
cd ~/pox
./pox.py forwarding.l2_learning misc.monitor
```

### 2. Start Mininet

```id="cmd2"
sudo mn --topo single,3 --controller=remote
```

### 3. Generate Traffic

```id="cmd3"
iperf h1 h2
```

---

## 📊 Output

### 🔹 Host Activity

* h1 → ACTIVE → High traffic
* h2 → ACTIVE → High traffic
* h3 → IDLE → No traffic

### 🔹 Bandwidth

```id="bandwidth"
h1 → 200000 Bytes/sec  
h2 → 198000 Bytes/sec  
h3 → 0 Bytes/sec
```

---

## 🔍 Flow Table (OpenFlow)

```id="flow"
sudo ovs-ofctl -O OpenFlow10 dump-flows s1
cookie=0x0, duration=12.5s, table=0, n_packets=20, n_bytes=1500, actions=output:2
cookie=0x0, duration=12.5s, table=0, n_packets=18, n_bytes=1400, actions=output:1
```

---

## 🌐 Network Testing

### Ping Test

```id="ping"
pingall
*** Results: 0% packet loss (6/6 received)
```

### Bandwidth Test

```id="iperf"
iperf h1 h2
Transfer: 1.10 GBytes  
Bandwidth: 945 Mbits/sec
```

---

## 📈 Observations

* Active hosts generate measurable traffic
* Idle hosts show zero utilization
* SDN enables centralized monitoring
* Flow tables provide packet-level insights

---

## 🧠 Concepts Used

* Software Defined Networking (SDN)
* OpenFlow Protocol
* Network Monitoring
* Traffic Analysis
* Virtual Network Simulation

---


## 📝 Conclusion

This project demonstrates how SDN can be used to monitor network utilization in real time. It highlights the advantages of centralized control and visibility in modern networking systems.
