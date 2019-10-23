class MyStuff(object):

    def __init__(self):
        self.suit = "A 3 piece suit"
        self.jacket = "A leather jacket"

    def displayer_module(self, suit, jacket):
        print(self.suit, '\t', suit)
        print(self.jacket, '\t', jacket)

if __name__ == "__main__":
    suit = "Pinstripes"
    jacket = "Bomber Style"
    MyStuff().displayer_module(suit, jacket)
