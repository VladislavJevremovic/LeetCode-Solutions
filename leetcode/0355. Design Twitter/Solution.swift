// https://leetcode.com/problems/design-twitter/

class Twitter {

    private struct Following: Hashable {
        let followerId: Int
        let followeeId: Int
    }

    private struct Tweet {
        let index: Int
        let userId: Int
        let tweetId: Int
    }

    private let feedMaxLength = 10

    private var followingSet = Set<Following>()

    private var tweets = Array<Tweet>()
    private var tweetCounter = Int(0)

    init() {}

    func postTweet(_ userId: Int, _ tweetId: Int) {
        tweets.append(Tweet(index: tweetCounter, userId: userId, tweetId: tweetId))
        tweetCounter += 1
    }

    func getNewsFeed(_ userId: Int) -> [Int] {
        let feedIds = [userId] + followingSet.filter { $0.followerId == userId }.map { $0.followeeId }
        let allTweetIds = tweets.filter { feedIds.contains($0.userId) }.sorted { $0.index > $1.index }.map { $0.tweetId }
        let returnCount = allTweetIds.count > feedMaxLength ? feedMaxLength : allTweetIds.count

        return returnCount < 1 ? [] : Array(allTweetIds[0..<returnCount])
    }

    func follow(_ followerId: Int, _ followeeId: Int) {
        followingSet.insert(Following(followerId: followerId, followeeId: followeeId))
    }

    func unfollow(_ followerId: Int, _ followeeId: Int) {
        followingSet.remove(Following(followerId: followerId, followeeId: followeeId))
    }
}