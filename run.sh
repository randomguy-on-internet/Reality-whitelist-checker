#!/bin/bash
cd /root

# Changing DNS
curl -Lo /root/dns.sh https://raw.githubusercontent.com/randomguy-on-internet/Reality-whitelist-checker/main/dns.sh &&
bash dns.sh &&

# Installing Python requirements
apt install pip -y &&
python3 -m pip install flask requests &&

# Download and extract Sing-Box Segaro Style XD
bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install --beta &&

# Download Sing-Box configuration file
curl -Lo /usr/local/etc/xray/config.json https://raw.githubusercontent.com/randomguy-on-internet/Reality-whitelist-checker/main/reality-xray.json

# Download Sing-Box service file from Segaro repo
systemctl daemon-reload

# Enable and start Sing-Box service
systemctl restart --now xray &&
sleep 0.2 &&
systemctl status xray &&

curl -Lo /root/run_server.sh https://raw.githubusercontent.com/randomguy-on-internet/Reality-whitelist-checker/main/run_server.sh &&
curl -Lo /root/server.py https://raw.githubusercontent.com/randomguy-on-internet/Reality-whitelist-checker/main/server.py &&

sleep 1 &&
bash run_server.sh &&
echo "run 'screen -ls' to find all detached screen and use 'screen -r sid' to check if its working properly"
