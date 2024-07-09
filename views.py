from flask import Flask, request, render_template, redirect, url_for, jsonify
from pymongo import MongoClient
from models import Player

app = Flask(__name__)

# Connect to MongoDB
try:
    client = MongoClient("mongodb://mongo:27017/")
    db = client['adventure_game']
    players_collection = db['players']
    print("Connected to MongoDB")
except Exception as e:
    print("Error connecting to MongoDB:", e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_game():
    player_name = request.form.get('name')
    player = Player(player_name)
    print(f"Inserting player: {player.to_dict()}")  # Debugging log
    players_collection.insert_one(player.to_dict())
    return redirect(url_for('play', player_name=player_name))

@app.route('/play/<player_name>', methods=['GET', 'POST'])
def play(player_name):
    player_data = players_collection.find_one({'name': player_name})
    if not player_data:
        print(f"Player not found: {player_name}")  # Debugging log
        return jsonify({"error": "Player not found"}), 404

    player = Player.from_dict(player_data)

    if request.method == 'POST':
        action = request.form.get('action')
        if action == '1' and 'house' not in player.visited_locations:
            return house(player)
        elif action == '2' and 'cave' not in player.visited_locations:
            return cave(player)
        elif action == '3' and 'forest' not in player.visited_locations:
            return forest(player)
        elif action == '4' and 'river' not in player.visited_locations:
            return river(player)
        elif action == '5' and 'mountain' not in player.visited_locations:
            return mountain(player)
        elif action == '6' and 'village' not in player.visited_locations:
            return village(player)
        elif action == '7' and 'dungeon' not in player.visited_locations:
            return dungeon(player)
        else:
            return jsonify({"message": "Invalid action or location already visited"}), 400

    # Pass player's current location to the template
    return render_template('play.html', player=player.to_dict(), current_location=player.location, css_file='index.css')

def cave(player):
    if 'sword' in player.items:
        message = "You've been here before, and gotten all the good stuff. It's just an empty cave now."
    else:
        message = ("You cautiously enter the cave, the darkness swallowing you whole. "
                   "After a few steps, you see a glint of metal. "
                   "It's the magical Sword of Ogoroth! You discard your silly old dagger and take the sword with you.")
        player.items.append('sword')
    player.visited_locations.append('cave')
    player.location = 'cave'
    players_collection.update_one({'name': player.name}, {"$set": player.to_dict()})
    return render_template('play.html', player=player.to_dict(), current_location=player.location, message=message, css_file='index.css')

def house(player):
    message = ("You approach the door of the eerie house, feeling a sense of foreboding. "
               "As you knock, the door creaks open to reveal a wicked fairie! The fairie lunges at you!")
    if 'sword' in player.items:
        message += (" You draw your Sword of Ogoroth. The fairie, seeing the gleaming sword, shrieks and flees! "
                    "You've saved the village from the wicked fairie. You are victorious!")
    else:
        message += (" Armed with only a tiny dagger, you try to defend yourself, but the fairie overpowers you. "
                    "You have been defeated!")
    player.visited_locations.append('house')
    player.location = 'house'
    players_collection.update_one({'name': player.name}, {"$set": player.to_dict()})
    return render_template('play.html', player=player.to_dict(), current_location=player.location, message=message, css_file='index.css')

def forest(player):
    if 'herb' in player.items:
        message = "You've been here before, and collected all the herbs. The forest is quiet now."
    else:
        message = ("You step into the dense forest, the trees towering above you. "
                   "As you walk deeper, you find a magical herb that heals your wounds. "
                   "You feel rejuvenated and continue your adventure.")
        player.items.append('herb')
    player.visited_locations.append('forest')
    player.location = 'forest'
    players_collection.update_one({'name': player.name}, {"$set": player.to_dict()})
    return render_template('play.html', player=player.to_dict(), current_location=player.location, message=message, css_file='index.css')

def river(player):
    if 'golden key' in player.items:
        message = "You've been here before and retrieved the golden key. The river flows peacefully."
    else:
        message = ("You arrive at a rushing river. The water is clear, and you see something shiny at the bottom. "
                   "You dive in and retrieve a golden key. It might come in handy later.")
        player.items.append('golden key')
    player.visited_locations.append('river')
    player.location = 'river'
    players_collection.update_one({'name': player.name}, {"$set": player.to_dict()})
    return render_template('play.html', player=player.to_dict(), current_location=player.location, message=message, css_file='index.css')
  
def mountain(player):
    if 'shield' in player.items:
        message = "You've been here before and taken the shield. The mountain peak is peaceful."
    else:
        message = ("You climb the steep mountain and reach the peak. The view is breathtaking. "
                   "You find an ancient shield half-buried in the ground. This will surely protect you.")
        player.items.append('shield')
    player.visited_locations.append('mountain')
    player.location = 'mountain'
    players_collection.update_one({'name': player.name}, {"$set": player.to_dict()})
    return render_template('play.html', player=player.to_dict(), current_location=player.location, message=message, css_file='index.css')

def village(player):
    if 'map' in player.items:
        message = "You've been here before and received all the help you could. The village is calm and welcoming."
    else:
        message = ("You enter a peaceful village. The villagers are friendly and offer you food and rest. "
                   "You learn valuable information about your quest and gain a map of the surrounding area.")
        player.items.append('map')
    player.visited_locations.append('village')
    player.location = 'village'
    players_collection.update_one({'name': player.name}, {"$set": player.to_dict()})
    return render_template('play.html', player=player.to_dict(), current_location=player.location, message=message, css_file='index.css')

def dungeon(player):
    if 'treasure' in player.items:
        message = "You've been here before and taken the treasure. The dungeon is now quiet."
    else:
        message = ("You enter the dark dungeon, the air thick with danger. "
                   "You encounter a fierce dragon guarding a treasure. "
                   "With your weapons and courage, you defeat the dragon and claim the treasure.")
        player.items.append('treasure')
    player.visited_locations.append('dungeon')
    player.location = 'dungeon'
    players_collection.update_one({'name': player.name}, {"$set": player.to_dict()})
    return render_template('play.html', player=player.to_dict(), current_location=player.location, message=message, css_file='index.css')
