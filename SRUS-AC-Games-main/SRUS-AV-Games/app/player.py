class Player:
    def __init__(self,UID, name):
        self.UID = UID
        self.name = name

    def __str__(self):
        return("class"+self.UID+"class"+ self.name)
        
