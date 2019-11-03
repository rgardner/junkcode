# C++ Playground

## Getting Started

### Building

```sh
mkdir build
cd build
cmake -GNinja -DCMAKE_BUILD_TYPE=<Debug or Release> ..
cmake --build . --target run
```

### Formatting

```sh
cmake --build . --target format
```

### Linting

```sh
cmake -GNinja \
  -DCMAKE_BUILD_TYPE=<Debug or Release> \
  "-DCMAKE_CXX_CLANG_TIDY=/usr/bin/clang-tidy" \
  ..
cmake --build .
```
