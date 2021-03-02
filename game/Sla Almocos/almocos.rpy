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
        
        "Todo mundo foi pra Prefeitura..." if day == 2 or day == 5 or day == 7 or day == 11:
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
    $ renpy.jump("end_almoco_" + str(day))

label poke_1:
    $ renpy.jump("end_almoco_" + str(day))