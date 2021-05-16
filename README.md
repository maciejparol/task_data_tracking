### RUN LOCAL BACKEND

1. go to **data_tracking** directory

   ```shell
    cd data_tracking
    ```

2. install **requirements**:

   ```shell
    poetry install
    ```

3. set **database**:
   create database form sql `files config_files/config/init.sql` and `app/sql/init_app.sql`
   ```shell
    export DB_URL=postgresql://data_tracking:data_tracking@localhost:<YOUR_PORT>/data_tracking
    ```

4. **start** app
   ```shell
    cd app/api && poetry run uvicorn app:APP
    ```


### RUN LOCAL IN DOCKER

1. build the image

   ```shell
    docker-compose build
    ```
2. run container

   ```shell
    docker-compose up
    ```

* * * *

### Python version

    Python 3.9.5

### Before push Install the git hook scripts

    pre-commit install

* * * *

### docs
1. Local version

   http://127.0.0.1:8000/docs

2. Local in docker version

   http://127.0.0.1:80/docs

### Tests

   ```shell
   make test
   ```
