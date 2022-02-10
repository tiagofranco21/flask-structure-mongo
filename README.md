# Flask Application Structure with MongoDB

This application aims to serve as a template for APIs that intend to use mongoengine and flask-restx. One of the advantages of this application is to generate swagger documentation through schemas.

The general structure of the application can be seen below:

```
app_name
 |--api
    |--middleware
    |--resources
    |--schemas
 |--models
 |--logs
```

## Requirements to run with Docker
- Docker 
	-  https://docs.docker.com/get-docker/
- Docker Compose
	- https://docs.docker.com/compose/install/

## Requirements to run without Docker
- Python 3.8
	-  https://www.anaconda.com/distribution
- MongoDB (> v.4)
	- https://www.mongodb.com/download-center/community


# Configuration

Configuration is handled by environment variables, for development purpose you just
need to update / add entries in `.env` file.

It's filled by default with following content:

```
# FLASK
ENV=(development | production)
SECRET_KEY=FLASK_SECRET_KEY
PORT=8000 # app port

# MongoDB
MONGO_DB=app_name
MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_USER=
MONGO_PASS=
```

- If ENV=development, the application will be automatically reloaded when any change happens in the source files.

# Execute with Docker

Initially it is necessary to build the image, which contains the application and the Postgres database

```
docker-compose --build
```

 The command line below activates the application's container. 

```
docker-compose up
```

Navigate to `http://localhost:8000/api` to see all routes on swagger. 

# Execute without Docker

First create the environment in Anaconda
```
conda create -n MYENV python=3.8
```

Activate the environment in the terminal

```
conda activate MYENV 
```

Import the libraries

```
pip install -r ./app_name/requirements.txt
```

Run the application 

```
python index.py
```

Navigate to `http://localhost:8000/api` to see all routes on swagger. 

## Running pylint

To execute the code quality test with [Pylint](https://www.pylint.org/).

```
pylint ./app_name
```

# Author & Help

* [**Tiago Franco**](https://www.linkedin.com/in/tiago-sanches-franco)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details