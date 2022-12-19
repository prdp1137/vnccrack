import pyvnc
import argparse
import sys

def authenticate_with_vnc(host, port, password_file):
    try:
        vnc = pyvnc.VNCClient(host=host, port=port)
    except Exception as e:
        print('Error: Could not connect to the VNC server')
        sys.exit(1)

    try:
        with open(password_file, 'r') as f:
            for password in f:
                password = password.strip()

                try:
                    if vnc.authenticate(password=password):
                        vnc.connect()
                        break
                except Exception as e:
                    continue
            else:
                print("Error: Could not authenticate with the VNC server. All passwords in the file have been tried.")
                sys.exit(1)
    except IOError:
        print('Error: Could not open the password file')
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-H', '--host', required=True, help='The hostname or IP address of the VNC server')
    parser.add_argument('-P', '--passwordfile', required=True, help='The path to the file containing the passwords')

    parser.add_argument('--port', default=5900, type=int, help='The port number of the VNC server (default: 5900)')

    args = parser.parse_args()

    if args.port < 0 or args.port > 65535:
        print('Error: Invalid port number')
        sys.exit(1)

    authenticate_with_vnc(args.host, args.port, args.passwordfile)
