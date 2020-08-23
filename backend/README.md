# Realtime Voice to Test Backend

## Memo

### Build docker image
```
docker build -t 044888744953.dkr.ecr.ap-northeast-1.amazonaws.com/realtime-v2t-backend:latest .
```

### Create ECS cluster
```
ecs-cli compose -f docker-compose-ecs create
```