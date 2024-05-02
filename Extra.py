import json

# JSON data
json_data = '''
{
  "username": [
    "King Arthur",
    "Lancelot",
    "Sir Robin, the Not-Quite-So-Brave",
    "Black Knight",
    "Sir Bedivere",
    "Roger the Shrubber",
    "Brother Maynard",
    "Bridgekeeper",
    "French Soldier",
    "Knight of Ni",
    "Dead Collector",
    "Dennis",
    "King of Swamp Castle"
  ],
  "password": [
    "Run away!",
    "She turned me into a newt!",
    "That's enough singing for now",
    "None shall pass",
    "How do you know so much about swallows?",
    "Oh, what sad times are these when passing ruffians can say Ni at will to old ladies.",
    "Armaments, chapter two, verses nine through twenty-one",
    "What... is the air-speed velocity of an unladen swallow?",
    "I fart in your general direction",
    "You must cut down the mightiest tree in the forest... WITH... A HERRING!",
    "Bring out your dead!",
    "Help, I'm being oppressed",
    "Let's not bicker and argue over who killed who'"
  ]
}
'''

# Parse JSON data into a Python dictionary
data = json.loads(json_data)

# Access the values associated with the "username" and "password" keys
usernames = data["username"]
passwords = data["password"]

print("Usernames:", usernames)
print("Passwords:", passwords)
