# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy (this is a line that shows your character asset you want to display.)

    # These display lines of dialogue.

    n "You sink the knife into the red-haired girl's ribs. She screams for a split second, but it's cut off abruptly as she passes out."

    n "Wake up."

define m = Character("Kang Eunji")
show eunji normal

m "Shit... That was a dream?! It was too realistic."
    # This ends the game.

return
