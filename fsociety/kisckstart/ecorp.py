# ----------------------
# This script intend to
# go over Mr.Robot garage
# No fancy stuff.
# -----------------------
hackers = ['Mr.Robot', 'Mohd Elias', 'Elliot', 'Darlene']


def welcome_fellas():
    print(hackers)


def add_me_in():
    hackers.append('V3NKAT')


if __name__ == '__main__':
    add_me_in()
    print('------------ Welcome fellas-----------')
    welcome_fellas()