class Player:
    def __init__(self, uid, name):
        self._uid = uid
        self._name = name

    def get_uid(self):
        return self._uid

    def set_uid(self, uniqueID):
        self._uid = uniqueID

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


    def __str__(self):
        return f"Player({self.get_uid()}, {self.get_name()})"


def main():
    player = Player("00", "Anthony")
    print(player)
    player.set_uid("01")
    player.set_name("Mike")
    print(player)


if __name__ == "__main__":
    main()

