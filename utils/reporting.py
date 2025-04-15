import allure
import json

def attach_response(status_code, response_body, name):
    combined_response = {
        "status_code": status_code,
        "response_body": response_body
    }
    response_text = json.dumps(combined_response, indent=2)
    allure.attach(
        response_text,
        name=f"{name} with Status",
        attachment_type=allure.attachment_type.JSON
    )