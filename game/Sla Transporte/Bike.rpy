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