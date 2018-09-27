# 说明
kubectl apply -f prometheus-config.yaml -f prometheus-deploy.yaml -f prometheus-rbac.yaml -f prometheus-service.yaml
上述操作成功后

将prometheus-config-add.yaml里配置加入到prometheus-config.yaml

kubectl apply -f prometheus-config.yaml
