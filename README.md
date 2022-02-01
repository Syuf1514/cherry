# cherry
Basic docker project template for Deep Learning.

Supported: GPU (CUDA), pytorch, mount binds, volumes, host user, Jupyter.

### Requirements

```
docker >= 19.03.13
```

### Usage
```
# Build and run container in shell mode (for administation), some run options are ignored (see --help)
docker compose build cherry
docker compose run --rm cherry

# OR build and start container as specified
docker compose up --build cherry
```
