#!/bin/bash
cp prometheus_ipmi_fan_exporter.py ./deb/usr/local/bin/prometheus_ipmi_fan_exporter.py
cp prometheus_ipmi_fan_exporter.service ./deb/lib/systemd/system/prometheus_ipmi_fan_exporter.service
dpkg -b ./deb ./prometheus-ipmi-fan-exporter_1.0.0-0_all.deb