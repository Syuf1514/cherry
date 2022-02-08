# cherry 🍒
Basic docker project template for Machine Learning.

Supported: GPU (CUDA), pytorch, mount binds, volumes, host user, Jupyter.

### Requirements
```
docker >= 19.03.13
docker-compose >= 2.2.3
```

### Usage
I suggest using different services for different tasks, for example
`cherry-jupyter` for running jupyter server and `cherry`
for conducting ML experiments. Here `<service>` is any of the services
defined in `docker-compose.yml`.

First, define necessary environmental variables (`$USER_ID` and `$GROUP_ID` here, equal to your
`id -u` and `id -g` respectively). You may store these variabled in `.env` file in your project root along with
any secrets and tokens that your project needs.

Build and run container in shell mode (for administration):
```
docker compose build <service>
docker compose run --rm <service> bash
```
OR build container, start it and exit once finished:
```
docker compose up --build <service>
```
