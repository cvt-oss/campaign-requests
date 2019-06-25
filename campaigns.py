from datetime import datetime
from config import db
from models import CampaignRequests, CampaignRequestsSchema

def create(body):
    schema = CampaignRequestsSchema()
    new_campaign_request = schema.load(body, session=db.session).data

    db.session.add(new_campaign_request)
    db.session.commit()
    data = schema.dump(new_campaign_request).data

    return data, 201

