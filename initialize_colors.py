# Initialize colors.
import curses

curses.start_color() # Must be called if the programmer wants to use colors.
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
black = curses.color_pair(1)
white = curses.color_pair(2)