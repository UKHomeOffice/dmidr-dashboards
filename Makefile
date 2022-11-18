DOCKER_COMPOSE = docker-compose -f docker-compose.yml

build:
	${DOCKER_COMPOSE} build

serve: build
	${DOCKER_COMPOSE} up -d reporting-app

stop:
	cd hocs-mi-transformation && make stop
	${DOCKER_COMPOSE} down

serve-transformation: 
	git clone https://github.com/UKHomeOffice/hocs-mi-transformation.git
	cd hocs-mi-transformation && make redo && make serve

clean:
	rm -fr ./hocs-mi-transformation

logs:
	docker-compose logs -f reporting-app

shell:
	docker exec -it reporting-app bash