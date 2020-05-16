from datastructures.gui.gui_helper import Square

if __name__ == '__main__':
    square = Square(-100, 20)
    for i in range(0, 2):
        square.add_data()
    square.plot()
