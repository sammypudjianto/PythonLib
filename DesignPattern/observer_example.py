"""
Example problem from http://34.212.143.74/s201911/pycon2019/docs/design_patterns.html#_what_is_a_pattern
Write a class called Twitter that inherits from the Observable and Observer classes
so that it effectively behaves simultaneously as a publisher and as a subscriber.
"""
from observer import Observer, Publisher


class Twitter(Observer, Publisher):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def follow(self, other):
        other.add_observer(self)
        return self

    def tweet(self, msg):
        self.notify_observer(msg)

    def update(self, publisher, *args, **kwargs):
        print(f'{self} received a tweet from {publisher}:', *args)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    a = Twitter('Alice')
    k = Twitter('King')
    q = Twitter('Queen')
    h = Twitter('Mad Hatter')
    c = Twitter('Cheshire Cat')

    a.follow(c).follow(h).follow(q)
    k.follow(q)
    q.follow(q).follow(h)
    h.follow(a).follow(q).follow(c)

    print(f'==== {q.name} tweets ====')
    q.tweet('Off with their heads!')
    print(f'\n==== {a.name} tweets ====')
    a.tweet('What a strange world we live in.')
    print(f'\n==== {k.name} tweets ====')
    k.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
    print(f'\n==== {c.name} tweets ====')
    c.tweet("We're all mad here.")
    print(f'\n==== {h.name} tweets ====')
    h.tweet('Why is a raven like a writing-desk?')
