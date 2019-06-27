from flask import abort, make_response
from datetime import datetime
from .models import CampaignRequests, CampaignRequestsSchema, db


def create(body):
    """
    This function creates CampaignRequest for given request body

    :param body:          dict representing CampaignRequest to create
    :return:              created CampaignRequest
    """
    schema = CampaignRequestsSchema()
    new_campaign_request = schema.load(body, session=db.session).data

    db.session.add(new_campaign_request)
    db.session.commit()
    data = schema.dump(new_campaign_request).data

    return data, 201


def read_all():
    """
    This function returns all CampaignRequest

    :return:              All CampaignRequests
    """
    campaigns = CampaignRequests.query.order_by(CampaignRequests.id).all()
    campaign_schema = CampaignRequestsSchema(many=True)
    data = campaign_schema.dump(campaigns).data
    return data


def read_one(campaign_id):
    """
    This function returns CampaignRequest for given campaign_id

    :param campaign_id:   Id of CampaignRequest to find
    :return:              CampaignRequest matching id
    """
    campaign = CampaignRequests.query.filter(
        CampaignRequests.id == campaign_id).one_or_none()

    # Are we trying to read CampaignRequest that does not exist
    if campaign is None:
        return abort(
            404,
            f"Campaign request for id {campaign_id} not found",
        )

    campaign_schema = CampaignRequestsSchema()
    data = campaign_schema.dump(campaign).data
    return data


def update_one(campaign_id, body):
    """
    This function updates CampaignRequest for given campaign_id

    :param campaign_id:   id of CampaignRequest to update
    :param body:          dict representing new CampaignRequest
    :return:              created CampaignRequest
    """
    campaign = CampaignRequests.query.filter(
        CampaignRequests.id == campaign_id).one_or_none()

    # Are we trying to update CampaignRequest that does not exist
    if campaign is None:
        return abort(
            404,
            f"Campaign Request for id {campaign_id} does not exist",
        )

    schema = CampaignRequestsSchema()
    update_campaign = schema.load(body, session=db.session).data
    update_campaign.id = campaign_id

    db.session.merge(update_campaign)
    db.session.commit()

    updated_campaign = CampaignRequests.query.filter(
        CampaignRequests.id == campaign_id).one_or_none()
    if updated_campaign is None:
        return abort(
            500,
            f"Failed to read updated CampaignRequest",
        )

    data = schema.dump(updated_campaign).data
    return data, 200


def delete_one(campaign_id):
    """
    This function deletes CampaignRequest for given campaign_id

    :param campaign_id:   id of CampaignRequest to delete
    :return:              id of deleted CampaignRequest
    """
    campaign = CampaignRequests.query.filter(
        CampaignRequests.id == campaign_id).one_or_none()

    # Are we trying to update CampaignRequest that does not exist
    if campaign is None:
        return abort(
            404,
            f"Campaign Request for id {campaign_id} does not exist",
        )

    db.session.delete(campaign)
    db.session.commit()

    return make_response(f"Campaign Request with id {campaign_id} deleted",
                         200)
