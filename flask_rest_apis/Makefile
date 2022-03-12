
NAME:=py_rest_server
DOCKER_REPOSITORY:=dsatya6
DOCKER_IMAGE_NAME:=$(DOCKER_REPOSITORY)/$(NAME)
VERSION:=0.1.0

.PHONY: build clean test build-container push-container test-container

build :
	python3 rest_server.py

clean :
	@echo ""

test:
	#@pytest
	python3 rest_server.py &
	sleep 5
	# pytest
	curl http://localhost:5000/\?name\=savir

build-container :
	@docker build -t dsatya6/$(NAME):$(VERSION) .

push-container :
	@docker push dsatya6/$(NAME):$(VERSION)

test-container :
	@docker rm -f $(NAME) || true
	# python server is running a 5000, map to docker 5000
	@docker run -dp 5000:5000 --name=$(NAME) $(DOCKER_IMAGE_NAME):$(VERSION)
	@docker ps
	@sleep 5
	@curl http://localhost:5000/\?name\=savir
	@echo ""
	@sleep 2
	@docker stop $(NAME) || true
	@docker rm -f $(NAME) || true