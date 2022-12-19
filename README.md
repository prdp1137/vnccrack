# VNC Bruteforce

This script allows to bruteforce a VNC server using a list of passwords.

## Usage
```
python3 vnccrack.py [-H] [-P] [--port]
```

## Options
```
-H, --host: The hostname or IP address of the VNC server (required)
-P, --passwordfile: The path to the file containing the passwords (required)
--port: The port number of the VNC server (default: 5900)
```

## Example
To authenticate with the VNC server at localhost using the passwords in the file passwords.txt:

```
python3 vnccrack.py -H localhost -P passwords.txt
```
To specify a port number other than the default (5900):

```
python vnccrack.py -H localhost -P passwords.txt --port 5901
```

## To Do
- [ ] Modify the script such that password spray within the CIDR
