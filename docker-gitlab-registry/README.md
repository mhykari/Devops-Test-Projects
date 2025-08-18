# Setup gitlab with local gitlab registry<br />
- Docker compose file to setup a local gotlab with local gitlab registry<br />
- A simple java api project for test gitlab ci/cd<br />
- gitlab-ci files for shell runner and docker runner<br />
- gitlab-runner config file to use docker runner on dood mode<br />
<br />
How to use:<br />
1- Setup gitlab with change the marked vars in docker compose file<br />
docker compose up -d<br />
2- Setup your gitlab registry on docker daemon file on /etc/docker/daemon.json then restart docker with this:<br />
{<br />
  "insecure-registries": ["127.0.0.1:5100"]<br />
}<br />
<br />
3- Test push and pull images:<br />
docker login your-gitlab-domain:5100 <br />
docker tag my-image:latest your-gitlab-domain:5100/username/project/image-name:tag <br />
docker push your-gitlab-domain:5100/username/project/image-name:tag <br />
<br />
4- Install and setup gitlab runner and register runners<br />
sudo gitlab-runner install --user=root --working-directory=/root/gitlab-runner<br />
gitlab-runner register<br />
gitlab-runner verify<br />
<br />
* Change the gitlab runner config.toml in ~/.gitlab-runner/config.toml if you are using the docker runner.<br />
<br />
5- Use the project and gitlab-ci.ynm file in repo tu build and deploy the java api test project<br />
<br />
6- check http://127.0.0.1:8080/api/hello to verify the test project deployed successfully.<br />