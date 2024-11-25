# Single node kubernetes cluster setup for test with rke

1- Setup ssh key<br />
<br />
2- Install docker<br />
<br />
3- Install kubectl<br />
<br />
4- Install rke CLI (change version):<br />
curl -LO https://github.com/rancher/rke/releases/download/v1.3.14/rke_linux-amd64<br />
sudo mv rke_linux-amd64 /usr/local/bin/rke<br />
sudo chmod +x /usr/local/bin/rke<br />
rke --version<br />
<br />
5- Create the cluster.yml File:<br />
rke config --empty --name cluster.yml<br />
<br />
6- Edit cluster.yml<br />
<br />
7- rke up<br />
If docker version error:<br />
rke up --ignore-docker-version<br />
<br />
8- Set Up kubectl:<br />
export KUBECONFIG=$(pwd)/kube_config_cluster.yml<br />

