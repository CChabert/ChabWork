Hacker-News-data

Analysis of a dataset of submissions to Hacker News from 2006 to 2015

Hacker News is a site where users can submit articles from across the internet (usually about technology and startups), and others can "upvote" the articles, signifying that they like them. 
The more upvotes a submission gets, the more popular it was in the community. Popular articles get to the "front page" of Hacker News, where they're more likely to be seen by others.

Dataset compiled by Arnaud Drizard using the Hacker News API
10000 rows has been sampled from the data randomly, and all extraneous columns and wrote scripts to answer some main questions have been removed :

submission_time -- when the story was submitted.
upvotes -- number of upvotes the submission got.
url -- the base domain of the submission.
headline -- the headline of the submission. Users can edit this, and it doesn't have to match the headline of the original article.

Main questions:

What words appear most often in the headlines?
What domains were submitted most often to Hacker News?
At what times are the most articles submitted?
