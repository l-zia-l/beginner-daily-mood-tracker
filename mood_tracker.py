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
    elif "apathetic" in feeling:
        return "I will give you something to feel. Look at this code"
    elif "excited" in feeling:
        return "Do share, as sharing is caring"
    else:
        return "alright dude, add this to the list of feelings 'cause idk what to say"

print(respond_to_mood(mood))