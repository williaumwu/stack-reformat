# "install kvm"
echo "######################################################################"
echo "install kvm"
echo "######################################################################"
apt-get -y install qemu-kvm libvirt-bin virt-top libguestfs-tools virtinst bridge-utils
modprobe vhost_net
lsmod | grep vhost
echo vhost_net >> /etc/modules
