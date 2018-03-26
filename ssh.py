import paramiko


def generate__private__and__public__key(hostname, port, username, password, path_local=''):
    """
    The function generates a private key in the server where your application runs and a public key in the server
    with which you want to establish a connection.

    :param str hostname:
    :param int port:
    :param str username:
    :param str password:
    :param str path_path: route where the private and public key is stored in the local machine. Example: /home/robert/
    :return:
    """
    if isinstance(hostname, str) and \
            isinstance(port, int) and \
            isinstance(username, str) and \
            isinstance(password, str) and \
            isinstance(path_local, str):
        pass
    else:
        raise Exception('Incorrect parameters format')

    key = paramiko.RSAKey.generate(1024)
    key.write_private_key_file(path_local + 'id_rsa')

    with open(path_local + 'id_rsa.pub', "w") as public:
        public.write("%s %s" % (key.get_name(), key.get_base64()))
    public.close()

    pubkey = open("id_rsa.pub").read()

    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, port=port, username=username, password=password)
    try:
        h_input, h_output, h_error = ssh_client.exec_command('mkdir -p ~/.ssh/')
        error__private__and__public__key(h_error)
        h_input, h_output, h_error = ssh_client.exec_command('echo "%s" > ~/.ssh/authorized_keys' % pubkey)
        error__private__and__public__key(h_error)
        h_input, h_output, h_error = ssh_client.exec_command('chmod 600 ~/.ssh/authorized_keys')
        error__private__and__public__key(h_error)
        h_input, h_output, h_error = ssh_client.exec_command('chmod 700 ~/.ssh/')
        error__private__and__public__key(h_error)
    except Exception as e:
        raise Exception(e.__str__())
    finally:
        ssh_client.close()


def error__private__and__public__key(h_error):
    error = h_error.read().decode('utf-8')
    if error != '':
        raise Exception(error)


def execute_command_with_private_key(hostname, port, username, private_key_path, command):
    """
    The function establishes SSH connection with remote server, in which it executes a command and finally returns the
    result obtained in the standard output.

    :param hostname:
    :param port:
    :param username:
    :param private_key_path: private key path
    :param command: to execute
    :return:
    """
    if isinstance(hostname, str) and \
            isinstance(port, int) and \
            isinstance(username, str) and \
            isinstance(private_key_path, str) and \
            isinstance(command, str):
        pass
    else:
        raise Exception('Incorrect parameters format')

    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, port=port, username=username, key_filename=private_key_path)
    try:
        h_input, h_output, h_error = ssh_client.exec_command(command)
        error__private__and__public__key(h_error)
    except Exception as e:
        raise Exception(e.__str__())
    else:
        return h_output.read().decode('utf-8')
    finally:
        ssh_client.close()
