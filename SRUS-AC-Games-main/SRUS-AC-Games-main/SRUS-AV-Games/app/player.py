class Player:
    def __init__(self, UID, name):
        self._UID = UID
        self._name = name

    def get_UID(self):
        return self._UID

    def setUID(self, uniqueID):
        self._UID = uniqueID

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name


    def __str__(self):
        return f"Player({self._UID}, {self._name})"


def main():
    Player()


if __name__ == "__main__":
    player = Player("00", "Anthony")
    print(player)
    player.setUID("01")
    player.setName("Mike")
    print(player)
