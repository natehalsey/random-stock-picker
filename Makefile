clean:
	rm -rf *.venv

docker.start:
	sudo docker-compose up --build -d

docker.stop:
	sudo docker-compose down

docker.re:
	make docker.stop && make docker.start

bootstrap:
	. ./script/bootstrap
