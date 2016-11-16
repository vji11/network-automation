import time

def perform_upgrade():
    print '\nNX-OS installation in progress'

def are_you_sure(do_stuff):
    try:
        from msvcrt import getch
    except ImportError:
        def getch():
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
    print '\n\n'
    print '\n\n\tYou are about to modify switches configuration.\n\n'
    print '\t\tBefore running the program make sure you revied the devices list and the commands list\n'
    print '\n\n\t\tAre you sure you want to continue? y/n'
    while True:
        char = getch()
        if char.lower() == "y":
            print char
            do_stuff()
        else:
            print 'Program End.'
            break

def main():
    print 'Program starting...\n'
    time.sleep(1)
    are_you_sure(perform_upgrade)

if __name__ == '__main__':
    #clear_screen()
    main()