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

### API

#### Create campaign request

To create new Campaign Request, you can post form data as follows:

```BASH
http --form POST http://localhost:8000/api/v1/campaigns profile=someProfile \
      campaign_text="Some Campaign" \
      campaign_start=2017-07-21T17:32:28Z \
      approved=true \
      budget=100 \
      comment=Something \
      note=SomeNote \
      profile=someProfile \
      project_code=ZCZE33445 \
      row=10 \
      section=SomeSection \
      target_group=Czechs
```

And get response:

```
HTTP/1.0 201 CREATED
Content-Length: 324
Content-Type: application/json
Date: Wed, 26 Jun 2019 14:57:00 GMT
Server: Werkzeug/0.15.4 Python/3.7.3

{
    "approved": true,
    "budget": 100,
    "campaign_start": "2017-07-21T17:32:28+00:00",
    "campaign_text": "Some Campaign",
    "comment": "Something",
    "id": 3,
    "note": "SomeNote",
    "profile": "someProfile,someProfile",
    "project_code": "ZCZE33445",
    "row": 10,
    "section": "SomeSection",
    "target_group": "Czechs"
}

```

#### Get Campaign Requests

To list all Campaign Requests run following GET request:

```bash
http http://localhost:8000/api/v1/campaigns
```

And get response:

```
HTTP/1.0 200 OK
Content-Length: 709
Content-Type: application/json
Date: Wed, 26 Jun 2019 14:50:20 GMT
Server: Werkzeug/0.15.4 Python/3.7.3

[
    {
        "approved": true,
        "budget": 100,
        "campaign_start": "2017-07-21T17:32:28+00:00",
        "campaign_text": "Some Campaign",
        "comment": "Something",
        "id": 1,
        "note": "SomeNote",
        "profile": "someProfile,someProfile",
        "project_code": "ZCZE33445",
        "row": 10,
        "section": "SomeSection",
        "target_group": "Czechs"
    },
    {
        "approved": true,
        "budget": 100,
        "campaign_start": "2017-07-21T17:32:28+00:00",
        "campaign_text": "Some Campaign",
        "comment": "Something",
        "id": 2,
        "note": "SomeNote",
        "profile": "someProfile,someProfile",
        "project_code": "ZCZE33445",
        "row": 10,
        "section": "SomeSection",
        "target_group": "Czechs"
    }
]
```

#### Update Campaign Request

To update Campaign Request, you can post form data as follows:

``` bash
http --form PUT http://localhost:8000/api/v1/campaigns/3 profile=someProfile \
      campaign_text="Some Campaign" \
      campaign_start=2017-07-21T17:32:28Z \
      approved=true \
      budget=100 \
      comment=Something \
      note=SomeNote \
      profile=someProfile \
      project_code=ZCZE33445 \
      row=10 \
      section=SomeSection \
      target_group="Czechs and Slovaks"
```

And get response:

```
HTTP/1.0 200 OK
Content-Length: 336
Content-Type: application/json
Date: Wed, 26 Jun 2019 15:03:11 GMT
Server: Werkzeug/0.15.4 Python/3.7.3

{
    "approved": true,
    "budget": 100,
    "campaign_start": "2017-07-21T17:32:28+00:00",
    "campaign_text": "Some Campaign",
    "comment": "Something",
    "id": 3,
    "note": "SomeNote",
    "profile": "someProfile,someProfile",
    "project_code": "ZCZE33445",
    "row": 10,
    "section": "SomeSection",
    "target_group": "Czechs and Slovaks"
}
```

#### Delete Campaign Request

```bash
http DELETE http://localhost:8000/api/v1/campaigns/3
```

And get response:

```
HTTP/1.0 200 OK
Content-Length: 34
Content-Type: text/html; charset=utf-8
Date: Wed, 26 Jun 2019 15:06:41 GMT
Server: Werkzeug/0.15.4 Python/3.7.3

Campaign Request with id 3 deleted
```

### Cleanup

```bash
docker-compose down --volumes
```
