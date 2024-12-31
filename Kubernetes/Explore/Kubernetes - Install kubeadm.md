## HOW TO INSTALL KUBEADM

1. MY ENVIRONMENT: VMWare and Ubuntu 
2. DESKTOP HYPERVISOR: VMware Workstation 17 Pro
   - Workstation 17 Pro is now available free for Personal Use
   - You can register [here](https://profile.broadcom.com/web/registration) to get a copy
3. OS: ubuntu-24.04.1-live-server-amd64
4. After installing the OS on the workstation, login and start running the following commands:
   - Edit /etc/fstab and comment off /etc/fstab
   - sudo vim /etc/fstab
     - #/swapfile                               none            swap    sw              0       0
     - worker1:/mnt/data         /opt/my-nfs     nfs rsize=8192,wsize=8192,timeo=14,intr
   - Download and untar **containerd**:
     - wget https://github.com/containerd/containerd/releases/download/v2.0.1/containerd-2.0.1-linux-amd64.tar.gz
     - sudo tar Cxzvf /usr/local containerd-2.0.1-linux-amd64.tar.gz
   - Download and move **containerd service** under **systemd**
     - wget https://raw.githubusercontent.com/containerd/containerd/main/containerd.service
     - sudo mv containerd.service /usr/lib/systemd/system/containerd.service
     - sudo systemctl daemon-reload
     - sudo systemctl enable --now containerd
     - sudo systemctl status containerd.service
   - Download and install **runc**
     - wget https://github.com/opencontainers/runc/releases/download/v1.2.3/runc.amd64
     - sudo install -m 755 runc.amd64 /usr/local/sbin/runc
   - Download and untar **cni-plugin**
     - wget https://github.com/containernetworking/plugins/releases/download/v1.6.1/cni-plugins-linux-amd64-v1.6.1.tgz
     - sudo mkdir -p /opt/cni/bin
     - sudo tar Cxzvf /opt/cni/bin /home/user01/cni-plugins-linux-amd64-v1.6.1.tgz
   - Update the apt package index and install packages needed to use the Kubernetes apt repository
     - sudo apt-get update
     - sudo apt-get install -y apt-transport-https ca-certificates curl gpg
   - Download the public signing key for the Kubernetes package repositories. The same signing key is used for all repositories so you can disregard the version in the URL:
     - curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.32/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   - Add the appropriate Kubernetes apt repository. Please note that this repository have packages only for Kubernetes 1.31; for other Kubernetes minor versions, you need to change the Kubernetes minor version in the URL to match your desired minor version
     - echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
   - Now let's begin installing kubeadm:
     - sudo apt-get update
     - sudo apt-get install -y kubelet kubeadm kubectl
     - sudo systemctl enable --now kubelet
   - Before initializing **kubeadm** there're still a couple of commands we should run:
   - - sudo swapoff -a
     - sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
   - Initialize **kubeadm**:
     - sudo kubeadm init
   - Configure kubectl & copy the kubeconfig file your home directory:
   - - mkdir -p $HOME/.kube
     - sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
     - sudo chown $(id -u):$(id -g) $HOME/.kube/config
    
   ## TROUBLESHOOTING
   If after installations you start having **cni plugin not initialized** issues, ensure:

   - CoreDNS is running. If not, try inspect the related pod:
     - k -n kube-system describe pod/coredns-xxxxx-xxxxx. The events should give you a clue 
   - CNI plugin, such as **Calico** or **Flannel**, has been installed. Example:
     - Calico:
       - kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
     - Flannel:
       - kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
         
   Do not forget that sometimes, stopping and starting the nodes again can resolve the issue if there are transient problems

