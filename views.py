from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__)

# Dictionary to store player data
players = {}

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
    players[player_name] = player
    return redirect(url_for('play', player_name=player_name))

@app.route('/play/<player_name>', methods=['GET', 'POST'])
def play(player_name):
    player = players.get(player_name)
    if not player:
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

    del players[player['name']]
    return render_template('end.html', message=message, css_file='house_styles.css')