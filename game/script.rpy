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
    
jump bike_1



## aulas

#sd1
jump aula_sd1_01
label end_aula_sd1_01:



## sd2



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



label end_almoco_1:
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