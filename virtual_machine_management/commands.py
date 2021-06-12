from azure.cli.core import azlogging, get_default_cli

def login():
    az_cli = get_default_cli()
    az_cli.invoke(['login', '--service-principal', '-u', '<appId>', '-p', 'password','--tenant','teanat id'])

    az_cli.invoke(['group','show', '-n', 'jimtest'])

    return az_cli

def start_vm():
    login()



def stop_vm():
    login()
