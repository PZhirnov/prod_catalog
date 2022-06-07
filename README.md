# prod_catalog

# Основные команды  для Docker
sudo docker-compose up --build

sudo docker-compose up --build --remove-orphans

sudo docker ps -a

sudo docker stop $(sudo docker ps -a -q)

sudo docker rm $(sudo docker ps -a -q)



# Войти в нужный контейнер:

sudo docker exec -ti -u0 catalog_project_nginx_1 /bin/bash


