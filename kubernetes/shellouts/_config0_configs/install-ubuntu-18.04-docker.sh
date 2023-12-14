# "install docker"
echo "######################################################################"
echo "install docker"
echo "######################################################################"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - || exit 1

apt-key fingerprint 0EBFCD88 || exit 1

add-apt-repository \
	   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
	      $(lsb_release -cs) \
	         stable" || exit 1

apt-get update -y
apt-get install docker-ce -y
