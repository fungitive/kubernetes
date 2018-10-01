# kubernetes安装efk

fluentd定义DaemonSet时设置了 nodeSelector beta.kubernetes.io/fluentd-ds-ready=true ，所以需要在期望运行 fluentd 的 Node 上设置该标签；

    kubectl abel nodes node01 beta.kubernetes.io/fluentd-ds-ready=true
    
执行文件：

    kubectl apply -f .
    
    
