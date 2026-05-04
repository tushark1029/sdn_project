from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.recoco import Timer
import time

log = core.getLogger()

class Monitor(object):

    def __init__(self):
        core.openflow.addListeners(self)
        self.stats = {}

        # Map switch ports to hosts
        self.host_map = {
            1: "h1",
            2: "h2",
            3: "h3"
        }

        # Run every 5 seconds
        Timer(5, self._request_stats, recurring=True)

    def _request_stats(self):
        for connection in core.openflow._connections.values():
            connection.send(of.ofp_stats_request(
                body=of.ofp_port_stats_request()
            ))

    def _handle_PortStatsReceived(self, event):
        for stat in event.stats:
            port = stat.port_no

            # Ignore local port
            if port == 65534:
                continue

            tx = stat.tx_bytes
            rx = stat.rx_bytes

            key = (event.dpid, port)

            if key in self.stats:
                old_tx, old_rx, old_time = self.stats[key]
                time_diff = time.time() - old_time

                if time_diff > 0:
                    bandwidth = ((tx - old_tx) + (rx - old_rx)) / time_diff

                    host = self.host_map.get(port, f"Port {port}")

                    if bandwidth > 0:
                        print(f"{host} → ACTIVE → {bandwidth:.2f} Bytes/sec")
                    else:
                        print(f"{host} → IDLE → {bandwidth:.2f} Bytes/sec")

            # Store current values
            self.stats[key] = (tx, rx, time.time())


def launch():
    core.registerNew(Monitor)