class Weather:
    def __init__(self, data):
        self.temperature = data.get('temperature')
        self.humidity = data.get('humidity')
        self.description = data.get('description')

    def to_dict(self):
        return {
            'temperature': self.temperature,
            'humidity': self.humidity,
            'description': self.description
        }