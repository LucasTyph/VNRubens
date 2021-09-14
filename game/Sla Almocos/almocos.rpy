label almoco:
    
    "É hora do almoço. Não seja um sanefuji e escolha um lugar para almoçar"
    
    menu:

        "Comer na física com o Zé e com o Gabigol" if day == 1:
            jump fisica
        
        "Comer no poke com o Rubens" if day == 6 or day == 10:
            $ renpy.jump("poke_" + str(day))
        
        "Comer no poke com o pessoal pós java" if day == 4 or day == 8 or day == 12:
            $ renpy.jump("poke_" + str(day))
        
        "Ir na Prefeitura com o Marcin" if day == 2:
            $ renpy.jump("pref_" + str(day))
        
        "Todo mundo foi pra Prefeitura..." if day == 3 or day == 5 or day == 7 or day == 9 or day == 11:
            $ renpy.jump("pref_" + str(day))

label fisica:

    show gabigol angry at left
    with dissolve
    gabigol "Cara."
    
    show zeh happy at right
    with dissolve
    zeh "Que?"
    
    gabigol "Isso é o dedão do porco?"
    
    show zeh annoyed
    zeh "wtf"
    
    "E ninguém nunca mais quis comer na Física."
    jump end_almoco

label poke_4:
    jump end_almoco

label poke_6:
    jump end_almoco

label poke_8:
    jump end_almoco

label poke_10:
    jump end_almoco

label poke_12:
    jump end_almoco

label pref_2:
    jump end_almoco

label pref_3:
    jump end_almoco

label pref_5:
    jump end_almoco

label pref_7:
    jump end_almoco

label pref_9:
    jump end_almoco

label pref_11:
    jump end_almoco


label end_almoco:
    "Com isso, todo mundo foi pra casa."
    "Você se prepara para as aulas do dia seguinte..."
    $ day += 1
    jump day_start