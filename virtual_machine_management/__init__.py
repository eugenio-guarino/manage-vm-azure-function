import logging
import vmcommands
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    command = req.params.get('command')
    if not command:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            command = req_body.get('command')

    getattr(vmcommands,'command')