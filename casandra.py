from windows import *

def ui():
    root = Tk()
    root.resizable(False, False)
    root['bg'] = '#CCCCFF'

    packs = []
    main_window(root, packs)

    root.mainloop()


def main():
    ui()


if __name__ == '__main__':
    main()