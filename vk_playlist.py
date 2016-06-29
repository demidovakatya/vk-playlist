"""
Creates a list of one's VK audios.
Output: csv.
"""

import requests
import os
import csv
from datetime import datetime


def get_url(token, user_id):
    url = "https://api.vkontakte.ru/method/audio.get.json?uid={uid}&access_token={a_token}".format(
            uid=user_id, a_token=token)
    return url

def get_tracklist(token, user_id):
    url = get_url(token, user_id)
    r = requests.get(url)
    return r.json()['response']

def save_tracklist_to_csv(tracklist):
    filename = os.path.join(".", 'output_' + \
                            (datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"))
    output_file = open(filename, 'w', newline='')
    output_writer = csv.writer(output_file)

    for i, track in enumerate(tracklist):
        print("Writing %s: %s - %s" % (i, track['artist'].encode('ascii', 'replace').decode('ascii'),
                                track['title'].encode('ascii', 'replace').decode('ascii')))
        output_writer.writerow( [track['artist'].encode('ascii', 'replace').decode('ascii'),
                                track['title'].encode('ascii', 'replace').decode('ascii'),
                                track['duration'],
                                track['url'].encode('ascii', 'replace').decode('ascii')]
                            )


if __name__ == '__main__':
    user_id = input("ID: ")
    token = os.getenv('VK_TOKEN')


    tracklist = get_tracklist(token, user_id)
    save_tracklist_to_csv(tracklist)

