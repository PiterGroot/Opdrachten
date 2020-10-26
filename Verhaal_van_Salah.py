import time
import sys
import os

asciiWelcome = """\
 __    __    ___  _         __   ___   ___ ___    ___
|  |_-_| |  /  _]| |       /  ] /   \ |   |   |  /  _]
|  |  |  | /  [_ | |      /  / |     || _   _ | /  [_
|  |  |  ||    _]| |___  /  /  |  O  ||  \_/  ||    _]
|  `  '  ||   [_ |     |/   \_ |     ||   |   ||   [_
 \      / |     ||     |\     ||     ||   |   ||     |
  \_/\_/  |_____||_____| \____| \___/ |___|___||_____|
"""
def Restart():
    print("\nWil je dit programma opnieuw starten? (y / n)")
    dontclose = input()
    if dontclose in answer_Y:
        intro()
    elif dontclose in answer_N:
        sys.exit()
    else:
        print("Typ alstublieft 'y' of 'n' in.")
        time.sleep(3)
        Restart()
#speler kan A en a, B en b, C en c en Y, y, N, n antwoorden
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_Y = ["Y", "y"]
answer_N = ["N", "n"]
#correctie
required = ("\nTyp alstublieft A, B of C\n")
#KLAAR
def intro():
  os.system('cls')
  print(asciiWelcome)
  print ("\n[INTRO]\n")
  print("Dit verhaal lees je anders dan de meeste verhalen, want jij (de speler) kiest de weg. "
   "\nJij speelt hierin dus eigenlijk de hoofdrol. Lukt het jou om een goed einde te krijgen?\n")
  time.sleep(1)
  print("Wacht iedere keer voordat je je antwoord wil typen, totdat je '>>>' ziet.")
  print("Dan kan je 'A, a', 'B, b' of 'C, c' kiezen als antwoord.")
  print("Soms hoef je alleen maar op ENTER te drukken, dit hoef je alleen te doen als het bij de vraag staat.")
  time.sleep(1)
  print("\nIn dit verhaal speel je als Salah, je zit met je gezin in Saudi-Arabië, jullie worden daar behandeld als tweederangsburgers.")
  print("Je kan geen geld verdienen, wan alle banen gaan naar de Saudiërs. Je zou terug kunnen gaan naar je geboorteland" + "\n" + "Jemen, maar het risico is wel dat je gezin zal worden opgepakt.")
  print("Omdat je vrouw uit het noorden van Jemen komt en jij uit het zuiden, dat is namelijk halsmisdaad. Wat ga je doen? \n")
  time.sleep(1)
  print("A. Je gaat vluchten")
  print("B. Je gaat terug naar je huis in Jemen")
  choice = input(">>> ")
  if choice in answer_A:
    q14()
  elif choice in answer_B:
    q13()
  else:
    print (required)
    time.sleep(3)
    intro()
#KLAAR
def q2():
  os.system('cls')
  print("\nJe besluit om eerst alleen te gaan vluchten omdat je gezin nog niet meekan.")
  print("Je kan nog net een boottocht betalen van je laatste centen die via de rode zee naar Cyprus vaart.")
  print("De boot zit overvol, de mensen zitten op elkaar gepropt. Je plan is om uiteindelijk naar Turkije te gaan.")
  print("Ondertussen hoor je geruchten dat je gezocht wordt door de politie want iemand heeft jullie verlinkt")
  print("en over jullie verboden relatie vertelt. Wat ga je doen?\n")
  time.sleep(1)
  print("A. Neem een ander bootje naar Europa")
  print("B. Negeer de geruchten")
  print("C. Neem de boot naar Kroatië")
  choice = input(">>> ")
  if choice in answer_A:
      q10()
  elif choice in answer_B:
      q21()
  elif choice in answer_C:
      q4()
  else:
    print (required)
    time.sleep(3)
    q2()
#KLAAR
def q3():
  os.system('cls')
  print("\nNa lang zoeken en smeken mag je bij een vrachtwagen achterin verstoppen.")
  print("Maar op een voorwaarde dat je bepaalde drugs moet meesmokkelen. Wat ga je doen?\n")
  time.sleep(1)
  print("A. Je gaat akkoord en smokkelt wat drugs mee in je zakken die je van de chauffeur mee hebt gekregen.")
  print("B. Je gaat niet akkoord.")
  choice = input(">>> ")
  if choice in answer_A:
    q11()
  elif choice in answer_B:
    q17()
  else:
    print (required)
    time.sleep(3)
    q3()
#KLAAR
def q4():
  os.system('cls')
  print("\nHet is nu een week later en je bent net aangekomen in Kroatië tot nu toe gaat het best wel goed.")
  print("Het is alleen moeilijk om soms aan een slaaplek en eten en drinken te komen.")
  print("Je gaat naar een internetcafé met je laatste centen om te kijken of je familie je een bericht heeft gestuurd.")
  print("Als je naar de browser gaat zie je een advertentie dat je gratis mee mag met een vliegtuig naar een land in Europa.")
  print("Op vaarwaarde dat je moet meehelpen met de crew. Dit vliegtuigmaatschappij doet dit wegens tekort aan bemanning.")
  print("Als je verder wil lezen valt de computer uit, je tijd blijkt op te zijn. Je hebt geen geld meer. Wat ga je doen?\n")
  time.sleep(1)
  print("A. Je gaat verder lopend vluchten naar Europa")
  print("B. Je kiest het baantje.")
  choice = input(">>> ")
  if choice in answer_A:
    q10()
  elif choice in answer_B:
    q8()
  else:
    print (required)
    time.sleep(3)
    q4()
#KLAAR
def q5():
  os.system('cls')
  print("\nJullie zien er verdacht uit, de agenten besluiten om aan te kloppen. Als je opendoet moet je je paspoort en papieren laten zien.")
  print("Helaas ziet de agent dat jouw vrouw uit het noorden komt en jij uit het zuiden. Jullie worden opgepakt en naar de gevangenis gestuurd.\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
      end1()
  elif choice in answer_B:
      end1()
  elif choice in answer_C:
      end1()
  else:
    end1()
#KLAAR
def q6():
  os.system('cls')
  print("\nJe kiest voor zekerheid en gaat met een paar andere vluchtelingen meelopen naar Trukije.")
  print("Je bent moe, want je hebt een lange vlucht gehad. Je ziet een rustig plekje onder een boom om te gaan slapen.")
  print("Maar je kan ook doorlopen. Wat ga je doen?\n")
  time.sleep(1)
  print("A. Doorgaan")
  print("B. Slapen")
  choice = input(">>> ")
  if choice in answer_A:
    q4()
  elif choice in answer_B:
    q4()
  else:
    print (required)
    time.sleep(3)
    q6()
#KLAAR
def q7():
  os.system('cls')
  print("\nJe zorgt ervoor dat je weer een baan krijgt. Jij en je gezin proberen weer een beter leven op te bouwen.")
  print("Al moet dat wel in geheim blijven. Jullie zijn niet erg gelukkig maar het kan ook veel slechter zijn.\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    end2()
  elif choice in answer_B:
    end2()
  elif choice in answer_C:
    end2()
  else:
    end2()
#KLAAR
def q8():
  os.system('cls')
  print("\nWanneer je bij de luchthaven aanmeld, word je gelijk toegewezen naar een ene John. Goed nieuws!")
  print("Het baantje is nog vrij en je vlucht gaat al over 10 minuten. Het vliegtuig blijkt naar Nederland te gaan.")
  print("Je kent Nederland eigenlijk nauwelijks, maar je weet dat het een veilig land is.\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    q9()
  elif choice in answer_B:
    q9()
  elif choice in answer_C:
    q9()
  else:
    print (required)
    time.sleep(3)
    q8()
#KLAAR
def q9():
  os.system('cls')
  print("\nNa eindelijk aangekomen te zijn in Nederland merk je gelijk al dat de sfeer hier veel rustiger en veiliger aanvoelt.")
  print("De mensen doen aardig tegen je en je voelt je in lange tijd weer beter. Je vraagt gelijk een asiel aan, voor jezelf en voor je familie.")
  print("Dat is wel spannend want je hebt al veel geruchten gehoord dat dat maandenlang kan duren en dat veel mensen afgewezen worden.")
  print("Maar dit is je enige kans. Wat ga je doen?\n")
  time.sleep(1)
  print("A. Je gaat slapen")
  print("B. Je gaat eten")
  choice = input(">>> ")
  if choice in answer_A:
    q20()
  elif choice in answer_B:
    q16()
  else:
    print (required)
    time.sleep(3)
    q9()
#KLAAR
def q10():
  os.system('cls')
  print("\nJe hebt ondertussen al bedacht dat je naar Nederland wil gaan, ondertussen is het een maand later.")
  print("Maar als je richting Duitsland komt zie je dat bij de grenzen strenge identiteitscontroles worden uitgevoerd. Wat ga je doen?\n")
  time.sleep(1)
  print("A. Je neemt een andere route naar Nederland.")
  print("B. Je gaat er gewoon heen, als je rustig bent kan er niks misgaan.")
  choice = input(">>> ")
  if choice in answer_A:
    q9()
  elif choice in answer_B:
    q15()
  else:
    print (required)
    time.sleep(3)
    q10()
#KLAAR
def q11():
  os.system('cls')
  print("\nDe vrachtwagen gaat na een lange rit over de grens, je hebt alleen veel pech. Omdat er bij de grens allemaal politiehonden staan.")
  print("Als de vrachtwagen langs de honden rijdt, gaan ze helemaal tekeer. De honden ruiken de drugs. Jij en de chauffeur worden opgepakt. Jij word in Jemen opgesloten.\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    end1()
  elif choice in answer_B:
    end1()
  elif choice in answer_C:
    end1()
  else:
    end1()
#KLAAR
def q12():
  os.system('cls')
  print("\nJe hebt twee keuzes, ga je verstoppen in een vrachtwagen om zo de grens over te komen, waardoor je")
  print("uiteindelijk in Turkije terecht komt? Of ga je lopend met een andere groep vluchtelingen?\n")
  time.sleep(1)
  print("A. Lopend")
  print("B. Vrachtwagen")
  choice = input(">>> ")
  if choice in answer_A:
    q6()
  elif choice in answer_B:
    q3()
  else:
    print (required)
    time.sleep(3)
    q12()
#KLAAR
def q13():
  os.system('cls')
  print("\nJe besluit om met je gezin naar je huis te gaan, wat best wel een risico is. Na ploeteren door woestijn,")
  print("wrakken en meer gevaarlijke gebieden komen jullie eindelijk aan waar je huis staat. Op hetzelfde moment zien jullie politieagenten rondlopen.")
  print("De agenten spreken jullie aan, jullie weten dat het gevaarlijk is want jullie relatie is verboden. Wat ga je doen?\n")
  time.sleep(1)
  print("A. Loop snel naar jullie huis en doe net alsof jullie niks horen.")
  print("B. Naar de agenten lopen en doen alsof er niks aan de hand is.")
  choice = input(">>> ")
  if choice in answer_A:
    q5()
  elif choice in answer_B:
    q19()
  else:
    print (required)
    time.sleep(3)
    q13()
#KLAAR
def q14():
  os.system('cls')
  print("\nJe besluit met je gezin te gaan vluchten naar je geboorteland Jemen.")
  print("Na een lange tocht kom je eindelijk aan. Het land is verwoest, er heerst een burgeroorlog.")
  print("Dit is de laatste kans dat je kan vluchten, maar je kan ook de gok wagen en terug naar je huis gaan. Wat ga je doen?""" + "\n")
  time.sleep(1)
  print("A. Vluchten")
  print("B. Naar je huis")
  choice = input(">>> ")
  if choice in answer_A:
      q2()
  elif choice in answer_B:
      q13()
  else:
    print (required)
    time.sleep(3)
    q14()
#KLAAR
def q15():
  os.system('cls')
  print("\nDe agenten vragen om je kaart maar je kan geen Duits, na lang gebrekkig Engels praten komen de agenten erachter dat je een vluchteling bent.")
  print("En Duitsland heeft zijn grenzen weer net gesloten voor vluchtelingen omdat het land vol begint te raken.")
  print("Je wordt terug naar een dichtbije luchthaven gebracht. Je moet terug naar Jemen.")
  print("Als je terug in Jemen aankomt weten veel mensen al van je verboden liefde met je vrouw.\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    end1()
  elif choice in answer_B:
    end1()
  elif choice in answer_C:
    end1()
  else:
    end1()
#KLAAR
def q16():
  os.system('cls')
  print("\nNa het eten ga je naar de balie om te horen of je al post gekregen hebt.\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    end3()
  elif choice in answer_B:
    end3()
  elif choice in answer_C:
    end3()
  else:
    end3()
#KLAAR
def q17():
  os.system('cls')
  print("\nDe chauffeur is kwaad, zo kwaad dat hij je verraad en bij de politie aangeeft. Je wordt gelijk weer teruggestuurd.\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    end1()
  elif choice in answer_B:
    end1()
  elif choice in answer_C:
    end1()
  else:
    end1()
#KLAAR
def q18():
  os.system('cls')
  print("\nAls je in Griekenland aankomt besluit je om zo weinig mogelijk tijd te verliezen en snel door te gaan met vluchten.")
  print("Je weet nog niet naar welk land je wilt.\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    q10()
  elif choice in answer_B:
    q10()
  elif choice in answer_C:
    q10()
  else:
    q10()
#KLAAR
def q19():
  os.system('cls')
  print("\nJe ziet er niet verdacht uit en na een kort gesprekje lopen de agenten weer verder. Wat ga je doen?\n")
  time.sleep(1)
  print("A. Na lang overleggen besluit je toch nog te gaan vluchten voor een beter leven.")
  print("B. Blijf thuis en bouw een nieuw leven op.")
  choice = input(">>> ")
  if choice in answer_A:
    q12()
  elif choice in answer_B:
    q7()
  else:
    print (required)
    time.sleep(3)
    q19()
#KLAAR
def q20():
  os.system('cls')
  print("\nAls je de volgende morgen wakker wordt, dan ga je gelijk naar de balie van het asielzoekerscentrum en vraagt of je al post hebt.")
  print("En ja hoor je hebt wat post ontvangen. Als je het opent zie je dat je asiel hebt gekregen en je familie mag ook komen.")
  print("Zij worden zelfs met vliegtuig en al gebracht naar Nederland.\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
      end4()
  elif choice in answer_B:
      end4()
  elif choice in answer_C:
      end4()
  else:
      end4()
#KLAAR
def q21():
  os.system('cls')
  print("\nJe negeert de geruchten en stapt in de boot, 10 minuten later staat de politie voor de boot om te inspecteren.")
  print("Je bent ontdekt en je wordt gelijk meegenomen in een busje.\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    end1()
  elif choice in answer_B:
    end1()
  elif choice in answer_C:
    end1()
  else:
    end1()
#KLAAR
def end1():
  os.system('cls')
  print("\nJe / jullie worden in de gevangenis gegooid tussen andere “criminelen”. De gevangenis is zwaar bewaakt en de bewakers zijn erg streng.")
  print("De kans is klein dat je / jullie levend uit de gevangenis komen.\n\n[DOODLOPEND EINDE]\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    Restart()
  elif choice in answer_B:
    Restart()
  elif choice in answer_C:
    Restart()
  else:
    Restart()
#KLAAR
def end2():
  os.system('cls')
  print("\nUiteindelijk kunnen je kinderen ook weer naar school, maar ze kunnen niet de juiste verzorging krijgen.")
  print("Soms denk je eraan of dit wel de beste keuze was geweest om terug te gaan.\n\n[NORMAAL EINDE]\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    Restart()
  elif choice in answer_B:
    Restart()
  elif choice in answer_C:
    Restart()
  else:
    Restart()
#KLAAR
def end3():
  os.system('cls')
  print("\nJe krijgt te horen dat je helaas geen asiel blijkt te krijgen in Nederland. Je wordt weer met een vliegtuig terug naar Jemen gebracht.\n\n[SLECHT EINDE]\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    Restart()
  elif choice in answer_B:
    Restart()
  elif choice in answer_C:
    Restart()
  else:
    Restart()
#KLAAR
def end4():
  os.system('cls')
  print("\nJe laat je familie naar Nederland vliegen en sinds ruim een halfjaar zie je je familie eindelijk weer.")
  print("Je kan nu eindelijk een mooi leven opbouwen. Je kinderen kunnen gelijk naar school en ze vinden het erg leuk.\n\n[GOED EINDE]\n")
  time.sleep(1)
  print("DRUK OP ENTER")
  choice = input(">>> ")
  if choice in answer_A:
    Restart()
  elif choice in answer_B:
    Restart()
  elif choice in answer_C:
    Restart()
  else:
    Restart()
intro()
