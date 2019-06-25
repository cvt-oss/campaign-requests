# Campaign Requester

Simple REST API to create requests for Campaigns.

## Initial setup

### Components

- Python3
  - virtualenv
  - Flask
  - Psycopg2
  - Flask-SQLAlchemy 
  - Flask-Migrate
  - Flask-Marshmallow
- Docker
- PostgreSQL

### Dev machine setup

Activate virtualenv 

``` bash
./bin/activate
```

### Run

``` bash
export DATABASE_URL="postgresql://localhost/campaign_requests"
python3 app.py
```

```bash
export POSTGRES_DB=campaign_requests 
export POSTGRES_USER=campaign_requests 
export POSTGRES_PASSWORD=campaign_requests 
docker-compose up -d
```

Connect to database
```bash
export PGHOST=localhost
export PGPORT=5432
export PGDATABASE=campaign_requests
export PGUSER=campaign_requests
export PGPASSWORD=campaign_requests
psql -X --set AUTOCOMMIT=off --set ON_ERROR_STOP=on
```

Run migrations

``` bash
# Initial setup
export FLASK_APP=config.py
flask db init

# On changed schema or after initialization
export PGUSER=campaign_requests
export PGPASSWORD=campaign_requests
export DATABASE_URL="postgresql://localhost/campaign_requests"
export FLASK_APP=config.py
flask db migrate
flask db upgrade
```

### Cleanup

```bash
docker-compose down --volumes
```
