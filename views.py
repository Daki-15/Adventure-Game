from flask import Flask, request, render_template, redirect, url_for, jsonify
from pymongo import MongoClient
import os

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
    player = {
        'name': player_name,
        'items': [],
        'location': 'field'
    }
    print(f"Inserting player: {player}")  # Debugging log
    players_collection.insert_one(player)
    return redirect(url_for('play', player_name=player_name))

@app.route('/play/<player_name>', methods=['GET', 'POST'])
def play(player_name):
    player = players_collection.find_one({'name': player_name})
    if not player:
        print(f"Player not found: {player_name}")  # Debugging log
        return jsonify({"error": "Player not found"}), 404

    if request.method == 'POST':
        action = request.form.get('action')
        if player['location'] == 'field':
            if action == '1':
                return house(player)
            elif action == '2':
                return cave(player)
            else:
                return jsonify({"message": "Invalid action"}), 400

    return render_template('play.html', player=player, css_file='index.css')

def cave(player):
    if 'sword' in player['items']:
        message = "You've been here before, and gotten all the good stuff. It's just an empty cave now."
    else:
        message = ("It turns out to be only a very small cave. "
                   "Your eye catches a glint of metal behind a rock. "
                   "You have found the magical Sword of Ogoroth! "
                   "You discard your silly old dagger and take the sword with you.")
        player['items'].append('sword')

    player['location'] = 'field'
    players_collection.update_one({'name': player['name']}, {"$set": player})
    return render_template('play.html', player=player, message=message, css_file='cave_styles.css')

def house(player):
    message = ("You approach the door of the house. "
               "You are about to knock when the door opens and out steps a fairie. "
               "Eep! This is the wicked fairie! "
               "The fairie attacks you!")
    if 'sword' in player['items']:
        message += (" As the fairie moves to attack, you unsheath your new sword. "
                    "The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack. "
                    "But the fairie takes one look at your shiny new toy and runs away! "
                    "You have rid the town of the fairie. You are victorious!")
    else:
        message += (" You feel a bit under-prepared for this, having only a tiny dagger. "
                    "You do your best... but your dagger is no match for the fairie. "
                    "You have been defeated!")

    return render_template('end.html', message=message, css_file='house_styles.css')
