## kubectl get po<br />
One of commands Kubernetes admins use a lot is $${\color{red}kubectl \space get \space po.}$$<br />
Are you wondering what this does?<br />
Well, it will list all the pods in the default namespace in the current cluster - since you didn't specify a namespace.<br />
By the way, po stands for pods - because kubernetes admins would abbreviate everything if they could.<br />

Try $${\color{red}kubectl \space get \space po \space myapp -oyaml.}$$<br />

---
apiVersion: v1
kind: Pod
metadata:
  annotations:
    cni.projectcalico.org/containerID: fd6f8f1d456e987fe653a025c025fff6de925932499e5465219461d496e28607
    cni.projectcalico.org/podIP: 10.1.156.168/32
    cni.projectcalico.org/podIPs: 10.1.156.168/32
  creationTimestamp: "2023-12-18T21:54:13Z"
  labels:
    app: myapp
  name: myapp
  namespace: default
  resourceVersion: "12617057"
  uid: b287e9d0-3630-4db3-8939-eeaf1079565a
spec:
  containers:
  - image: nginx
    imagePullPolicy: Always
    name: nginx-container
    resources: {}
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-xc278
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: hp-g5.platform.ing
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - name: kube-api-access-xc278
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2023-12-18T21:54:13Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2024-12-10T20:05:25Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2024-12-10T20:05:25Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2023-12-18T21:54:13Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: containerd://3c2a5680f63863e06f9350f66bd24170014eb7199edb2b26e829fa43f2bbaa51
    image: docker.io/library/nginx:latest
    imageID: docker.io/library/nginx@sha256:fb197595ebe76b9c0c14ab68159fd3c08bd067ec62300583543f0ebda353b5be
    lastState:
      terminated:
        containerID: containerd://0baa131a95ccd446f08904dc5abe7bc5e9edbdd81de928135615165ba34e9091
        exitCode: 255
        finishedAt: "2024-12-10T20:04:46Z"
        reason: Unknown
        startedAt: "2024-12-09T20:01:45Z"
    name: nginx-container
    ready: true
    restartCount: 369
    started: true
    state:
      running:
        startedAt: "2024-12-10T20:05:24Z"
  hostIP: 192.168.0.112
  phase: Running
  podIP: 10.1.156.168
  podIPs:
  - ip: 10.1.156.168
  qosClass: BestEffort
  startTime: "2023-12-18T21:54:13Z"
---
