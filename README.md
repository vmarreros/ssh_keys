# ssh_keys

> SSK Keys Generation.
Use of paramiko to generate the private key and the public key. Establish SSH connection with a remote server through keys


The ***vars.py*** file contains the variables that are used to establish the connection to the remote server and the path in which the keys are generated on the local server
```
hostname = 'server.com'
port = 22
username = 'robertr'
password = '123gh*hg321'
path_local = '/home/robert'
```
In the ***run.py*** file, a simple example is shown where the keys are created and used to establish a connection with a remote server and execute commands in it.
