import pyshorteners

# Create a Shortener object
s = pyshorteners.Shortener()

a=input()
# Shorten a URL
short_url = s.tinyurl.short(a)

# Print the shortened URL
print(short_url)