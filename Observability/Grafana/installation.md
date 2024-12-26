The installation guide for grafana can be found [here](https://grafana.com/docs/grafana/latest/setup-grafana/installation/).

If you're on Kubernetes, you can use its native package manager, helm, to run the installation.

1. List the charts:
   - _helm search hub Grafana_ <br/>
2. Or go to the [Artifact hub](https://artifacthub.io/) to search for it
3. Add and update the repo you would like to get Grafana from:
   - _helm repo add grafana https://grafana.github.io/helm-charts_
   - _helm repo update_
3. Install it:
   - _helm install my-grafana grafana/grafana_
4. Access Grafana via web browser:
   - helm get notes my-grafana
   - Get the Grafana admin password:
     - kubectl get secret my-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
     - Save the decoded password to a file on your machine.
   - access Grafana service on the web browser:
     - export POD_NAME=$(kubectl get pods -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=my-grafana" -o jsonpath="{.items[0].metadata.name}")
   - Run the following port forwarding command to direct the Grafana pod to listen to port 3000:
     - kubectl port-forward $POD_NAME 3000
   - Navigate to 127.0.0.1:3000 in your browser
   - The Grafana sign-in page appears.
   - To sign in, enter admin for the username.
   - For the password paste it which you have saved to a file after decoding it earlier.

