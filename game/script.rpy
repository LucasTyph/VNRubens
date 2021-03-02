# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

## Characters
# define = DynamicCharacter('', color="#")
define marcin = DynamicCharacter("marcio_name", color="#090909")
define rubens = DynamicCharacter("rubens_name", color="#e0e0e0")
define amarelo = DynamicCharacter("amarelo_name", color="#ffd700")
define gabigol = DynamicCharacter("gabigol_name", color="#090909")
define taliz = DynamicCharacter("taliz_name", color="#1e90ff")
define zeh = DynamicCharacter("zeh_name", color="#B8860B")
define johnny = DynamicCharacter("johnny_name", color="#B8860B")
define sane = DynamicCharacter("sane_name", color="#e0ffff")

## flags
default f_goodend = False

## variables
default v_bg = ""
default v_bg_print = ""

default day = 1

## stats
default s_boiler = 0
default s_effort = 0
default s_sadboy = 0
default s_marcin_hd = 0
default s_dogboy_hd = 0
default s_social_hd = 0

# The game starts here.

label start:

menu:

    "game":
        jump main
    
    "teste":
        jump teste

label main:

    scene bg linhaamarela

    "Parabéns, você passou na Poli para Engenharia da Computação! Infelizmente sua nota não foi boa o bastante pra passar em Ciências da Computação, mas é a vida."
    "Antes de qualquer coisa, defina seu nome:"
    
    $ player_name = renpy.input("Só não escolha boris pls", length=32)
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name="Bóris"

    if player_name.lower() == "rubens":
        $ marcio_name = "Rubens"
        $ rubens_name = "Rubens"
        $ amarelo_name = "Rubens"
        $ gabigol_name = "Rubens"
        $ taliz_name = "Rubens"
        $ zeh_name = "Rubens"
        $ johnny_name = "Rubens" 
        $ sane_name = "Rubens"
    else:
        $ marcio_name = "Marcin"
        $ rubens_name = "Rubn9"
        $ amarelo_name = "Amarelo"
        $ gabigol_name = "Gabigol"
        $ taliz_name = "Taliz"
        $ zeh_name = "Zehzin"
        $ johnny_name = "Jhone Boy" 
        $ sane_name = "Sanefuji"
    
    "Beleza, [player_name]. Agora, defina seu background -- como foi sua trajetória até chegar aqui?"

menu:

    "Etapa":
        $ v_bg = "etapa"
        $ v_bg_print = "fez Etapa"
        jump main02
    
    "ETEC":
        $ v_bg = "etec"
        $ v_bg_print = "fez ETEC"
        jump main02
    
    "Mendel":
        "vida triste lmao"
        "eternamente fadado a ser o bires ou o boris"
        "eu givaria"
        return
    
    "Passou direto":
        $ v_bg = "direto"
        $ v_bg_print = "passou direto"
        jump main02

label main02:
    
    "Então você [v_bg_print], nice."
    
    "Bom, na poli, o tempo é relativo. Você está atualmente no décimo ----to semestre, no ano 202X."
    "Suas matérias esse semestre são:"
    "SD1 com o Gomi"
    "SD2 com o Balburdini"
    "SD3 com a Cintia Boris"
    "Java OO com o Dedinhos"
    "E assim começa novamente sua jornada no inferno que é a poli."
    
    jump day_start
    
label day_start:
    
    scene bg butanta
    "Você está na estação Butantã no momento. Como você quer ir para a Poli?"
    
menu:
    
    "Bicicleta":
        scene bg bike
        $ renpy.jump("bike_" + str(day))
    
    "Circular":
        scene bg circular
        $ renpy.jump("circular_" + str(day))
    

## eventos de bike

label bike_1:
    
    "Indo de bike, você encontra o Gabigol e o Zé."
    
    show gabigol happy at left
    with dissolve
    
    gabigol "E aí zé, animado pro semestre novo?"
    
    show zeh zeh at right
    with dissolve
    
    zeh "Sei lá cara, quero café"
    
    gabigol "E você, [player_name]?"

menu:
    "Sei la, quero café também":
        jump bike_1_cafe
    "Cade minhas férias :c":
        jump bike_1_ferias

label bike_1_cafe:
    show zeh maluco
    with dissolve
    
    zeh "nice"
    
    "Vocês continuam o caminho até a Poli para a primeira aula, de SD1."
    
    jump aula_sd1_01

label bike_1_ferias:
    show gabigol angry
    with dissolve
    
    gabigol "sad"
    
    show zeh sad
    
    zeh "sad demais"
    
    $ s_sadboy += 1
    
    "Você ganhou um ponto de sadboy."
    
    "Vocês continuam o caminho até a Poli para a primeira aula, de SD1."
    
    jump aula_sd1_01

label bike_2:

    "bike dia 2"
    
    jump aula_sd2_01

label bike_3:

    "bike dia 3"
    
    jump aula_sd3_01

label bike_4:

    "bike dia 4"
    
    jump aula_java_01

label bike_5:

    "bike dia 5"
    
    jump aula_sd1_02

label bike_6:

    "bike dia 6"
    
    jump aula_sd2_02

label bike_7:

    "bike dia 7"
    
    jump aula_sd3_02

label bike_8:

    "bike dia 8"
    
    jump aula_java_02

label bike_9:

    "bike dia 9"
    
    jump aula_sd1_03

label bike_10:

    "bike dia 10"
    
    jump aula_sd2_03

label bike_11:

    "bike dia 11"
    
    jump aula_sd3_03

label bike_12:

    "bike dia 12"
    
    jump aula_java_03

## eventos de circular

label circular_1:
    
    "Na fila do circular, você encontra o Sanefuji."
    
    show sane happy
    sane "E aí, [player_name]!"
    
    "Infelizmente, o Sanefuji está cercado pelos amigos de verdade dele."
    "Ele até tenta te dar atenção, mas a força do grupo enorme com ele é grande demais."
    
    "Vocês continuam o caminho até a Poli para a primeira aula, de SD1."
    
    jump aula_sd1_01

label circular_2:

    "circular dia 2"
    
    jump aula_sd2_01

label circular_3:

    "circular dia 3"
    
    jump aula_sd3_01

label circular_4:

    "circular dia 4"
    
    jump aula_java_01

label circular_5:

    "circular dia 5"
    
    jump aula_sd1_02

label circular_6:

    "circular dia 6"
    
    jump aula_sd2_02

label circular_7:

    "circular dia 7"
    
    jump aula_sd3_02

label circular_8:

    "circular dia 8"
    
    jump aula_java_02

label circular_9:

    "circular dia 9"
    
    jump aula_sd1_03

label circular_10:

    "circular dia 10"
    
    jump aula_sd2_03

label circular_11:

    "circular dia 11"
    
    jump aula_sd3_03

label circular_12:

    "circular dia 12"
    
    jump aula_java_03

## aulas

#sd1

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


## sd2

label aula_sd2_01:

   "Aula do Balburdini"
   "O que você quer fazer?"
    
menu:
    "Varzear":
        jump almoco
        
    "Prestar atenção":
        jump almoco

label aula_sd2_02:

   "Aula do Balburdini"
   "O que você quer fazer?"
    
menu:
    "Varzear":
        jump almoco
        
    "Prestar atenção":
        jump almoco

label aula_sd2_03:

   "Aula do Balburdini"
   "O que você quer fazer?"
    
menu:
    "Varzear":
        jump almoco
        
    "Prestar atenção":
        jump almoco

## sd3

label aula_sd3_01:

   "Aula da Cintia"
   "O que você quer fazer?"
    
menu:
    "Varzear":
        jump almoco
        
    "Prestar atenção":
        jump almoco

label aula_sd3_02:

   "Aula da Cintia"
   "O que você quer fazer?"
    
menu:
    "Varzear":
        jump almoco
        
    "Prestar atenção":
        jump almoco

label aula_sd3_03:

   "Aula da Cintia"
   "O que você quer fazer?"
    
menu:
    "Varzear":
        jump almoco
        
    "Prestar atenção":
        jump almoco

## java

label aula_java_01:

   "Aula do Mark Dedos"
   "O que você quer fazer?"
    
menu:
    "Varzear":
        jump almoco
        
    "Prestar atenção":
        jump almoco

label aula_java_02:

   "Aula do Mark Dedos"
   "O que você quer fazer?"
    
menu:
    "Varzear":
        jump almoco
        
    "Prestar atenção":
        jump almoco

label aula_java_03:

   "Aula do Mark Dedos"
   "O que você quer fazer?"
    
menu:
    "Varzear":
        jump almoco
        
    "Prestar atenção":
        jump almoco

## Almoços

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

label poke_1:














##começo dos menes

label teste:

    scene bg eletrica
    with None

    "É apenas mais um dia normal no curso de Engenharia da Computação. Alunos que não queriam estar aqui chegam para dormir em aulas que eles não queriam ter."
    
    "Por pura coincidência, você encontra seus colegas da série B na entrada do prédio da Elétrica."
    
    show marcin happy
    with dissolve
    
    play sound "audio/tapa.ogg"
    
    marcin "Bom dia bom dia"
    
menu:

    "Responder com \"bom dia bom dia\"":
        $ f_goodend = True
        jump labdig
    
    "não falar nada":
        jump pathetic

label pathetic:

    show marcin pathetic
    with dissolve
    marcin "bó"
    
    jump labdig

label labdig:

    scene bg labdig
    
    "A aula atual é de labdig."
    
    show zeh sad
    with dissolve
    
    "O Zé parece que tá sofrendo do lado do marcin"
    
    show marcin happy at left
    marcin "como ta os isekai ai taliz"
    
    show taliz happy at right
    with dissolve
    
    taliz "mto bom"
    marcin "como ta o vhdl ai taliz"
    
    show taliz codando at right
    with dissolve
    
    taliz "mto sad"
    
    if f_goodend:
        "sei la final feliz"
    
    "aaaaaaaaaaaaa"
    
    return