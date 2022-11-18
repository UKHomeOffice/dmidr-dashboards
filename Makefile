DOCKER_COMPOSE = docker-compose -f docker-compose.yml

build:
	${DOCKER_COMPOSE} build

serve: serve-transformation build
	${DOCKER_COMPOSE} up -d reporting-app

stop:
	rm -fr ./hocs-mi-transformation
	${DOCKER_COMPOSE} down

serve-transformation: 
	git clone https://github.com/UKHomeOffice/hocs-mi-transformation.git
	cd hocs-mi-transformation && make redo && make serve