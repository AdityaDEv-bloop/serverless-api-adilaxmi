import json
from services.changelanguage_service import ChangeLanguage

def changeLanguage(event, context):
    service = AllServices(event,context)
    tarnslated = service.change_language()
    response = {"statusCode": 200, "body": json.dumps(tarnslated)}

    return response
