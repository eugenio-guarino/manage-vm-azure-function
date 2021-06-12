from azure.cli.core import get_default_cli

def login():
    az_cli = get_default_cli()
    az_cli.invoke(['login', '--service-principal', '-u', '<appId>', '-p', '<password>', '--tenant', '<teanat id>'])

    return az_cli

def start_vm():
    az_cli = login()
    az_cli.invoke(['vm', 'start', '--name', '<vm_name>', '--resource_group', '<mygroup>'])

def stop_vm():
    az_cli = login()
    az_cli.invoke(['vm', 'stop', '--name', '<vm_name>', '--resource_group', '<mygroup>'])

def get_usage_information():
    az_cli = login()
    az_cli.invoke(['consumtpion', 'usage', 'list', '--subscription', '<my_subscription>',\
         '--start-date', 'YYYY-MM-DD', '--end-date', 'YYYY-MM-DD'])

