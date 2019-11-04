# C Playground

## Getting Started

```sh
mkdir -p build
cd build
cmake -GNinja -DCMAKE_BUILD_TYPE:STRING=<Debug or Release> ..
cmake --build . --target runTests
```

### Linux on Docker

`docker/linux/Dockerfile` is provided for Linux development in a Docker
container. Use the provided `Makefile` to build and connect to the Linux
container.

```sh
make build-docker-linux
make run-docker-linux
```

### Using Valgrind

If valgrind is installed, use `-DC_PLAYGROUND_USE_VALGRIND:BOOL=ON` during
cmake's configure step to enable running the test executable under valgrind.
For convenience, the Linux Docker container has valgrind installed.

```sh
cmake -GNinja -DCMAKE_BUILD_TYPE:STRING=<Debug or Release> \
      -DC_PLAYGROUND_USE_VALGRIND:BOOL=ON ..
```
