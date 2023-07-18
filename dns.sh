apt update -y &&
apt install resolvconf -y &&

#sudo systemctl status resolvconf.service &&

sudo systemctl start resolvconf.service &&

sudo systemctl enable resolvconf.service &&

curl -Lo /etc/resolvconf/resolv.conf.d/head https://raw.githubusercontent.com/randomguy-on-internet/fantastic-lamp/main/head &&

sudo resolvconf --enable-updates &&
sudo resolvconf -u &&

cat /etc/resolv.conf &&

sudo systemctl restart resolvconf.service &&
sudo systemctl restart systemd-resolved.service &&

clear && cat /etc/resolv.conf
