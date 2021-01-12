Radiodawg Volumio webradio watchdog
===

Radiodawg is a Volumio service handling automatic resuming of webradios in case of internet drop-outs.

Python script _radiodawg.py_ periodically (default timeout = 1 sec) queries Volumio's status to determine whether we are streaming a webradio. If so, it checks, whether a DNS service (default is 8.8.8.8, Google's DNS service) is reachable. If not, Volumio playback is stopped and is not resumed, until the DNS becomes reachable again.

### Setup

To install the Radiodawg service, copy/move _radiodawg.py_ to `/usr/bin/` and _radiodawg.service_ to `/lib/systemd/system/`.
Then, to enable the service (let it run automatically at startup), run the following command:

`$ sudo systemctl enable radiodawg.service`

Please note that up until now, Radiodawg has only been tested with Volumio 2.861 running on Raspberry Pi 3.
