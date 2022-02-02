# cherry 🍒
Basic docker project template for Machine Learning.

Supported: GPU (CUDA), pytorch, mount binds, volumes, host user, Jupyter.

### Requirements
```
docker >= 19.03.13
```

### Usage
I suggest using different servies for different tasks, for example
`cherry_jupyter` for running jupyter server and `cherry_experiment`
for conducting ML experiments. Here `<service>` is any of the services
defined in `docker-compose.yml`.

Build and run container in shell mode (for administration):
```
docker compose build <service>
docker compose run <service> bash
```
OR build container, start it and exit once finished:
```
docker compose up --build <service>
```

### TODO
* mount pip cache
