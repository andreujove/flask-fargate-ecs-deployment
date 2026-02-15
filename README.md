# 🚀 Flask Fargate ECS Deployment

## 🛠 Local Setup

### 1. Initialize Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Start application:
```bash
pip3 install -r requirements/requirements.txt
python3 main.py
```

### 3. Run tests:
```bash
pip3 install -r requirements/requirements-test.txt
pytest
```

## Docker setup:

### Execute the application:

```bash
make up TAG=2.0.0
```

### Execute tests
```bash
make tests
```




## Update ecs service in local:

```bash

aws ecs describe-task-definition --task-definition tp-flask-app-task --profile tp-exam > task-definition.json

cat task-definition.json | jq '.taskDefinition | 
  .containerDefinitions[0].image = "3********.dkr.ecr.eu-west-2.amazonaws.com/tp-flask-app:2.0.0" | 
  del(.taskDefinitionArn, .revision, .status, .registeredAt, .registeredBy, .requiresAttributes, .compatibilities)' > new_task_def.json

aws ecs register-task-definition     --cli-input-json file://new_task_def.json     --profile tp-exam

aws ecs update-service     --cluster tp-flask-app-ecs-cluster     --service tp-flask-app-ecs-service     --task-definition tp-flask-app-task     --profile tp-exam
```


# TO DO:

- gunicorn for prod environment.
- Environment variables + settings.
- volumes for development.
- reduce of size of docker images.
- linting: flake8, black, isort, etc..
- AI tools for coding.