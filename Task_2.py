from datetime import datetime

class Post:
    def __init__(self, post_id, content, date, likes):
        self.post_id = post_id
        self.text = content
        self.timestamp = date
        self.likes = likes
        self.next_post = None
        self.prev_post = None

    def __repr__(self):
        return f"Post(id={self.post_id}, date={self.timestamp.strftime('%Y-%m-%d')}, likes={self.likes})"


class PostCollection:
    def __init__(self):
        self.first = None
        self.last = None
        self.current_post = None

    def add(self, post):
        if not self.first:
            self.first = self.last = self.current_post = post
        else:
            self.last.next_post = post
            post.prev_post = self.last
            self.last = post

    def delete(self, post_id):
        node = self.first
        while node:
            if node.post_id == post_id:
                if node.prev_post:
                    node.prev_post.next_post = node.next_post
                else:
                    self.first = node.next_post

                if node.next_post:
                    node.next_post.prev_post = node.prev_post
                else:
                    self.last = node.prev_post

                if self.current_post == node:
                    self.current_post = node.next_post or node.prev_post
                return True
            node = node.next_post
        return False

    def sort_by(self, attribute="timestamp", descending=False):
        posts = []
        node = self.first
        while node:
            posts.append(node)
            node = node.next_post

        if attribute == "timestamp":
            posts.sort(key=lambda p: p.timestamp, reverse=descending)
        elif attribute == "likes":
            posts.sort(key=lambda p: p.likes, reverse=descending)

        for i, post in enumerate(posts):
            post.prev_post = posts[i - 1] if i > 0 else None
            post.next_post = posts[i + 1] if i < len(posts) - 1 else None

        self.first = posts[0] if posts else None
        self.last = posts[-1] if posts else None
        self.current_post = self.first

    def go_next(self):
        if self.current_post and self.current_post.next_post:
            self.current_post = self.current_post.next_post
        return self.current_post

    def go_prev(self):
        if self.current_post and self.current_post.prev_post:
            self.current_post = self.current_post.prev_post
        return self.current_post

    def show_all(self):
        print("Post list:")
        node = self.first
        while node:
            print(node)
            node = node.next_post


if __name__ == "__main__":
    feed = PostCollection()

    feed.add(Post(1, "Hello everyone", datetime(2024, 5, 1), 12))
    feed.add(Post(2, "New Python tutorial", datetime(2024, 5, 3), 34))
    feed.add(Post(3, "Holiday in Spain", datetime(2024, 4, 28), 22))

    print("\nPosts added")
    feed.show_all()

    print("\nSorted by likes descending")
    feed.sort_by(attribute="likes", descending=True)
    feed.show_all()

    print("\nNavigation")
    print("Current:", feed.current_post)
    print("Next:", feed.go_next())
    print("Next:", feed.go_next())
    print("Previous:", feed.go_prev())

    print("\nRemoving post 2")
    feed.delete(2)
    feed.show_all()
