FROM gcc:9.2

# Update and install dependencies, and remove the package manager cache. Do
# this in a single step for better caching.
RUN apt-get --yes update && apt-get install --yes --no-install-recommends \
        clang-format \
        clang-tidy \
        cmake \
        ninja-build \
        valgrind \
        && rm -rf /var/lib/apt/lists/*
