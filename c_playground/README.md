# C Playground

## Getting Started

```sh
invoke setup [--release] [--valgrind]
invoke test [--release] [--valgrind]
```

### Linux on Docker

`docker/linux/Dockerfile` is provided for Linux development in a Docker
container. Use the provided `docker-` tasks to build and connect to the Linux
container:

```sh
invoke docker-build docker-run
# Now on the guest machine
invoke setup test lint
```

### Using Valgrind

If valgrind is installed, use `-DC_PLAYGROUND_USE_VALGRIND:BOOL=ON` during
cmake's configure step to enable running the test executable under valgrind.
For convenience, the Linux Docker container has valgrind installed.

```sh
invoke setup --valgrind [--release]
invoke test --valgrind [--release]
```
