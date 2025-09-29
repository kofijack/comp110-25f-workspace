# """Practice with bolleans and conditionals"""
# Write a function called check_first_letter that takes a input two strs: word and letter
# It should return “match!” if the first character of word is letter
# Otherwise, it should return “no match!”


def check_first_letter(word: str, letter: str) -> str:
    """Check if the first cahrecter in word == letter."""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="hello", letter="h"))

# Write a function called get_weather_report that takes weather: str as input
# and returns a str
# ● If weather is "rainy" or "cold", it should print "Bring a jacket!"
# If weather is "hot", it should print "Keep cool out there!"
# ● Otherwise, it should print "I don't recognize this weather."
# ● return the weather variable
# ● Call it with the input “cold” to see what you get!
# Now, use the input function to ask the user “What is the weather?” and pass
# hat as the argument to get_weather_report


def get_weather_report(weather: str) -> str:
    """Helpful tool for weather"""
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


print(get_weather_report(weather="cold"))
get_weather_report(weather=input("What is the weather?"))
