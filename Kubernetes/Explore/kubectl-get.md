## kubectl get po<br />
One of commands Kubernetes admins use a lot is $${\color{red}kubectl \space get \space po.}$$<br />
Are you wondering what this does?<br />
Well, it will list all the pods in the default namespace in the current cluster - since you didn't specify a namespace.<br />
By the way, po stands for pods - because kubernetes admins would abbreviate everything if they could.<br />

Check this out [kubectl get po myapp -oyaml](https://github.com/ekongsimpson/Resources/blob/main/Kubernetes/Explore/kubectl-get-po.yaml)<br />


---



Now compare that with a json output.
[kubectl get po myapp -ojson](https://github.com/ekongsimpson/Resources/blob/main/Kubernetes/Explore/kubectl-get-po.json)<br />



---

## Note how rich the json output is!
