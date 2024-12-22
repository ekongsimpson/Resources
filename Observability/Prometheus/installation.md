The installation guide for prometheus can be found [here](https://prometheus.io/docs/prometheus/latest/installation/).

If you're on Kubernetes, then you can use its native package manager, helm, to run the installation.

1. List the charts:
   - _helm search hub Prometheus_ <br/>
2. Or go to the [Artifact hub](https://artifacthub.io/) to search for it
3. Add and update the repo you would like to get Prometheus from:
   - _helm repo add prometheus-community https://prometheus-community.github.io/helm-charts_
   - _helm repo update_
3. Install it:
   - _helm install prometheus prometheus-community/prometheus_
4. After the installation expose the service to make it accessible from outside the cluster:
   - _kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext_
   
