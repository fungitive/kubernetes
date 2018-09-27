# mertics-server

https://github.com/kubernetes/kubernetes/tree/master/cluster/addons/metrics-server

需要修改的两个地方：

metrics-server-deployment.yaml #

- --source=kubernetes.summary_api:''

- --source=kubernetes.summary_api:https://kubernetes.default?kubeletHttps=true&kubeletPort=10250&insecure=true

resource-reader.yaml#

resources:

  - pods

  - nodes

   - namespaces

  - nodes/stats  #新加
