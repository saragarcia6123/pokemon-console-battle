from pythonclimenu import menu

STARTERS = ["BULBASAUR", "CHARMANDER", "SQUIRTLE"]

starter = menu(
    title=["CHOOSE YOUR STARTER:"],
    options=STARTERS,
    cursor_color=(255, 0, 0),
    title_color=[(255, 255, 0)],
)
