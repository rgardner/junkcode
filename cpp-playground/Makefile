makefile_dir = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))
docker_linux_tag = rgardner/junkcode-cppplayground-linux:latest

build-docker-linux:
	docker build docker/linux --tag $(docker_linux_tag)

run-docker-linux:
	docker run --interactive --tty \
		--volume $(makefile_dir):/usr/src/cpp-playground --rm \
		--workdir /usr/src/cpp-playground $(docker_linux_tag) /bin/bash
