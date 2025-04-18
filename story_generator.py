import random

# Character and setting pools for variety
places = ["Mumbai", "Valeria", "The Crimson Coast", "Rajpur", "Forest of Whispers", "Neo-Terra"]

def romcom_structure(boy, girl, num_lines):
    location = random.choice(places)
    
    # Creating a base story structure
    story = [
        f"{boy} had always known {girl} as his best friend since their childhood days in {location}.",
        f"As they grew up, something inside {boy} started to change whenever he looked at her.",
        f"He would notice the way her eyes lit up while talking about her dreams.",
        f"But expressing love wasn’t as easy as laughing over jokes like they used to.",
        f"{boy} feared that telling her might risk the bond they shared so dearly.",
        f"One day, {girl} mentioned she might move to another city for work.",
        f"That night, {boy} couldn’t sleep, thinking about a life without her nearby.",
        f"He decided to do something he’d never dared to before.",
        f"The next day, he invited her to their favorite spot and confessed his feelings.",
        f"She smiled and said, 'I was waiting for you to say that, dummy.'"
    ]
    
    # If the requested number of lines is greater than the base, continue the story with unique content
    while len(story) < num_lines:
        # We add new lines based on the context of the story, ensuring it doesn't repeat
        story.append(f"{boy} and {girl} spent the following days growing even closer, sharing their dreams and fears.")
        story.append(f"The more {boy} thought about her, the more he realized that this was the kind of love he'd always wanted.")
        story.append(f"One evening, {boy} surprised {girl} with a dinner at their favorite place, sparking a new chapter in their relationship.")
        story.append(f"Their bond had deepened, and the laughter between them felt even more special now.")
        story.append(f"With each passing day, they realized their love was something that could weather any storm.")
    
    return story[:num_lines]

def thriller_structure(protagonist, partner, num_lines):
    location = random.choice(places)
    
    # Creating a base story structure
    story = [
        f"The quiet town of {location} hadn’t seen crime in decades.",
        f"One foggy night, a scream echoed through the empty streets.",
        f"{protagonist}, a freelance journalist, found a trail of blood leading to a closed-off alley.",
        f"The police dismissed it as a prank, but {protagonist} knew better.",
        f"He teamed up with {partner}, an old friend turned detective, to investigate.",
        f"Together, they followed scattered clues, each pointing to a series of disappearances.",
        f"Newspapers had avoided covering it, scared of the consequences.",
        f"{protagonist} and {partner} traced evidence to an abandoned asylum.",
        f"Inside, they found names etched on the walls—names of the missing.",
        f"Suddenly, a door slammed behind them. Someone else was there."
    ]
    
    # If the requested number of lines is greater than the base, continue the story with unique content
    while len(story) < num_lines:
        # We add new lines based on the context of the story, ensuring it doesn't repeat
        story.append(f"With the evidence in hand, {protagonist} and {partner} knew they were in too deep.")
        story.append(f"The town had a dark secret, and they were about to uncover it all.")
        story.append(f"As the investigation grew more dangerous, {protagonist} started getting cryptic messages.")
        story.append(f"They discovered a hidden room beneath the asylum, filled with photographs of the missing.")
        story.append(f"In the midst of their discovery, they were ambushed, barely escaping with their lives.")
    
    return story[:num_lines]

def generate_story(boy, girl, genre_choice, num_lines):
    story_title = random.choice([ 
        "Unspoken Moments", "Twist of Fate", "Echoes of the Heart", "Shadows of Truth", "Lost in Time"
    ])

    genre_functions = {
        1: romcom_structure,
        2: thriller_structure,
    }

    genre_labels = {
        1: "Rom-Com",
        2: "Thriller",
    }

    if genre_choice not in genre_functions:
        return "❌ Invalid choice. Choose a number from the list."

    story_func = genre_functions[genre_choice]
    story = story_func(boy, girl, num_lines)
    return f"{genre_labels[genre_choice]} Story: {story_title}\n\n" + "\n".join(story)

# Main Program
print("🎬 Welcome to the Smart Story Generator!")
print("Choose a Genre:")
print("1. Rom-Com")
print("2. Thriller")

# Get user input for genre, names, and story length
genre_num = int(input("Enter your genre choice (1 for Rom-Com, 2 for Thriller): "))
boy_name = input("Enter the boy's name: ")
girl_name = input("Enter the girl's name: ")
num_lines = int(input("How many lines do you want in the story? (e.g., 10, 20, 30, etc.): "))

story_result = generate_story(boy_name, girl_name, genre_num, num_lines)
print("\n" + story_result)