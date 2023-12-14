wget https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
chmod +x minikube-linux-amd64
mv minikube-linux-amd64 /usr/local/bin/minikube

cat >> $HOME/.bash_profile << __EOF__
source <(kubectl completion bash)
__EOF__

cat > /etc/bash_completion.d/kubectl << __EOF__
source <(kubectl completion bash)
__EOF__

