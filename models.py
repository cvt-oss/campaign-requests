from config import db, ma
from sqlalchemy import DateTime


class CampaignRequests(db.Model):
    __tablename__ = 'campaign_requests'

    id = db.Column(db.Integer, primary_key=True)
    profile = db.Column(db.String())
    campaign_text = db.Column(db.String())
    campaign_start = db.Column(db.DateTime(timezone=True))


    def __init__(self, profile, campaign_text, campaign_start):
        self.profile = profile
        self.campaign_text = campaign_text
        self.campaign_start = campaign_start

    def __repr__(self):
        return '<id {}>'.format(self.id)


class CampaignRequestsSchema(ma.ModelSchema):
    class Meta:
        model = CampaignRequests
        sqla_session = db.session
