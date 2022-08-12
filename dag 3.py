print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welkom op LuckyCraft, we geven hier een introductie over iedereen.")
keus = int(input(("Met wie wil je als eerste kennis maken?\n1) Erik\n2) Luuk \n3) Sven\n4) Ole\n")))
if keus == 1:
    print("Oke je hebt besloten Erik te ontmoeten.")
    keus = str(input("Erik probeert je al direct een lucky rank aan te smeren wat doe je? 'kopen' of 'niks'"))
    if keus == 'kopen':
        keus = str(input(("Je hebt Erik erg blij gemaakt, hij zet ook nog een deal op voor 40x sleutels voor maar $800,- en een speciale tag, wil je dit? 'ja' of 'nee'")))
        if keus == 'ja':
            print("Je krijgt een eigen speciale tag, top donateur tag + een chat kleur. LuckyCraft kan nu een bouwer inhuren en pescada plugins kopen extra")
        elif keus == 'nee':
            print("Erik kijkt teleurgesteld en springt van een brug")
    elif keus == 'niks':
        print("Erik krijgt een paniek aanval en koopt een $1000 bouwer en heeft geen geld meer om de server te huren, luckycraft sluit.")
if keus == 2:
    keus = str(input(("Luuk is bezig met Erik zijn shit fixen en zijn discord bot te programmeren, je hoort hem 10x zeggen 'ik ben echt een retard', wat doe je 'helpen' of 'niks'\n")))
    if keus == 'helpen':
        print("Je probeert Luuk te helpen, alleen hij raakt geirriteerd en zegt dit wist ik al\nhij programmeert vervolgens een bot die je uitscheld")
    elif keus == 'niks':
        keus = input("Luuk roept je terug en zegt hij kan je bot fixen wat wil je? 'oke' of 'nee'\n")
        if keus == 'oke':
            print("Hij clipt tijdens het helpen de secret van je bot en geeft zichzelf admin permissies om vervolgens je discord te nuke\nLuuk heeft zijn ultieme wraak omdat je geen hukp aanbood.")
        elif keus == 'nee':
            print("Luuk bant je van de minecraft server voor L bozo")
if keus == 3:
    print("Je probeert hallo te zeggen maar Sven lult al een verhaal over command blocks en plugins op splashcraft")
    keus = input("je hebt nu twee keuzes: wat doe je 'rennen' , 'luisteren' 'zelfmoord'\n")
    if keus == 'rennen':
        print("Je hebt een goede keus gemaakt door te rennen, maar Sven rent achter je aan en zegt dat hij tot trap 22 kan rennen\nen top conditie heeft, hij zal je nu voor eeuwig achterna zitten")
    elif keus == 'luisteren':
        print("Je raakt verward over alle kut termen die Sven gebruikt en wanneer je uitleg vraagt kan Sven het niet uitleggen\nje raakt in de war en je wilt dood")
    elif keus == 'zeldmoord':
        print("je loopt naar het spoor en je laat je overrijden door een trein, je hebt de goede keus gemaakt.")
if keus == 4:
    print("Je komt Ole tegen, hij ziet er chill uit maar vind luckycraft saai en dat hij nooit meer geld gaat uitgeven")
    keus = input("Je geeft hem twee opties 'survival' of 'skymine'\n")
    if keus == 'skymine':
        print("Ole zegt dat hij alle woorden die hij heeft gezegd niet meende en spend vervolgen weer geld en grind skymine")
        print("ole is weer gelukkig <3")
    elif keus == 'survival':
        keus = input("Ole blijft shit praten over luckycraft en begint zijn eigen server Olecraft die veel meer succesvol wordt dan Lucky\nOle wordt nu de grootste concurrent van lucky en ze worden grootste vijanden. je hebt opnieuw een keus 'olecraft of 'luckycraft'\n")
        if keus == 'olecraft':
            print("ole slaat je met een hoe met sharpness 1000 en gebruikt commandblocks om mobs op je hoofd te spanwnen")
        if keus == 'luckycraft':
            print("Erik probeert je de gloednieuwe zomer rank aan te smeren om een nieuwe $1500 bouwer in te huren voor skymine 2")