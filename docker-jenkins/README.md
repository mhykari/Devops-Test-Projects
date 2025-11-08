# Setup jenkins and jdk21 ssh agent using docker and test java api pipeline test<br />
- Docker compose file to setup a local jenkins with jdk21 ssh agent<br />
- A simple java api project for test gitlab ci/cd<br />
- jenkinsfile for java-api ci/cd<br />
<br />
This project deploy the jenkins controller and ssh agent to run pipeline for java-api ci/cd
How to use:<br />
1- Deploy jenkins and ssh agent:<br />
docker compose up -d<br />
2- Setup ssh key on jenkins controller and add this to .env file:<br />
docker exec -it jenkins bash<br />
su - jenkins<br />
rm -rf ~/.ssh<br />
mkdir -p ~/.ssh && chmod 700 ~/.ssh<br />
ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/id_rsa<br />
cat ~/.ssh/id_rsa.pub<br />
<br />
add the public key to .env file:<br />
JENKINS_AGENT_SSH_PUBLIC_KEY="$cat ~/.ssh/id_rsa.pub"<br />
<br />
docker compose up -d agent<br />
<br />
Test ssh in controller container:<br />
ssh jenkins@jenkins_agent<br />
<br />
3- Add ssh agent on jenkins UI:<br />
Remote root directory: /home/jenkins/agent<br />
Launch method: Launch agents via SSH<br />
Host: jenkins_agent<br />
Add Credential:<br />
Username: jenkins<br />
Private Key: "/var/jenkins_home/.ssh/id_rsa" #private key of jenkins user in controller node<br />
<br />
4- Create Pipeline Project<br />
sudo gitlab-runner install --user=root --working-directory=/root/gitlab-runner<br />
gitlab-runner register<br />
gitlab-runner verify<br />
<br />
5- Create jenkinsfile or copy the content of jenkinsfile in pipline in jenkins controller UI
<br />
6- check http://127.0.0.1:8085 to verify the test project deployed successfully.<br />