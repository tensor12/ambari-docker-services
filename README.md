# ambari-docker-service
## Setup
* 操作系统为centos7
* 下载docker service，运行下面命令

```
VERSION=`hdp-select status hadoop-client | sed 's/hadoop-client - \([0-9]\.[0-9]\).*/\1/'`
```
```
sudo git clone http://192.168.0.30/lihua/ambari-docker-service.git   /var/lib/ambari-server/resources/stacks/HDP/$VERSION/services/DOCKER
```

* Restart Ambari

```
ambari-server restart
```

* 登录ambari图形界面（http://localhost:8080）
* 点击Add Service添加服务
* 选择服务组件Docker
* 选择要安装的机器
* 安装部署

![a](screenshots/1.png)