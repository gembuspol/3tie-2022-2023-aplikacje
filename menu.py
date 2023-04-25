import pygame_menu
import pygame
#import pliku z grą
import waz

def wlaczGre():
    waz.waz()
def zmienJablka(tekst,ilosc):
    print("a")
def main():
    pygame.init()
    #utworzenie okna gry i okreslenie jego rozmiarów
    oknoGry=pygame.display.set_mode((600,600),0,32)
    #ustawiamy nazwę okienka
    pygame.display.set_caption("Wąż")
    menu=pygame_menu.Menu("Gra Wąż 3TIE",600,600,theme=pygame_menu.themes.THEME_ORANGE)
    menu.add.button('Uruchom grę',wlaczGre,background_color=(0,255,0))
    menu.add.selector("Wybierz ilośc jabłek",[('jedno',1),('dwa',2),('pięć',5),('dziesięć',10),('dwadzieścia',20)],onchange=zmienJablka)
    menu.mainloop(oknoGry)
main()