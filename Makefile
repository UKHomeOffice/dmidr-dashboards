DOCKER_COMPOSE = docker-compose -f docker-compose.yml

build:
	${DOCKER_COMPOSE} build

serve: 
	${DOCKER_COMPOSE} up -d reporting-app

stop:
	${DOCKER_COMPOSE} down
