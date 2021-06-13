import logging
import azure.functions as func
from azure.cli.core import get_default_cli

def login():
    az_cli = get_default_cli()
    az_cli.invoke(['login', '--service-principal', '-u', '', '-p', '', '--tenant', ''])

    return az_cli

def start_vm():
    az_cli = login()
    az_cli.invoke(['vm', 'start', '-g', 'minecraft-server', '-n',  ''])

def stop_vm():
    az_cli = login()
    az_cli.invoke(['vm', 'deallocate',  '-g', 'minecraft-server', '-n',  ''])

def get_usage_information():
    az_cli = login()
    az_cli.invoke(['consumption', 'usage', 'list', '--subscription', '',\
         '--start-date', '2021-06-01'])


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    command = req.params.get('command')

    if command == 'start':
        start_vm()
    elif command == 'stop':
        stop_vm()