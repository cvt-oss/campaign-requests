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
python3 manage.py db init

# On changed schema
python3 manage.py db migrate
python3 manage.py db upgrade
```

Generate JS files:
```bash
npx babel --watch src --out-dir . --presets react-app/prod
```

### Cleanup

```bash
docker-compose down --volumes
```
