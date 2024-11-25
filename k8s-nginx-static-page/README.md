# Simple nginx static page for test on kubernetes cluster

kubectl apply -f every files<br />
To access to the page from the browser:<br />
1- kubectl --namespace ngninx port-forward service/nginx 8580:80 --address 0.0.0.0<br />
2- Port forward from firewall<br />