# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /code

COPY . /code

# install dependencies
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
# command to run on container start
CMD [ "./rest_server.py" ]