# clean up os
echo "######################################################################"
echo "clean up os"
echo "######################################################################"
apt-get update -y
service lxcfs stop
apt-get remove -y lxc-common lxcfs lxd lxd-client docker docker-engine docker.io

# "install base packages"
echo "######################################################################"
echo "install base packages"
echo "######################################################################"
apt-get update -y
apt-get install apt-transport-https ca-certificates curl software-properties-common -y 
apt-get upgrade
