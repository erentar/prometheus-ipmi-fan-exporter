python script written with ipmitool for monitoring fan speeds on Dell Rx20 servers. (may work on other machines with minimal adaptation.)

# Requirements
* python3
* ipmitool

# Installation
put prometheus_ipmi_fan_exporter.py to /usr/local/bin/<br>
put prometheus_ipmi_fan_exporter.service to /etc/systemd/system/

run `sudo systemctl enable prometheus_ipmi_fan_exporter; sudo systemctl restart prometheus_ipmi_fan_exporter`