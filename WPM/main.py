import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome! Speed Typing Test")
    stdscr.addstr(1, 0, "Press button to begin")
    stdscr.refresh()
    stdscr.getket()

def wpm_test(stdscr):
    target = "Hello world this is some test text for this app!"
    current = []

    while True:
        stdscr.clear()
        stdscr.addstr(target)


        for char in current:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getkey()

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current) > 0:
                current.pop()
            else:
                current.append(key)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)


    start_screen(stdscr)
    wpm_test(stdscr)



wrapper(main)