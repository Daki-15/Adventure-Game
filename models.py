class Player:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.location = 'field'
        self.visited_locations = []

    def to_dict(self):
        return {
            'name': self.name,
            'items': self.items,
            'location': self.location,
            'visited_locations': self.visited_locations
        }

    @staticmethod
    def from_dict(data):
        player = Player(data['name'])
        player.items = data.get('items', [])
        player.location = data.get('location', 'field')
        player.visited_locations = data.get('visited_locations', [])
        return player
