from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.session.commit()
        ma.init_app(app)

    return app


class CampaignRequests(db.Model):
    __tablename__ = 'campaign_requests'

    id = db.Column(db.Integer, primary_key=True)
    profile = db.Column(db.String())
    campaign_text = db.Column(db.String())
    campaign_start = db.Column(db.DateTime(timezone=True))
    campaign_end = db.Column(db.DateTime(timezone=True))
    budget = db.Column(db.Integer())
    project_code = db.Column(db.String())
    row = db.Column(db.Integer())
    section = db.Column(db.String())
    target_group = db.Column(db.String())
    note = db.Column(db.String())
    comment = db.Column(db.String())
    approved = db.Column(db.Boolean())

    def __repr__(self):
        return '<id {}>'.format(self.id)


class CampaignRequestsSchema(ma.ModelSchema):
    class Meta:
        model = CampaignRequests
        sqla_session = db.session
