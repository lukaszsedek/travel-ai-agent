APP_NAME=travel-buddy-agent

build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

logs:
	docker-compose logs -f

restart:
	docker-compose down && docker-compose up --build

clean:
	docker-compose down -v --remove-orphans

shell:
	docker exec -it $(APP_NAME) /bin/sh
