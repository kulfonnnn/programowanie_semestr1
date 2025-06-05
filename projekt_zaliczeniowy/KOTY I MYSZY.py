#biblioteki
from random import*
from math import sqrt, e
from matplotlib import pyplot as plt #biblioreka do wykresow
from tkinter import * #biblioteka do GUI
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #dodatek pozwalający na łączenie matplotlib z tkinterem
from matplotlib.figure import Figure #do wrzucenia wykresu do tkintera musimy go reprezentowac jako figure
#wszystkie open-source


#wczytanie plików i zamiana na inta
mouses = []
try:
    with open("mouse.txt", "r") as file:
        for linia in file:
            linia = linia.strip() #strip pozbywa sie bialych znakow, w tej sytuacji \n
            if linia.count(" ") == 1:
                linia = linia.split(" ")
                mouses.append(linia)
            else:
                pass
except FileNotFoundError:
    print("Brakuje pliku, jedno zwierze mniej na wykresie!")

for i in range(len(mouses)): #zmiana listy z str na int
    for j in range(2):
        try:
            mouses[i][j] = int(float(mouses[i][j])) #taki exception try dla zmiennoprzecinkowych xd
        except ValueError:
            mouses[i][j] = randrange(0, 101)
        if mouses[i][j] > 100 or mouses[i][j] < 0:
            mouses[i][j] = randrange(0, 101)

cats = []
try:
    with open("cat.txt", "r") as file:
        for linia in file:
            linia = linia.strip()
            if linia.count(" ") == 1:
                linia = linia.split(" ")
                cats.append(linia)
            else:
                pass
except FileNotFoundError:
    print("Brakuje pliku, jedno zwierze mniej na wykresie!")


for i in range(len(cats)): #zmiana listy z str na int
    for j in range(2):
        try:
            cats[i][j] = int(float(cats[i][j]))
        except ValueError:
            cats[i][j] = randrange(0, 101)
        if cats[i][j] > 100 or cats[i][j] < 0:
            cats[i][j] = randrange(0, 101)


kittens =[]
try:
    with open("kitten.txt", "r") as file:
        for linia in file:
            linia = linia.strip()
            if linia.count(" ") == 1:
                linia = linia.split(" ")
                kittens.append(linia)
            else:
                pass
except FileNotFoundError:
    print("Brakuje pliku, jedno zwierze mniej na wykresie!")

for i in range(len(kittens)): #zmiana listy z str na int
    for j in range(2):
        try:
            kittens[i][j] = int(float(kittens[i][j]))
        except ValueError:
            kittens[i][j] = randrange(0, 101)
        if kittens[i][j] > 100 or kittens[i][j] < 0:
            kittens[i][j] = randrange(0, 101)


lazy_cats = []
try:
    with open("lazy_cat.txt", "r") as file:
        for linia in file:
            linia = linia.strip()
            if linia.count(" ") == 1:
                linia = linia.split(" ")
                lazy_cats.append(linia)
            else:
                pass
except FileNotFoundError:
    print("Brakuje pliku, jedno zwierze mniej na wykresie!")

for i in range(len(lazy_cats)): #zmiana listy z str na int
    for j in range(2):
        try:
            lazy_cats[i][j] = int(float(lazy_cats[i][j])) #taki exception try dla zmiennoprzecinkowych xd
        except ValueError:
            lazy_cats[i][j] = randrange(0, 101)
        if lazy_cats[i][j] > 100 or lazy_cats[i][j] < 0:
            lazy_cats[i][j] = randrange(0, 101)

#tworzenie klas
class Animal: #klasa bazowa
    def __init__(self, x, y, visited, home_x, home_y): #definiujemy argumenty wejściowe
        self.x = x #atrybuty
        self.y = y
        self.visited = visited
        self.home_x = home_x
        self.home_y = home_y
    def add_to_visited(self): #funkcja, ktora dodaje aktualne wspolrzedne do listy wspolrzednych visited
        self.visited.append((self.x, self.y))
    def move(self): #definiujemy funkje jako abastrakcyjna i w dziedziczonych bedziemy ja modyfikowac
        pass
    def czy_zwierze_w_ogrodzie(self, current_x, current_y, max_x, max_y):
        while self.x > max_x or self.y > max_y or self.x < 0 or self.y < 0: #dopóki zwierze jest poza ogrodem
            self.x = current_x  #zmieniamy mu wspolrzedne na poprzednie
            self.y = current_y
            self.move() #i wykonujemy ruch


class Mouse(Animal): #klasa dziedziczona dla myszy
    def __init__(self, x, y, visited, home_x, home_y): #argumenty wejściowe
        super().__init__(x, y, visited, home_x, home_y) #super zwraca obiekt z klasy bazowej i daje dostep do jego atrybutow/metod
    def move(self):
        self.x += randrange(-1,2) #losuje ruch z -1,0,1
        self.y += randrange(-1,2)
    def teleport_home(self): #mysz wraca do norki
     #   print(f"mysz teleportuje się z {self.x}, {self.y} do {self.home_x}, {self.home_y}")
        self.x = self.home_x
        self.y = self.home_y

class Cat(Animal): #klasa dziedzona dla kota przeciętniaka
    def __init__(self, x, y, visited, home_x, home_y):
        super().__init__(x, y, visited, home_x, home_y)
    def move(self):
        self.x += randrange(-10,11) #losuje ruch od -10 do 10
        self.y += randrange(-10,11)

class Kitten(Animal): #klasa dziedziczona dla kociaka
    def __init__(self, x, y, visited, home_x, home_y):
        super().__init__(x, y, visited, home_x, home_y)
    def move(self):
        self.x += randrange(-5,6) #losuje ruch od -5 do 5
        self.y += randrange(-5,6)
    def teleport_home(self): #kociak wraca do pudełka
       # print(f"kociak teleportuje się z {self.x}, {self.y} do {self.home_x}, {self.home_y}")
        self.x = self.home_x
        self.y = self.home_y

class Lazy_cat(Animal):
    def __init__(self,x, y, visited, home_x, home_y):
        super().__init__(x, y, visited, home_x, home_y)
        self.przegonione_myszy = 0 #ilosc przegonionych myszy kazdego kota
    def move(self):
        self.x += randrange(-10, 11)  # losuje ruch od -10 do 10
        self.y += randrange(-10, 11)


#tworzenie obiektów
mouses_objects = [] #lista przechowujaca obiekt kazdej myszy
for i in range (len(mouses)): #jest tworzona dla dlugosci pliku (bo tyle jest myszy)
    mouses_objects.append(Mouse(mouses[i][0], mouses[i][1], [(mouses[i][0], mouses[i][1])],mouses[i][0], mouses[i][1])) #jako argumenty podajemy pierwsze wspolrzedne

cats_objects = []
for i in range (len(cats)):
    cats_objects.append(Cat(cats[i][0], cats[i][1], [(cats[i][0], cats[i][1])],cats[i][0], cats[i][1]))

kittens_objects = []
for i in range (len(kittens)):
    kittens_objects.append(Kitten(kittens[i][0], kittens[i][1], [(kittens[i][0], kittens[i][1])], kittens[i][0], kittens[i][1]))

lazy_cats_objects = []
for i in range (len(lazy_cats)):
    lazy_cats_objects.append(Lazy_cat(lazy_cats[i][0], lazy_cats[i][1], [(lazy_cats[i][0], lazy_cats[i][1])],lazy_cats[i][0], lazy_cats[i][1]))

#funkcje
def odleglosc(x1,y1,x2,y2): #srednia euklidesowa na odleglosc miedzy wspolrzednymi
    return sqrt((x1-x2)**2+(y1-y2)**2)

def cat_vs_mouse():
    for i in range(len(cats_objects)): #dla każego kota przeciętniaka
        for j in range(len(mouses_objects)): #sprawdzamy kazda mysz
            if odleglosc(cats_objects[i].x, cats_objects[i].y, mouses_objects[j].x, mouses_objects[j].y ) < 4: #sprawdzamy, czy mysz jest blisko kota
                mouses_objects[j].teleport_home() #jak jest, to mysz wraca do domu
                mouses_objects[j].add_to_visited()  # i zapisujemy aktualne polozenie myszy

def kitten_vs_mouse():
    for i in range(len(kittens_objects)): #dla każego kotciaka
        for j in range(len(mouses_objects)): #sprawdzamy kazda mysz
            if odleglosc(kittens_objects[i].x, kittens_objects[i].y, mouses_objects[j].x,mouses_objects[j].y) < 4:  # sprawdzamy, czy mysz jest blisko kociaka
                if odleglosc(kittens_objects[i].home_x, kittens_objects[i].home_y, kittens_objects[i].x, kittens_objects[i].y) > 50: #jezeli kociak jest dalej niz 50 od pozycji poczatkowej
                    kittens_objects[i].teleport_home()  # to kociak wraca do pudelka
                    kittens_objects[i].add_to_visited() #i zapisujemy pozycje kociaka
                else: #odleglosc kociaka od domu <=50
                    mouses_objects[j].teleport_home()#to mysz wraca do domu
                    mouses_objects[j].add_to_visited() #i zapisyjemy pozycje myszy



def lazy_cat_vs_mouse():
    for i in range(len(lazy_cats_objects)): #dla każego kota leniucha
        for j in range(len(mouses_objects)): #sprawdzamy kazda mysz
            if odleglosc(lazy_cats_objects[i].x, lazy_cats_objects[i].y, mouses_objects[j].x,mouses_objects[j].y) < 4:  # sprawdzamy, czy mysz jest blisko kociaka
                n = lazy_cats_objects[i].przegonione_myszy #przypisujemy n aktualna ilosc przegonienia myszy
                prawdo = 1/(1+e**(-0.1*n)) #liczymy prawdopodobienstwo przegonienia
                if randrange(0,101)/100 <= prawdo: #jezeli wylosowalo sie przegonienie
                    mouses_objects[j].teleport_home()#to mysz wraca do domu
                    mouses_objects[j].add_to_visited() #i zapisyjemy pozycje myszy
                    lazy_cats_objects[i].przegonione_myszy +=1 #dodajemy mysz do ilosci przegonionych


#okreslamy wymiary ogrodu
max_x = 100
max_y = 100


# glowna petla symulacji, jako funkcja zeby moc aktualizowac wykres w gui
def tworzenie_danych():

    #usuniecie poprzednich danych z visited
    for mysz in mouses_objects:
        mysz.x = mysz.home_x #jako aktualne wspolrzedne ustawiamy pozycje domu
        mysz.y = mysz.home_y
        mysz.visited.clear() #czyscimy wszystkie zapisy odwiedzonych punktow
        mysz.visited.append([mysz.home_x, mysz.home_y]) #dodajemy do odwiedzonych aktualna pozycje

    for kot in cats_objects:
        kot.x = kot.home_x
        kot.y = kot.home_y
        kot.visited.clear()
        kot.visited.append([kot.home_x, kot.home_y])

    for kociak in kittens_objects:
        kociak.x = kociak.home_x
        kociak.y = kociak.home_y
        kociak.visited.clear()
        kociak.visited.append([kociak.home_x, kociak.home_y])

    for leniuch in lazy_cats_objects:
        leniuch.x = leniuch.home_x
        leniuch.y = leniuch.home_y
        leniuch.visited.clear()
        leniuch.visited.append([leniuch.home_x, leniuch.home_y])

    # tworzymy petle syulacji 100 iteracji
    for i in range(100): #tworzymy petle syulacji 100 iteracji
        for mysz in mouses_objects: #kazda mysz wykonuje ruch (i jest on dodawany do visited)
            current_x = mysz.x #zapisanie aktualnych wspolrzednych
            current_y = mysz.y
            mysz.move()
            mysz.czy_zwierze_w_ogrodzie(current_x, current_y, max_x, max_y)
            mysz.add_to_visited()
        for kot in cats_objects: #kazdy kot wykonuje ruch
            current_x = kot.x #zapisanie aktualnych wspolrzednych
            current_y = kot.y
            kot.move()
            kot.czy_zwierze_w_ogrodzie(current_x, current_y, max_x, max_y)
            kot.add_to_visited()
        cat_vs_mouse()
        for kociak in kittens_objects: #kazdy kociak wykonuje ruch
            current_x = kociak.x #zapisanie aktualnych wspolrzednych
            current_y = kociak.y
            kociak.move()
            kociak.czy_zwierze_w_ogrodzie(current_x, current_y, max_x, max_y)
            kociak.add_to_visited()
        kitten_vs_mouse()
        for leniuchkot in lazy_cats_objects:
            current_x = leniuchkot.x #zapisanie aktualnych wspolrzednych
            current_y = leniuchkot.y
            leniuchkot.move()
            leniuchkot.czy_zwierze_w_ogrodzie(current_x, current_y, max_x, max_y)
            leniuchkot.add_to_visited()
        lazy_cat_vs_mouse()


#tworzymy wizualizacje graficzna ogrodka
#przydatne funkcje
def pozostawienie_x(lista): #z [x,y] zostaje x
    wynik = []
    for punkt in lista: #dla kazdego punktu zapisanego w liscie
        wynik.append(punkt[0]) #dodajemy jego x do wyniku
    return wynik

def pozostawienie_y(lista): #z [x,y] zostaje y
    wynik = []
    for punkt in lista:
        wynik.append(punkt[1])
    return wynik

#tworzymy gui
window = Tk() #stworzenie okna
window.geometry("1920x1080")
window.title("SPACERY W OGRODZIE")
window.config(background="black")

label = Label(window, text="SPACERY W OGRODZIE", font=("Arial", 50, "bold"), foreground="red", background="black")
label.place(x=600, y=100)



#fukcja odswiezajaca wykres (usuwa sie poprzedni, tworzy i zapisuje nowy)
def odswiez_wykres():

    osie.clear() #czysci poprzedni wykres
    # Rysowanie wykresu
    for mysz in mouses_objects:
        osie.plot(pozostawienie_x(mysz.visited), pozostawienie_y(mysz.visited), color="r") #tworzy linie dla kazdej myszy
    osie.plot([], [], color="r", label="myszy") #tworzy legende w kolorze myszy (eliminacja nadpisan)

    for kot in cats_objects:
        osie.plot(pozostawienie_x(kot.visited), pozostawienie_y(kot.visited), color="b")
    osie.plot([], [], color="b", label="koty przeciętniaki")

    for kociak in kittens_objects:
        osie.plot(pozostawienie_x(kociak.visited), pozostawienie_y(kociak.visited), color="c")
    osie.plot([], [], color="c", label="kociaki")

    for leniuch in lazy_cats_objects:
        osie.plot(pozostawienie_x(leniuch.visited), pozostawienie_y(leniuch.visited), color = "m")
    osie.plot([], [], color="m", label="koty leniuchy")

    osie.set_title("OGRÓD")
    osie.set_xlabel("X")
    osie.set_ylabel("Y")
    osie.legend(fontsize='small')

    canvas.draw()  # aktualizuje aktualny wykres

#funkcja wrzucajaca wykres do gui
def odpal_wykres():
    canvas_widget.place(x=700, y=500) #wrzucenie wykresu na okreslona pozycje okna


# Dodanie powiązań wykresu (jako figury) z GUI
wykres = Figure(figsize=(5, 5), dpi=100) #tworzy sie figura 5x5 cala (100pixeli na cal), która przechowywuje wykres i jego czesci
osie = wykres.add_subplot(111)  # dodaje osie do tej figury ("wykres") (111- 1 rzad, 1 kolumna, 1-pierwsza oś (podwykres))
#dodanie wykresu do okna
canvas = FigureCanvasTkAgg(wykres, master=window) #łączy wykres z oknem
canvas_widget = canvas.get_tk_widget()  # Pobranie widgetu z wykresem



#dodanie przyciskow do interfejsu graficznego
    #przycisk do odpalania wykresu
button_odpalanie = Button(window, text="Zobacz wydeptane ścieżki!", font=("Ink Free", 30, "bold"), activebackground="red", command=odpal_wykres)
button_odpalanie.place(x=700, y=270)

    #przycisk do ponownego generowania wykresu
def nastepny_dzien():
    tworzenie_danych()
    odswiez_wykres()
button_nastepnydzien = Button(window, text="Zobacz symulacje z następnego dnia", font=("Ink Free", 30, "bold"), activebackground="red", command=nastepny_dzien)
button_nastepnydzien.place(x=660, y=400)


    #przycisk do zamykania wykresu
def zamknij_program():
    window.destroy()
button_zamykanie = Button(window, text="Zamknij program", font=("Ink Free", 15, "bold"), activebackground="red", command=zamknij_program)
button_zamykanie.place(x=0,y=0)

nastepny_dzien() #stworzenie danych i wykresu

window.mainloop() #otworzenie okna


