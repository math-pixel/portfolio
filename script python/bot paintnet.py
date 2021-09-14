import time
import keyboard #pip install keyboard
import mouse# pip install mouse
from tkinter import *


#-------	action 	------
def action1(): #setup les outils
        keyboard.wait('esc')
        keyboard.send('s')#choisir loutil aguette magique
        time.sleep(0.2)
        keyboard.send('s')
        time.sleep(0.2)
        keyboard.send('s')
        time.sleep(0.2)
        keyboard.send('s')
        time.sleep(0.2)
        mouse.move(528, 87, absolute=True, duration=0.1)# choisir 30 de tolerence
        mouse.click(button='left')
        keyboard.press_and_release('alt + tab')
        mes2()

def action2():#choisir le pixel de couleur
        global X
        global Y
        mouse.wait(button='left')
        color_pos = mouse.get_position()
        X = '{0[0]}'.format(color_pos)
        Y = '{0[1]}'.format(color_pos)
        keyboard.press_and_release('alt + tab')
        mes3()
	
def action3():#supprimer les couleur dans les calques
        keyboard.press_and_release('alt + 1')
        while True:       
                mouse.move(X,Y , absolute=True, duration=0.2)
                mouse.click(button='left')
                keyboard.send('suppr')
                keyboard.press_and_release('ctrl + tab')
                if keyboard.is_pressed('space'):
                        break
        print('finish')


#------	message	--------
def mes1():
        print('etre sur la fenetre de paint.net et appuyer sur echape')
        print('~~ pour importer des image choisir fichier-ouvrir et selectionner toute les image ~~')
        action1()

def mes2():
	print(' \nmaintenaant selectioner un pixel de couleur a enlever\ncommun sur toute les frame \n(il est preferable de choisir un coin)\n')
	i = 5
	while i > 0:
		print('retour dans ' + str(i) + 'sec')
		time.sleep(1)
		i = i-1
	keyboard.press_and_release('alt + tab')
	action2()

def mes3():
        print("\n			ATTENTION\n! NE CHANGER PAS DE FENETRE PENDANT LEXXECUTION DE CETTE DERNIERE TACHE !\n\n 	modifier la tolerence si besoin et appuyer sur ECHAP pour lancer la tache \n\npour ARRETER le script resté appuyer sur ESPACE")
        keyboard.wait('esc')
        action3()

#----------- appel de fonction  ----------
mes1()
#action2()
#mes3()

