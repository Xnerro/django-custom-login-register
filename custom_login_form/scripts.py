from subprocess import call


def start():
    cmd = ["poetry", "run", "python", "app/manage.py", "runserver"]
    call(cmd, shell=True)
    
def migrations():
    cmd = ["poetry", "run", "python", "app/manage.py", "makemigrations"]
    call(cmd, shell=True)

def migrate():
    cmd = ["poetry", "run", "python", "app/manage.py", "migrate"]
    call(cmd, shell=True)
