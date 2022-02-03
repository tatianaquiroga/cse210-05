

class Parachute:
# create a parachute draw that for the game
    def __init__(self):
        self.wrong_guess = True
        self._draw = []
  

    def create_parachute(self):
        # create a bunch of variables that will be used to create the parachute, 
        # appending the variables to the _draw list to delete if the guess of the 
        # player is wrong  

        # Args:
        #     _draw (list): starts with a empty list

        firts_try  = " ___ "
        second_try = "/___\ "
        third_try  = "\   / "
        fourth_try = " \ / "
        head = "  O "
        chest = " /|\ "
        legs = " / \ "
        self._draw.append(firts_try)
        self._draw.append(second_try)
        self._draw.append(third_try)
        self._draw.append(fourth_try)
        self._draw.append(head)
        self._draw.append(chest)
        self._draw.append(legs)

    def draw_parachute(self):
        # iterate over the list to draw the parachute

        # Args:
        #     _draw (list): a list of strings that will be used to draw the parachute
        for i in self._draw:
            print(i)

    def delete_parachute(self):
        # delete the parachute if the guess is wrong
        # Args:
        #     _draw (list): a list of strings that will be used to draw the parachute
        if self.wrong_guess:
            self._draw.pop(0)



paracaidas = Parachute()
paracaidas.create_parachute()
paracaidas.draw_parachute()
paracaidas.delete_parachute()
print("\n")
paracaidas.draw_parachute()