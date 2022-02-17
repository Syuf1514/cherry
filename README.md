# cherry 🍒
Basic docker project template for Machine Learning.

Supported: GPU (CUDA), pytorch, mount binds, volumes, host user, Jupyter, pip cache mounting,
CUDA version from environment, freezed code for experiments and live code for Jupyter.

### Requirements
```
docker >= 19.03.13
docker-compose >= 2.2.3
```

Environmental variables:
* `$USER_ID` and `$GROUP_ID`, equal to your user `id -u` and `id -g` respectively,
* `$CUDA_BASE` tag of official nvidia/cuda base image from dockerhub fitting your CUDA driver (version not greater
than that displayed by `nvidia-smi` on your machine, e.g. `11.1.1-cudnn8-devel-ubuntu20.04`),
* `$CUDA_TORCH` torch installation suffix appropriate to your `$CUDA_BASE` version, e.g. `cu111`.

You may store these variables in `.env` file in your project root along with any secrets and tokens
that your project needs. Just make sure it is not tracked by git.

### Usage
I suggest using different services for different tasks, for example `cherry-jupyter` for running jupyter server
and `cherry` for conducting ML experiments. Here `<service>` is any of the services  defined in `docker-compose.yml`.

Build and run container in shell mode (for administration):
```
docker compose build <service>
docker compose run --rm <service> bash
```
OR build container, start it and exit once finished:
```
docker compose up --build <service>
```
