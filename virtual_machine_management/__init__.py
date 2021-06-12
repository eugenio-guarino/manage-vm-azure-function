import logging
import commands
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

    if command == 'start':
        commands.start_vm()
        logging.info("This HTTP triggered function executed successfully", status_code=200)
    elif command == 'stop':
        commands.stop_vm()
        logging.info("This HTTP triggered function executed successfully", status_code=200)
