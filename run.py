import vars
from ssh import generate__private__and__public__key, execute_command_with_private_key

try:
    generate__private__and__public__key(vars.hostname, vars.port, vars.username, vars.password, vars.path_local)
    execute_command_with_private_key(vars.hostname, vars.port, vars.username, vars.path_local + 'id_rsa', 'ls /')
except Exception as e:
    print(e.__str__())
