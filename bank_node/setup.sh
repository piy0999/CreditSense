export LC_ALL="en_US.UTF-8"
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
sudo dpkg-reconfigure locales
git clone https://github.com/piy0999/CreditSense-Private.git
sudo apt install python3-pip
sudo pip3 install -r CreditSense-Private/bank_node/requirements.txt
cd /tmp
wget https://www.multichain.com/download/multichain-1.0.4.tar.gz
tar -xvzf multichain-1.0.4.tar.gz
cd multichain-1.0.4
sudo mv multichaind multichain-cli multichain-util /usr/local/bin
multichain-util create chain1
multichaind chain1 -daemon
sudo ufw allow 22
sudo ufw allow 5000
sudo ufw enable
cat ~/.multichain/chain1/params.dat
cat ~/.multichain/chain1/multichain.conf
