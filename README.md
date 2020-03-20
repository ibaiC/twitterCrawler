# TwitterCrawler
A Twitter crawler developed for Web Science course at the University of Glasgow.

## Instructions
1) Run twitter_crawler.py for an hour (sample twitter.json file is provided to work with)
2) Run initialise_seeds.py
3) Remove last comma of initialSeeds.txt file 
4) Run kmeans.py with the following syntax: `py kmeans.py <n. of clusters> initialSeeds.txt tweets.json`
5) Run analysis.py for hashtags analysis
6) See output folder for all the generated graphs, clutsered tweets and hashtag analysis.

Note: The tweets.json file is only a subset of the data used throughout the development of the assignment. The data collected throughout an hour with the crawler script amounted to approximately 100,000 tweets which made the file too big to share on github with the limited wifi connection I have at home at the moment. For this reason, the sample data provided consists only of 2100 tweets.
