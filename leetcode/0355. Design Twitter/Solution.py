# https://leetcode.com/problems/design-twitter/

from typing import List
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.followed_users = defaultdict(set) # userId: (followeeId)
        self.tweets = defaultdict(list) # userId: [tweetId]
        
        self.tweet_count = 1
        self.tweet_order = dict() # tweetId: tweet_count

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(tweetId)
        
        self.tweet_order[tweetId] = self.tweet_count
        self.tweet_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followed_users[userId].add(userId)
        
        tweets = []
        for f in self.followed_users[userId]:
            tweets += self.tweets[f]
        
        return sorted(tweets, key=lambda x: -self.tweet_order[x])[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed_users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed_users[followerId]:
            self.followed_users[followerId].remove(followeeId)

twitter = Twitter()
twitter.postTweet(1, 5)
assert twitter.getNewsFeed(1) == [5]
twitter.follow(1, 2)
twitter.postTweet(2, 6)
assert twitter.getNewsFeed(1) == [6, 5]
twitter.unfollow(1, 2)
assert twitter.getNewsFeed(1) == [5]
