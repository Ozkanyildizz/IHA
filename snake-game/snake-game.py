import turtle, random, time, os

# Global değişkenler
liste = []
engeller = []
skor = 0
maxSkor = 0
seviye = 1
hiz = 0.1
oyun_basladi = False

# Skor dosyasını oku/yükle
skor_dosyasi = "skor_kaydi.txt"
if os.path.exists(skor_dosyasi):
    with open(skor_dosyasi, "r") as f:
        try:
            maxSkor = int(f.read())
        except:
            maxSkor = 0

# Ekran ayarı
w = turtle.Screen()
w.title("Yılan Oyunu")
w.setup(600,600)
#w.bgcolor("#FDF6E3")
w.bgcolor("#000000")
w.tracer(0)

# Başlangıç mesajı
baslangic_mesaj = turtle.Turtle()
baslangic_mesaj.hideturtle()
baslangic_mesaj.color("white")
baslangic_mesaj.penup()
baslangic_mesaj.goto(0, 0)
baslangic_mesaj.write("YILAN OYUNU\n\nBaşlamak için SPACE tuşuna bas", align="center", font=("Arial", 16, "bold"))

def oyunu_baslat():
    global oyun_basladi
    if not oyun_basladi:
        oyun_basladi = True
        baslangic_mesaj.clear()

# Yılan kafası
yln = turtle.Turtle()
yln.speed(0)
yln.shape("square")
#yln.color("#2E8B57")
yln.color("#FFFFFF")
yln.penup()
yln.goto(0,0)
yln.yon = "dur"

# Yem
yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("#009B46")
yem.penup()
yem.goto(0,100)

# Yön fonksiyonları
def hareket():
    if yln.yon == "ust":
        yln.sety(yln.ycor() + 20)
    if yln.yon == "alt":
        yln.sety(yln.ycor() - 20)
    if yln.yon == "sag":
        yln.setx(yln.xcor() + 20)
    if yln.yon == "sol":
        yln.setx(yln.xcor() - 20)

def yukariGit():
    if yln.yon != "alt":
        yln.yon = "ust"
def asagiGit():
    if yln.yon != "ust":
        yln.yon = "alt"
def sagaGit():
    if yln.yon != "sol":
        yln.yon = "sag"
def solaGit():
    if yln.yon != "sag":
        yln.yon = "sol"

w.listen()
w.onkeypress(yukariGit, "Up")
w.onkeypress(asagiGit, "Down")
w.onkeypress(sagaGit, "Right")
w.onkeypress(solaGit, "Left")
w.onkeypress(oyunu_baslat, "space")

# Engel ekleme fonksiyonu
def engelEkle(adet):
    for _ in range(adet):
        while True:
            x = random.randint(-14, 14) * 20
            y = random.randint(-14, 14) * 20
            if yem.distance(x, y) > 40 and yln.distance(x, y) > 40:
                engel = turtle.Turtle()
                engel.speed(0)
                engel.shape("square")
                engel.color("#FF0000")
                engel.penup()
                engel.goto(x, y)
                engeller.append(engel)
                break

# Yem yeme ve kuyruk ekleme
def ye():
    global skor, maxSkor, seviye, hiz

    if yln.distance(yem) < 20:
        while True:
            x = random.randint(-14, 14) * 20
            y = random.randint(-14, 14) * 20
            if all(engel.distance(x, y) > 30 for engel in engeller):
                yem.goto(x, y)
                break

        kuyruk = turtle.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("square")
        #kuyruk.color("#3CB371")
        kuyruk.color("#FFFFFF")
        kuyruk.penup()
        liste.append(kuyruk)

        skor += 5
        if skor > maxSkor:
            maxSkor = skor
            with open(skor_dosyasi, "w") as f:
                f.write(str(maxSkor))

        # Seviye artışı ve engel ekleme
        if skor % 20 == 0:
            seviye += 1
            hiz = max(0.02, hiz - 0.01)
            engelEkle(1)

        w.title(f"Skor: {skor} | En yüksek: {maxSkor} | Seviye: {seviye}")

    # Kuyruğu takip ettir
    for i in range(len(liste)-1, 0, -1):
        liste[i].goto(liste[i-1].pos())
    if liste:
        liste[0].goto(yln.pos())

# Oyunu sıfırla
def baslangic():
    global skor, seviye, hiz
    time.sleep(0.5)
    yln.goto(0,0)
    yln.yon = "dur"

    for k in liste:
        k.goto(1000,1000)
    liste.clear()

    for engel in engeller:
        engel.goto(1000,1000)
    engeller.clear()

    skor = 0
    seviye = 1
    hiz = 0.1

    yem.goto(0,100)
    w.title(f"Skor: {skor} | En yüksek: {maxSkor} | Seviye: {seviye}")

# Ana oyun döngüsü
while True:
    w.update()

    if oyun_basladi:
        ye()
        hareket()

        # Duvara çarpma
        if abs(yln.xcor()) > 290 or abs(yln.ycor()) > 290: # abs mutlak değer alır 
            baslangic()

        # Kendi kuyruğuna çarpma
        for k in liste:
            if k.distance(yln) < 20:
                baslangic()

        # Engele çarpma
        for engel in engeller:
            if yln.distance(engel) < 20:
                baslangic()

        time.sleep(hiz)
