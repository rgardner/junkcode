# C++ Playground

## Getting Started

### Prerequisites

```sh
pipx install invoke
```

### Building

```sh
invoke setup [--release] [--lint]
invoke test [--release]
```

### Formatting

```sh
invoke format [--release]
```

### Linting

```sh
invoke lint
```

### Using Docker

```sh
invoke docker-build docker-run
# Now on the guest machine
invoke setup test lint
```
