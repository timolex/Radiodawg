import os
import time
import sys

TIMEOUT_SEC = 1
DNS_TO_QUERY = "8.8.8.8"
MUTE = " > /dev/null 2>&1"

def stop_playback():
    print("Stopping Volumio playback...")
    sys.stdout.flush()
    os.system("volumio stop")

def start_playback():
    print("Starting Volumio playback...")
    sys.stdout.flush()
    os.system("volumio play")

def is_net_reachable():
    response = os.system("ping -c 1 " + DNS_TO_QUERY + MUTE)
    if response is 0:
        return True
    else:
        return False

def is_streaming_webradio():
    response = os.system("volumio status | grep webradio" + MUTE)
    if response is 0:
        return True
    else:
        return False

while True:
    if is_streaming_webradio():
        if not is_net_reachable():
            print(DNS_TO_QUERY + " is not reachable, stopping Volumio playback")
            sys.stdout.flush()
            stop_playback()
            while not is_net_reachable():
                print(DNS_TO_QUERY + " is still not reachable, trying again in " + str(TIMEOUT_SEC) + " sec")
                sys.stdout.flush()
                time.sleep(TIMEOUT_SEC)
            print(DNS_TO_QUERY + " is reachable again, resuming Volumio playback now")
            sys.stdout.flush()
            start_playback()

    time.sleep(TIMEOUT_SEC)
