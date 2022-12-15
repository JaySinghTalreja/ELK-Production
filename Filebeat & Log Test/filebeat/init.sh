#!/bin/bash

#run filebeat in usr/share/filebeat
current_dir=$(pwd)
echo "Current Dir:" + $current_dir
#excutes a non-ending background process ./filebeat -e without blocking the shell
nohup ./filebeat -e &
#cd to logs generator script /home/Logs/generate.py
cd /home/Logs

# Read all log files a sample file.log is pushed just to note the logs are being generated
# chmod +x *.log
nohup tail -F * &
# -u unbuffered output to print out in docker console
#excutes a non-ending background process python3 -u generate.py without blocking the shell
# nohup python3 -u generate.py &

#cd back to the filebeat directory
cd $current_dir
echo "Back to Dir:" + $current_dir
#wait before all the background process are working, if the shell closes the container will close as it is the entrypoint for the container
wait