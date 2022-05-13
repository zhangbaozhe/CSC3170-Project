# CSC3170 Group Project: Course Comment and Evaluation System

This is the repo contains the source code of thie project. The team members are

- Baozhe Zhang (Leader, 119010421)
- Yuyang Liang (119010174)
- Junxiao Liu (120090809)
- Yongqi Yu (120090761)

# How to run the code (for TA)

## Run in a docker container (recommended)

We use docker environment to run the code. The docker image can be found at [somewhere](). Please download it and unzip it using 

```bash
$ tar -zxvf image.tar.gz 
```

To run the docker image, first you need to load the image using the command
```bash
$ docker load < image.tar
```
Use `docker images` to check the new added image and copy the image ID as `<IMAGE_ID>`

Create the container using 
```bash
$ docker docker create -it --name csc3170 -p 3170:8000 -p 8080:8080 <IMAGE_ID> /bin/sh 
```
Use `docker container list` to check the new container named as csc3170 and remember the container ID as `<CONTAINER_ID>`

Execute the container by running 
```bash
$ docker start <CONTAINER_ID>
```
Once you start the container, you can execute it
```bash
$ docker exec -it <CONTAINER_ID> /bin/sh
```
Then you will enter a terminal which goes into the docker container. In the container, enter 
```bash
> cd csc3170
> ./run_backend.sh & ./run_frontend.sh 
```
Then in your host browser, enter `localhost:8080/login`. You can test the demo. 


