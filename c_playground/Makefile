makefile_dir = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))
docker_linux_tag = rgardner/junkcode-cplayground-linux:latest

build-docker-linux:
	docker build docker/linux --tag $(docker_linux_tag)

run-docker-linux:
	docker run --interactive --tty --volume $(makefile_dir):/usr/src/cplayground --rm \
		--workdir /usr/src/cplayground $(docker_linux_tag) /bin/bash
