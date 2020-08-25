# Realtime Voice to Test Backend

## Memo

### Build docker image
```
docker build -t 044888744953.dkr.ecr.ap-northeast-1.amazonaws.com/realtime-v2t-backend:latest .
```

```
$(aws ecr get-login --region ap-northeast-1 --no-include-email)
```

```
docker push 044888744953.dkr.ecr.ap-northeast-1.amazonaws.com/realtime-v2t-backend:latest
```

### Configure ECS
```
ecs-cli configure profile --profile-name ecs-iju --access-key key --secret-key secret
ecs-cli configure --region ap-northeast-1 --cluster ecs-cli-demo --default-launch-type EC2 --config-name ecs-cli-demo
ecs-cli up --keypair demo-ecs --capability-iam --size 1 --instance-type t2.small --cluster-config ecs-cli-demo -ecs-profile ecs-iju
```

### Create ECS cluster
```
ecs-cli compose -f docker-compose-ecs.yaml create
```

### Start/Stop ECS cluster
```
ecs-cli compose -f docker-compose-ecs.yaml start
ecs-cli compose -f docker-compose-ecs.yaml stop
```
