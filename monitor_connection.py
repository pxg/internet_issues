import os
from datetime import datetime
from time import sleep

hostname = 'google.com'
ping_command = 'ping -c 1 {} > /dev/null'.format(hostname)
last_response = 1

while True:
    response = os.system(ping_command)
    # TODO: log to file
    if last_response != response:
        if response == 0:
            print('Internet is connected {}'.format(datetime.now()))
        else:
            print('Internet Down {}'.format(datetime.now()))
        sleep(1)
    last_response = response

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
