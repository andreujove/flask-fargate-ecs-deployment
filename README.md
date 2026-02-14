# flask-fargate-ecs-deployment


## Setup local:

1- Create virtual env: 
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2- Start application:
```bash
pip install flask
python3 main.py
```

## Docker setup:

### Execute the application:

```bash
make up
```

### Execute tests
```make
make tests
```

# TO DO:

- gunicorn for prod environment
- volumes for development
- reduce of size of docker images
