class PlayerNode:
    def __init__(player, UID, key ):
        self.player = player
        self.UID = UID
        self.key = key

        key = self.UID

    def __str__(self):
        return self.player
