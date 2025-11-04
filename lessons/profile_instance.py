"""Instantiate the profile calss."""

from lessons.profile import Profile

# create new variale user1 with username "110_rulz"
user1: Profile = Profile("110_rulez")
# update private atttribute to false
user1.private = False
# call the tweet method
user1.tweet("OOP is cool")
