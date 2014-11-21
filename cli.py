import sys

import snake

a = snake.had()
jidlo=set()
snake.pridej_zradlo(a, jidlo)

while True:
    snake.vykresli(a,jidlo)
    if sys.version_info < (3, 0):
        s = raw_input("Zadej směr: ")
    else:
        s = input("Zadej směr: ")
    snake.pohyb(s, a,jidlo)
