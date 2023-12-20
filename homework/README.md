Your goal is to create a machine learning pipeline with uptime monitoring.

## Short description

In short, once the docker compose is ran, the following should happen:
1. A Postgres database should be set up and populated with data (to do that, you need to find a way to run the .sql script in postgres/scripts)
2. A MySQL database should be set up, empty.
3. Another container should run the `main.py` python script in `pythonml`. This script fetches data from the Postgres database, builds a scikit-learn model, does predictions and saves them into the MySQL database. This script needs to be rerun every 30 seconds.
4. A container running [Adminer](https://www.adminer.org/) should be available to connect and view both databases
5. A container running [Uptime Kuma](https://github.com/louislam/uptime-kuma) should monitor the adminer application.

## Details about containers
You are free to decide where to write a Dockerfile and where to just use the image from docker hub.

### Postgres
- image: [postgres:16.1-bookworm](https://hub.docker.com/_/postgres)
- database name: `postgresdb`
- username: `postgresuser`
- password: `postgrespass`

### MySQL
- image: [mysql:8.2.0](https://hub.docker.com/_/mysql)
- database name: `mysqldb`
- username: `mysqluser`
- password: `mysqlpass`
- root password: `mysqlpass`

### PythonML
- image: [python:3.10-bookworm](https://hub.docker.com/_/python)

The script uses the same environment variables as MySQL and Postgres do, to define the user, password, and the database to access, so reuse them from the other two containers.

The CSV containing the predictions is saved to `/app/predictions/predictions.csv` inside the container.

All the Python dependencies are in `requirements.txt`

### Adminer
- image: [adminer:4.8.1-standalone0](https://hub.docker.com/_/adminer)
- the UI should be accessible at port [localhost:10000](http://localhost:10000)

### Uptime Kuma
- image: [louislam/uptime-kuma:1.23.10](https://hub.docker.com/r/louislam/uptime-kuma)
- the UI should be accessible at [localhost:10001](http://localhost:10001)

Uptime Kuma requires you to set up an account on first start, just enter something, it doesn't matter.


## Additional instructions

You should provide the following screenshots in the screenshots directory of the repo:
- Screenshot of the entered login form for Adminer to login to Postgres
- Screenshot from Adminer of the housing table in the Postgres database
- Screenshot of the entered login form for Adminer to login to MySQL
- Screenshot from Adminer of the predictions table in the MySQL database
- Screenshot of how you added a monitor to Uptime Kuma, to tell it to monitor Adminer
- Screenshot of how the main dashboard of Uptime Kuma looks (monitoring Adminer, status says Adminer is up).

You should also provide the predictions.csv from the model. Put it into the predictions directory in the repo.


Follow best practices:
- Do you need to map a certain port to host (i.e. the mysql/postgres port)?
- Do not write sensitive data like passwords in the docker-compose.yml file.
- Make sure that the order of container start ups makes sense - does it make sense for e.g. Adminer to start before the actual databases (Postgres/MySQL) are ready?
- Some environment variables may be needed in multiple containers. Can you make it so that these are defined only once (so if you have to change them, you only change them in one place).
- Write Dockerfiles such that you utilize caching of layers (changing the `main.py` script should not force Docker to reinstall dependencies from `requirements.txt` in the next build).