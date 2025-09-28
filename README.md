# 🧠 Daily Mood Tracker

A beginner-friendly Python CLI project to track your daily mood. Stores entries with timestamps in a local `.json` file and gives custom responses based on your vibe. Great for journaling, self-awareness, and learning Python basics.

## 🚀 Features
- Track your mood from the terminal
- Auto-saves mood + timestamp to a JSON file
- Smart responses based on how you feel
- Keeps a growing history of all your mood entries

### Example Output
[
  {
    "date": "2025-05-15 14:33:45",
    "mood": "tired but vibin"
  }
]

## 🛠️ Tech Used
- Python 3
- JSON for local storage
- Command Line Interface (Git Bash)
- Vim for text editing

## 📦 How to Run
### Clone repository to your directory and go into the folder
```bash
git clone https://github.com/l-zia-l/beginner-daily-mood-tracker.git
cd beginner-daily-mood-tracker.git
```
### Run the Mood Tracker program
```bash
python mood_tracker.git
```

### Run mood list to add a new mood using Vim
```bash
vim mood_tracker.py      # open the file
i                        # start typing/editing
<Esc>                    # press Esc to exit insert mode
:wq                      # type to save and quit
```

## P.S
Delete the mood_tracker.json file if you do not want to see my mood logs.
## 🛑 Disclaimer

The original code for this project was created with the help of [ChatGPT](https://openai.com/chatgpt) to help me jumpstart my learning journey. I modified the comments and explored how the code works to build familiarity with Python before starting the **Cisco Python Essentials** course.

This project is **purely educational** and was designed to help me get hands-on exposure to:
- Writing and running Python scripts
- Understanding syntax and basic logic
- Learning how to work with files, dates, and functions
- Practicing good GitHub practices (commits, README, documentation)

I'm sharing this publicly to showcase my learning progress, not as an original or advanced work. 💡✨
