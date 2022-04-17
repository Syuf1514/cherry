# cherry 🍒
Basic docker project template for Machine Learning.

Supported: GPU (CUDA), pytorch, mount binds, volumes, host user, Jupyter, pip cache mounting,
CUDA version from environment, freezed code for experiments and live code for Jupyter.

### Run with docker

Define environmental variables:
* `USER_ID` and `GROUP_ID`, equal to your user `id -u` and `id -g` respectively;
* `DEVICE` gpu you want to use (`0`);
* `CPUSET` cpu range you want to use (`0-15`);
* `BASE_IMAGE` tag of CUDA base image from docker hub fitting your CUDA driver (`11.3.1-cudnn8-devel-ubuntu20.04`);
* `TORCH_CUDA` torch cuda version, suffix in torch requirements (`cu102`, `cu111`, `cu113`, or add your own);
* `PYTHON_VERSION` version of python you want to install inside the container (`3.9`).

You may store these variables in `.env` file in your project root along with any secrets and tokens
that your project needs. Just make sure it is not tracked by git.

Dependencies can be configured in `docker-compose.yml`. Once done:
```
# to start jupyter server
run/jupyter

# to run an experiment
docker compose build cherry
docker compose run cherry
```
