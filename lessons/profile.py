"""Definition of the profile calss."""


# DEFINE
class Profile:
    username: str
    private: bool

    # constructor
    def __init__(self, username_input: str):
        self.username = username_input
        self.private = True

    # method
    def tweet(self, msg: str):
        if self.private is False:
            print(msg)


# INSTANTIATE
"""Instantiate the profile calss."""

# create new variale user1 with username "110_rulz"
user1: Profile = Profile("110_rulez")
# update private atttribute to false
user1.private = False
# call the tweet method
user1.tweet("OOP is cool")
