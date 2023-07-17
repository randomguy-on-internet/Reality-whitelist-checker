#!/bin/bash
cd /root
bash dns.sh &&
apt install pip &&
python3 -m pip install flask requests&&
# Download and extract Sing-Box
curl -Lo /root/sb https://github.com/SagerNet/sing-box/releases/download/v1.3.0/sing-box-1.3.0-linux-amd64.tar.gz &&
tar -xzf /root/sb &&
cp -f /root/sing-box-*/sing-box /root &&
rm -r /root/sb /root/sing-box-* &&
chown root:root /root/sing-box &&
chmod +x /root/sing-box
# Download Sing-Box configuration file
curl -Lo /root/sing-box_config.json https://raw.githubusercontent.com/randomguy-on-internet/fantastic-lamp/main/reality-singbox.json

# Download Sing-Box service file and reload systemd
curl -Lo /etc/systemd/system/sing-box.service https://raw.githubusercontent.com/iSegaro/Sing-Box/main/sing-box.service &&
systemctl daemon-reload

# Enable and start Sing-Box service
systemctl enable --now sing-box &&
sleep 0.2 &&
systemctl status sing-box &&
sleep 0.2
systemctl restart --now sing-box &&
sleep 0.2 &&
systemctl status sing-box &&

bash run_server.sh