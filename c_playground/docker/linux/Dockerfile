FROM gcc:9.2

# Update and install dependencies, and remove the package manager cache. Do
# this in a single step for better caching.
RUN apt-get --yes update && apt-get install --yes --no-install-recommends \
        clang-tidy \
        cmake \
        ninja-build \
        python3-pip \
        python3-venv \
        valgrind \
        && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip \
        && python3 -m pip install --user pipx \
        && python3 -m pipx ensurepath \
        && python3 -m pipx install invoke
