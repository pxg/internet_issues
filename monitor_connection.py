import os
from datetime import datetime
from subprocess import call
from time import sleep

DOWN_COUNT_LIMIT = 5
SLEEP_TIME_SECONDS = 2.5


def connection_check(hostname='google.com'):
    """
    Do we currently have a internet connection?
    Pings host with one packet.
    Allows a 2 second wait time for slow networks.
    http://stackoverflow.com/questions/2953462/pinging-servers-in-python
    """
    devnull = open(os.devnull, 'w')
    response = call(
        ['ping', '-c', '1', '-W', '2', hostname],
        stdout=devnull,
        stderr=devnull)
    return response == 0


def connection_changed(connnection, last_connection, down_count):
    """
    Print if the connection status has changed
    """
    if last_connection != connection:
        if connection:
            print('{} Internet is connected. Down count {}'.format(
                datetime.now(), down_count))
        else:
            print('{} Internet down. Down count {}'.format(
                datetime.now(), down_count))


def reconnect_to_network():
    """
    You will need to run sudo ifconfig without needing to input a password for
    this to work
    """
    os.system('sudo ifconfig en0 down; sudo ifconfig en0 up')


last_connection = None
down_count = 0
while True:
    connection = connection_check()
    connection_changed(connection, last_connection, down_count)
    last_connection = connection

    if connection is False:
        down_count += 1
    else:
        down_count = 0

    if down_count > DOWN_COUNT_LIMIT:
        reconnect_to_network()
    sleep(SLEEP_TIME_SECONDS)
