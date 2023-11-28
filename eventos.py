class EventManager:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def unsubscribe(self, callback):
        self.subscribers.remove(callback)

    def notify(self, data=None):
        for subscriber in self.subscribers:
            subscriber(data)
