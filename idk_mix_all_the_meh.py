import random

# Word weights based on categories
word_weights = {
    "emotion": {
        "happy": 3,
        "joyful": 3,
        "sad": -2,
        "angry": -3,
        "excited": 2,
        "neutral": 0,
    },
    "action": {
        "help": 3,
        "fight": -2,
        "talk": 1,
        "run": 1,
        "think": 2,
        "avoid": -1,
    },
    "context": {
        "quiet": 2,
        "noisy": -1,
        "dark": -1,
        "bright": 2,
        "crowded": -2,
        "peaceful": 3,
    },
    "polarity": {
        "good": 3,
        "bad": -3,
        "neutral": 0,
        "great": 4,
        "terrible": -4,
    },
}
def adjust_bias_for_context(context):
    """Adjust word weights based on context."""
    bias = {
        "peaceful": {
            "emotion": 1.2,
            "action": 1.1,
            "polarity": 1.5,
            "context": 1.3
        },
        "tense": {
            "emotion": 0.8,
            "action": 1.3,
            "polarity": 1.8,
            "context": 0.9
        },
        "neutral": {
            "emotion": 1.0,
            "action": 1.0,
            "polarity": 1.0,
            "context": 1.0
        }
    }
    
    return bias.get(context, bias["neutral"])

def calculate_sentence_score(sentence, context):
    """Calculate the total score of a sentence based on word weights and context bias."""
    bias = adjust_bias_for_context(context)
    score = 0
    
    # Tokenize sentence into words (simplified for demonstration)
    words = sentence.lower().split()
    
    for word in words:
        for category in word_weights:
            if word in word_weights[category]:
                word_weight = word_weights[category][word]
                adjusted_weight = word_weight * bias[category]  # Apply bias to weight
                score += adjusted_weight
                
    return score

def generate_dynamic_sentence(context, npc_emotion="neutral", npc_action="thinking"):
    """Generate a sentence based on context, emotion, and action."""
    # Possible components for sentence generation
    possible_subjects = ["the NPC", "the player", "a guard", "the merchant", "an adventurer"]
    possible_actions = {
        "thinking": ["is considering the situation", "is pondering the consequences", "is lost in thought"],
        "talking": ["speaks to you cautiously", "whispers to a nearby NPC", "shouts across the street"],
        "fighting": ["bravely faces the enemy", "launches into battle", "defends their position"],
        "helping": ["offers their assistance", "gives you a hand", "lends you support"]
    }
    
    # Randomly choose components
    subject = random.choice(possible_subjects)
    action = random.choice(possible_actions[npc_action])
    
    # Generate sentence based on the chosen subject, action, and context
    sentence = f"{subject} {action}."
    
    # Calculate its score (and possibly modify based on score)
    score = calculate_sentence_score(sentence, context)
    
    return sentence, score

# Example usage:
context = "peaceful"  # Can be "peaceful", "tense", or "neutral"
npc_emotion = "happy"
npc_action = "thinking"  # NPC can be thinking, talking, fighting, helping
sentence, score = generate_dynamic_sentence(context, npc_emotion, npc_action)

print(f"Generated Sentence: {sentence}")
print(f"Sentence Score: {score}")

npc_state = {
    "emotion": "neutral",
    "action": "thinking",
    "interaction_history": [],
}

def npc_thought_process():
    """Generate an internal thought for the NPC based on their state and context."""
    # Example thought generation based on past interactions and current context
    if npc_state["emotion"] == "happy":
        thought = "The day feels good, maybe I should offer help."
    elif npc_state["emotion"] == "sad":
        thought = "Everything seems off today, I should stay quiet."
    elif npc_state["action"] == "thinking":
        thought = "I need to assess the situation before taking action."
    else:
        thought = "I don't know what to do, but I’ll just keep going."
    
    return thought

def npc_interaction_history(player_action):
    """Update NPC's interaction history."""
    npc_state["interaction_history"].append(player_action)
    if len(npc_state["interaction_history"]) > 5:  # Limit history length
        npc_state["interaction_history"].pop(0)
    
    # Example emotion change based on interaction history
    if "helped" in npc_state["interaction_history"]:
        npc_state["emotion"] = "happy"
    elif "hurt" in npc_state["interaction_history"]:
        npc_state["emotion"] = "angry"
    else:
        npc_state["emotion"] = "neutral"

# Example usage of thought process
thought = npc_thought_process()
print(f"NPC Thought: {thought}")

def main():
    # Set context and NPC state
    context = "peaceful"  # Can be "peaceful", "tense", or "neutral"
    npc_emotion = "happy"
    npc_action = "helping"
    
    # Generate NPC thought
    thought = npc_thought_process()
    print(f"NPC Thought: {thought}")
    
    # Generate dynamic sentence
    sentence, score = generate_dynamic_sentence(context, npc_emotion, npc_action)
    print(f"Generated Sentence: {sentence}")
    print(f"Sentence Score: {score}")

# Run the NPC dialogue system
main()