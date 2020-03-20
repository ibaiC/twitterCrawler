from collections import Counter 
import numpy as np
import pandas as pd
import json
import string
import itertools
import time

"""
This program takes the tweets.json file and analyses its hashtags, user mentions and concepts.
"""

def get_tweet_hashtags(t_id):
    tweets_file = open("tweets.json", 'r', encoding='utf-8')
    tweets_file.seek(0)
    hashtags = []
    for line in tweets_file:
        tweet = json.loads(line)
        if str(tweet["id"]["$numberLong"]) == str(t_id).strip():
            hashtags = tweet["entities"]["hashtags"]
            tags = []
            for i in hashtags:
                if len(hashtags) > 0:
                    tags.append(i["text"])
                    print(tags)
            return tags
    print("returning empty hashtags")
    return hashtags
    

clustered_data = open("output/output.txt", 'r', encoding='utf-8')

# Setting output file for analysis of hashtags of each cluster
output_file = open("output/cluster_hashtags.txt", "w", encoding='utf-8')
print("Top 10 Hashtags of each cluster: ", file = output_file)


# Get the hashtags of each tweet searched by ID
cluster_hashtags = {}
for line in clustered_data:
    hashtags = []
    # Ensures that title and SSE line are ignored.
    if line.split()[0].isdigit():
        cluster_id = line.split()[0]
        stripped_line = line[3:-2]
        tweet_ids = stripped_line.split(",")
        for t_id in tweet_ids:
            hashtags.append(get_tweet_hashtags(t_id.strip()))
            cluster_hashtags[cluster_id] = hashtags

    else:
        continue

# Sort the hashtags by frequency
for cluster in cluster_hashtags:
    tags = cluster_hashtags[cluster]
    sorted_hashtags = sorted(tags, key = tags.count, reverse = True)
    clusterTags = []
    for item in sorted_hashtags:
        if item != []:
            clusterTags.append(item[0])
    to_file = "Cluster "+cluster+ ": "+ str(set(itertools.islice(set([str(item) for item in clusterTags]), 10)))
    print(to_file, file = output_file)