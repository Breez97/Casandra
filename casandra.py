from windows import *

packs = []


def ui():
    root = Tk()
    root['bg'] = '#CCCCFF'
    root.resizable(False, False)

    packs = []
    main_window(root, packs)

    root.mainloop()


def main():
    ui()


if __name__ == '__main__':
    main()