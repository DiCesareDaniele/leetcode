'''
https://leetcode.com/problems/design-twitter
'''

from collections import defaultdict
import heapq

N = 10

class Twitter:
    seq: int
    graph: dict[int, set[int]]
    tweet: dict[int, list[tuple[int, int]]]

    def __init__(self):
        self.seq = 0
        self.graph = defaultdict(set)
        self.tweet = defaultdict(list)

    # pylint: disable-next=invalid-name
    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.tweet[user_id].append((-self.seq, tweet_id))
        self.seq += 1

    # pylint: disable-next=invalid-name
    def getNewsFeed(self, user_id: int) -> list[int]:
        heap = []
        for tweet_id in self.tweet[user_id]:
            heapq.heappush(heap, tweet_id)
        for followee_id in self.graph[user_id]:
            for tweet_id in self.tweet[followee_id]:
                heapq.heappush(heap, tweet_id)

        feed = []
        while len(heap) > 0 and len(feed) < N:
            _, tweet_id = heapq.heappop(heap)
            feed.append(tweet_id)
        return feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.graph[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.graph[follower_id].discard(followee_id)
