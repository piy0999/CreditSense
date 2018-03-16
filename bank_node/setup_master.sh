echo '1. Setting up ubuntu locale...'
export LC_ALL="en_US.UTF-8"
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
sudo dpkg-reconfigure locales
echo '2. Cloning github...'
git clone http://github.com/piy0999/CreditSense.git
cd ~/CreditSense
git config credential.helper store
cd ~
echo '3. Installing python3 pip...'
sudo apt-get update
sudo apt -y install python3-pip
echo '4. Installing packages...'
sudo pip3 install -r ~/CreditSense/bank_node/requirements.txt
echo '5. Installing multichain...'
cd ~/tmp
wget https://www.multichain.com/download/multichain-1.0.4.tar.gz
tar -xvzf multichain-1.0.4.tar.gz
cd multichain-1.0.4
sudo mv multichaind multichain-cli multichain-util /usr/local/bin
cd ~
echo '6. Creating multichain chain and stream...'
multichain-util create chain1 -setup-first-blocks=1 -admin-consensus-admin=0.6
sed -i -e 's/anyone-can-connect = false/anyone-can-connect = true/g' ~/.multichain/chain1/params.dat
#sed -i -e 's/anyone-can-send = false/anyone-can-send = true/g' ~/.multichain/chain1/params.dat
#sed -i -e 's/anyone-can-receive = false/aanyone-can-receive = true/g' ~/.multichain/chain1/params.dat
multichaind chain1 -daemon
multichain-cli chain1 create stream strm1 true
echo '7. Setting up local credentials for multichain...'
port=`sudo grep default-rpc-port ~/.multichain/chain1/params.dat | grep -oP '[0-9]{4}'`
networkport=`sudo grep default-network-port ~/.multichain/chain1/params.dat | grep -oP '[0-9]{4}'`
password=`sudo grep rpcpassword  ~/.multichain/chain1/multichain.conf | cut -d'=' -f2`
cat >~/CreditSense/bank_node/API/credentials.json <<EOF
    {
      "rpcuser": "multichainrpc",
      "rpcpasswd": "$password",
      "rpchost": "localhost",
      "rpcport": "$port",
      "chainname": "chain1"
    }
EOF
echo '8. Opening ports....'
sudo ufw allow 22
sudo ufw allow 5000
sudo ufw allow $networkport
sudo ufw --force enable
nodeaddress=`multichain-cli chain1 getinfo | grep "nodeaddress" | cut -d '"' -f4`
echo "Connect to $nodeaddress from other nodes"
echo '9. Starting flask server...'
cd ~/CreditSense/bank_node/API
python3 app.py
