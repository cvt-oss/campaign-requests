from app import db


class CampaignRequests(db.Model):
    __tablename__ = 'campaign_requests'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return '<id {}>'.format(self.id)
