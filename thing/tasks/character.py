from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient

from evething.celery import app


def get_client():
    http_client = RequestsClient()
    client = SwaggerClient.from_url("https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")
    return client

@app.task(name="character_info")
def character_info(token_id):
    pass
