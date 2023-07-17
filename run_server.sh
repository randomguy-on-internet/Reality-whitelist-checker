screen -dmS Python_server &&
screen -S Python_server -X stuff "python3 server.py$(printf \\r)" &&
screen -S Python_server -X detach
