# flask-fargate-ecs-deployment


## Setup local:

1- Create virtual env: 
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2- Start application:
```bash
pip3 install -r requirements/requirements.txt
python3 main.py
```

3- Run tests:
```bash
pip3 install -r requirements/requirements-test.txt
pytest
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
- Environment variables + settings
- volumes for development
- reduce of size of docker images
