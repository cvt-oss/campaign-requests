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
python3 install -r requirements.txt
```

### Run

``` bash
export PGUSER=campaign_requests
export PGPASSWORD=campaign_requests
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

Run migrations locally

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
