"""
http://stackoverflow.com/questions/2953462/pinging-servers-in-python
"""
import os
from datetime import datetime
from time import sleep

hostname = 'google.com'
# Wait time 2 seconds to allow for slow response or delays
ping_command = 'ping -c 1 -W 2 {} > /dev/null'.format(hostname)
last_response = None  # Initialise
down_count = 0

while True:
    response = os.system(ping_command)
    connection = response == 0

    if last_response != response:
        if connection:
            print('{} Internet is connected. Down count {}'.format(
                datetime.now(), down_count))
        else:
            # Don't need down count here
            print('{} Internet down. Down count {}'.format(
                datetime.now(), down_count))
            # TODO: fix with ifconfig en0 down; ifconfig en0 up
            # sudo ifconfig en0 down; sudo ifconfig en0 up
            # TODO: track intetenet outage here

    if connection is False:
        down_count += 1
    else:
        down_count = 0

    # TODO: restart here based on down count > 5

    last_response = response
    sleep(2.5)

# do
#   yup=`ping -c1 -t2 www.google.com|grep from`
#   if [[ -n $yup ]]
#      then echo "Internet is connected!"
#   else
#         ifconfig en0 down; ifconfig en0 up
#         echo "Down at `date +%m%d%Y%H%M%S`">>./dropped.out
#   fi
#   sleep 5
# clear
# done
