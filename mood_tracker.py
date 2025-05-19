#Import resources to use that are not used often - like methods
import json
from datetime import datetime
import os

#Create the mood tracking file
DATE_FILE = "mood_tracker.json"

#If it exists, don't, else make the structure for the list
if not os.path.exists(DATE_FILE):
    with open(DATE_FILE, "w") as f:
        json.dump([], f)

#Get today's date
today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Get user's mood
mood = input("How are you feeling today?")

#Add today's mood to memory
entry = {
    "date": today,
    "mood": mood
}

#Load all moods
with open(DATE_FILE, "r") as f:
    mood_list = json.load(f)

#Add today's mood to mood list
mood_list.append(entry)

#Store the mood list back into the json file
with open(DATE_FILE, "w") as f:
    json.dump(mood_list, f, indent=4)

#Time to give feedback
def respond_to_mood(feeling):
    feeling = feeling.lower()
#if feeling == "feeling: that works too :)
    if "happy" in feeling:
        return "Awesome that you are happy, great!"
    elif "sad" in feeling:
        return "Boohoo, write it out in your journal dude!"
    elif "fine" in feeling:
        return "Just vibin'? Respect. Sometimes fine is just enough."
    elif "apathetic" in feeling:
        return "I will give you something to feel. Look at this code"
    elif "excited" in feeling:
        return "Sunshine mode: ACTIVATED."
    elif "confident" in feeling:
        return "You’re the main character and this is your training montage."
    elif "anxious" in feeling:
        return "Let’s overthink together. I brought snacks and spiral thoughts."
    elif "tired" in feeling:
        return "Life’s hard. Take a break. Eat something beige."
    elif "amazing" in feeling:
        return "This is chef’s kiss level mood. Send some of that energy my way!"
    elif "cool" in feeling:
        return "Cool vibes only — you’re basically emotional air conditioning."
    elif "giddy" in feeling:
        return "Certified Silly Goose hours. Honk honk."
    elif "annoyed" in feeling:
        return "Annoyance levels at ‘side-eye and walk away.’ Proceed with caution."
    elif "embarrassed" in feeling:
        return "Don’t worry, no one saw… except your ancestors. And me."
    elif "alone" in feeling:
        return "I’m here. Even if I’m not real. But like... I’m still HERE."
    elif "hungry" in feeling:
        return "Hangry mode: initiated. Proceed with snacks or regret."
    elif "proud" in feeling:
        return "You did that. I saw it. Gold star, forehead kiss, full applause."
    elif "smart" in feeling:
        return "Big brain energy detected. You deserve a Nobel and a nap."
    elif "inspired" in feeling:
        return "Energy is high. Time to act before overthinking catches up!"
    elif "in love" in feeling:
        return "Love has entered the chat — and possibly broken the firewall."
    elif "bored" in feeling:
        return "Boredom: the itch you can’t scratch with productivity."
    elif "splendid" in feeling:
        return "You’re basically royalty in a whatever you are wearing... right now."
    elif "energized" in feeling:
        return "Pump the brakes, we're goin', movin', thrivin'!"
    elif "hidden feeling" in feeling:
        return "Whoa, a secret feeling appeared. This one's rare and powerful. (1)"
    else:
        return "alright dude, add this to the list of feelings 'cause idk what to say"

print(respond_to_mood(mood))