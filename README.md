# cherry 🍒
Basic docker project template for Machine Learning.

Supported: GPU (CUDA), pytorch, mount binds, volumes, host user, Jupyter, pip cache mounting,
CUDA version from environment, freezed code for experiments and live code for Jupyter.

Suggested project structure:
* `configs` for any configuration files (`.yaml`, `.json`, etc.);
* `figures` for images, tables and other easy accessable files;
* `lib` for code;
* `notebooks` for jupyter notebooks;
* `requirements` for pip-syntaxed requirements, `common.txt` for any and `torch+X.txt` for CUDA-dependent;
* `run` for docker bash scripts, configure permissions to execute files inside: `chmod +x run/*`;
* `.` for project service files.

### Run with docker

Define environmental variables:
* `USER_ID` and `GROUP_ID`, equal to your user `id -u` and `id -g` respectively;
* `DEVICE` gpu you want to use (`0`);
* `CPUSET` cpu range you want to use (`0-15`);
* `JUPYTER_PORT` port to expose for a jupyter server (`8000`);
* `BASE_IMAGE` tag of CUDA base image from docker hub fitting your CUDA driver (`nvidia/cuda:11.3.1-cudnn8-devel-ubuntu20.04`);
* `TORCH_CUDA` torch cuda version, suffix in torch requirements (`cu102`, `cu111`, `cu113`, or add your own);
* `PYTHON_VERSION` version of python you want to install inside the container (`3.9`).

You may store these variables in `.env` file in your project root along with any secrets and tokens
that your project needs. Just make sure it is not tracked by git.
Dependencies can be configured in `docker-compose.yml`.
Once done:
```
# to build docker image
docker compose build cherry

# to start jupyter server
run/jupyter

# to run an experiment
run/test
```
If you have problems with internet connection inside containers (can be on Fedora)
use `docker run` instead of `docker compose run`:
```
# to start jupyter server
run/docker jupyter
# inside container (docker@X: /cherry$) 
jupyter notebook --no-browser --ip 0.0.0.0 --port 8000
# Ctrl+P, Ctrl+Q to detach
```
