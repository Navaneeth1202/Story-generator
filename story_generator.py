import random

places = ["Mumbai", "Valeria", "The Crimson Coast", "Rajpur", "Forest of Whispers", "Neo-Terra"]

def get_names_from_user():
    num = int(input("Enter the number of characters in your story: "))
    names = []
    for i in range(num):
        name = input(f"Enter name for character {i + 1}: ")
        names.append(name)
    return names

def romcom_structure(prompt, boy, girl, location):
    return [
        f"{boy} and {girl} had been best friends in {location}, their bond growing stronger over the years.",
        f"{boy} often thought about the moment he would finally tell {girl} how he felt. {prompt}",
        f"He replayed conversations in his mind, wondering if she had ever felt the same.",
        f"But fear of losing her friendship always held him back.",
        f"One evening, she mentioned she might be leaving town soon, and his heart sank.",
        f"He couldn’t let her go without telling her the truth.",
        f"He invited her to meet him at their favorite spot in the park.",
        f"While the stars twinkled above them, he took a deep breath.",
        f"'There’s something I need to say,' he said, voice trembling.",
        f"{girl} turned to him, curiosity in her eyes.",
        f"'I’ve been in love with you for a long time,' he confessed.",
        f"There was silence — and then she smiled. 'I hoped you’d say that.'",
        f"From that night on, their story changed forever.",
        f"The friendship that once defined them now bloomed into love.",
        f"They promised to always cherish the memories that brought them here.",
    ]

def thriller_structure(prompt, characters, location):
    protagonist = characters[0]
    partner = characters[1] if len(characters) > 1 else "an ally"
    return [
        f"{location} seemed like an ordinary town — until {prompt}",
        f"{protagonist}, a determined journalist, couldn’t ignore the strange events happening around him.",
        f"A trail of disappearances pointed to something sinister.",
        f"He reached out to {partner}, a private investigator with a shadowy past.",
        f"Together, they started to uncover disturbing truths hidden for decades.",
        f"Their clues led them to a forgotten asylum deep in the woods.",
        f"The walls whispered stories of suffering and cover-ups.",
        f"A hooded figure began stalking their every move.",
        f"{protagonist} found a journal filled with cryptic symbols and names.",
        f"A message in red ink read: '{prompt}' — was it a warning or a clue?",
        f"One night, they broke into the asylum basement.",
        f"The floorboards creaked under their feet as fear tightened its grip.",
        f"Suddenly, they weren’t alone. Someone was watching them.",
        f"A struggle broke out. In the chaos, {protagonist} found a camera with footage.",
        f"The truth was darker than either of them had imagined.",
    ]

def expand_story(initial_story, target_length, prompt):
    story = initial_story.copy()
    used_lines = set()

    while len(story) < target_length:
        last_line = story[-1]
        next_line = generate_continuation(last_line, prompt, used_lines)
        story.append(next_line)
    return story

def generate_continuation(previous_line, prompt, used_lines):
    generic_lines = [
        "They held their breath, waiting for what would happen next.",
        "Every second felt like a lifetime, but they pressed on.",
        "What started as a simple moment was turning into a turning point.",
        "They thought they were ready, but the journey was just beginning.",
        "Whispers from the past seemed to echo their every move.",
        "The decision they made would change everything.",
        "They questioned everything they thought they knew.",
        "What came next was something they never expected.",
        f"The events unfolding reminded them of the situation: {prompt.lower()}",
        "And through it all, they never gave up hope.",
        "A sudden silence fell over the place — too quiet to be normal.",
        "Each heartbeat echoed louder than the last.",
        "The weight of the truth began to settle on their shoulders.",
        "Nothing about this moment felt like coincidence.",
        "Their instincts screamed that something wasn’t right.",
        "They could almost hear the ticking of fate closing in.",
        "It wasn’t just fear they felt — it was responsibility.",
        "Some questions don’t have answers, only consequences.",
        "Every shadow seemed to whisper secrets meant to be forgotten.",
        "Time felt suspended as they stepped into the unknown."
    ]

    unused_lines = [line for line in generic_lines if line not in used_lines]

    if unused_lines:
        next_line = random.choice(unused_lines)
        used_lines.add(next_line)
        return next_line
    else:
        # All lines used — return a slightly modified version to keep variety
        base = random.choice(generic_lines)
        variations = [
            base.replace("They", "The two of them"),
            base.replace("They", "Both of them"),
            base + " Still, they moved forward.",
            "And then it happened — " + base.lower(),
            "Everything changed when " + base.lower()
        ]
        return random.choice(variations)

def generate_story(user_prompt, genre_choice, target_lines, user_names):
    story_title = random.choice([
        "The Heart's Whisper", "Shattered Silence", "Beneath the Surface", "Echoes of the Past", "Chasing Fate"
    ])

    location = random.choice(places)

    if genre_choice == 1:
        if len(user_names) < 2:
            return "❌ Rom-Com needs at least 2 characters (e.g., boy and girl)."
        boy, girl = user_names[0], user_names[1]
        base_story = romcom_structure(user_prompt, boy, girl, location)
        genre_label = "Rom-Com"
    elif genre_choice == 2:
        base_story = thriller_structure(user_prompt, user_names, location)
        genre_label = "Thriller"
    else:
        return "❌ Invalid choice. Please choose a valid genre number."

    final_story = expand_story(base_story, target_lines, user_prompt)
    return f"{genre_label} Story: {story_title}\n\n" + "\n".join(final_story)

# ==== MAIN LOGIC ====
user_input = input("Enter your story idea or situation: ")
genre_num = int(input("Choose genre (1 = Rom-Com, 2 = Thriller): "))
desired_lines = int(input("How many lines should the story have? "))
user_names = get_names_from_user()

story_result = generate_story(user_input, genre_num, desired_lines, user_names)
print("\n" + story_result)
