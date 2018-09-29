# kubernetes-gitlab

# create gitlab namespace
> $ kubectl create -f gitlab-ns.yaml

# deploy redis
> $ kubectl create -f emptyDir/git-redis.yaml

# deploy postgres
> $ kubectl create -f emptyDir/gitlab-postgres.yaml

# deploy gitlab 
> $ kubectl create -f emptyDir/gitlab.yaml

# deploy ingress controller
> $ kubectl create -f ingress/default-backend.yml
> $ kubectl create -f ingress/nginx-ingress-lb.yml
> $ kubectl create -f ingress/gitlab-ingress.yml



  Helm chart based on this manifests: https://github.com/lwolf/gitlab-chart

https://blog.lwolf.org/post/how-to-easily-deploy-gitlab-on-kubernetes/
