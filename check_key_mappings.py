import curses
window = curses.initscr() # Initialize the library. Returns a WindowObject which represents the whole screen.

# *******************************************************************************
# *** Kludge *** 
# *******************************************************************************
# The keyboard mappings in windows command shell are different from those in Git Bash.
# To be able to run this script in both Bash and CMD I prompt the user to hit the Page Up key
# and then overwrite the curses mappings in the event that the mapping is not what the script expects.
# This is a kludge, but it works.

def checkKeyMappingsMessage():
    window.addstr('Press the Page Up key to check the key mappings.\n')
    pageUpKeyValue = window.getch()

    if pageUpKeyValue != curses.KEY_UP:
        curses.KEY_UP = curses.KEY_A2
        curses.KEY_LEFT = curses.KEY_B1
        curses.KEY_DOWN = curses.KEY_C2
        curses.KEY_RIGHT = curses.KEY_B3
# *******************************************************************************
# *** End of the kludge ***
# *******************************************************************************
