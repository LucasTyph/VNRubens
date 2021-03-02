#SD1

label aula_sd1_01:
    
    scene bg sala
    with dissolve

    "A primeira aula é com o professor Gomi."
    "Ele assume que vocês já manjam de VHDL, e começa a explicar o funcionamento do código de Hemming."
    "O que você quer fazer?"
    menu:
        "Varzear":
            show johnny class at left
            johnny "Hey, [player_name]."
            "Você sabia que o nome do Gomi em japonês significa lixo?"
            
            show zeh maluco at right
            
            zeh "edson satoshi lixo kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
            
            $ s_boiler += 1
            "Você ganhou um ponto de Boiler."
            
            jump almoco
            
        "Prestar atenção":
            "O professor se perdeu na explicação e não conseguiu falar nada de útil depois de 5 minutos."
            "Você não aprendeu nada, e começou a questionar o quão bons são os professores da poli."
            $ s_sadboy += 1
            "Você ganhou um ponto de Sadboy."
            jump almoco


label aula_sd1_02:
   
   "Aula do Gomi"
   "O que você quer fazer?"
    
menu:
    "Varzear":
        jump almoco
        
    "Prestar atenção":
        jump almoco

label aula_sd1_03:

   "Aula do Gomi"
   "O que você quer fazer?"
    
menu:
    "Varzear":
        jump almoco
        
    "Prestar atenção":
        jump almoco