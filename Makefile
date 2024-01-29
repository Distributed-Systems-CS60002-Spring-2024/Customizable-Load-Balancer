deploy:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

rmi:
	docker-compose down --remove-orphans --rmi all
