import random as rnd

# Estadísticas pokemon de entrenador y rival
atqpoke1= rnd.randint(1,100)
defpoke1= rnd.randint(1,100)
atqpoke2= rnd.randint(1,100)
defpoke2= rnd.randint(1,100)
hp1 = hp2 = 100

#Tipo de pokemon rival
tipos= ['Agua','Fuego','Planta','Eléctrico']
PokeRival= rnd.choice(tipos)

#Efectividad Tipo vs Tipo
def calcular_efectividad(PokeAtacante, PokeDefensor):
    tabla_efectos={
        'Agua': {'Agua': 0.5, 'Fuego': 2, 'Planta':0.5, 'Eléctrico':1},
        'Fuego': {'Agua': 0.5, 'Fuego': 0.5, 'Planta':2, 'Eléctrico':1},
        'Planta': {'Agua': 2, 'Fuego': 0.5, 'Planta':0.5, 'Eléctrico':1},
        'Eléctrico': {'Agua': 2, 'Fuego': 1, 'Planta':0.5, 'Eléctrico':0.5}
    }
    return tabla_efectos[PokeAtacante][PokeDefensor]

#determinar mensaje de efectividad
def obtner_efecto(efectividad):
    if efectividad ==1:
        return 'Neutral'
    elif efectividad ==2:
        return 'SUPER EFECTIVO'
    elif efectividad ==0.5:
        return '...No es muy efectivo'
#Calcular el daño
def dmg_hecho(atq,defensa,efectividad):
    return round(30 *( atq/defensa)*efectividad)

    

#PRIMERA FASE - Datos pokemon entrenador y rival

print('BATALLA POKÉMON')
entrenador= input('¿Cuál es tu nombre entrenador?: ')
print(f'\nHola {entrenador}, esta es tu primera batalla, digita los datos de tu pokémon: ')

#Pokemon Entrenador
while True:
    
    print('\nTipo de Pokémon:')
    for i, tipo in enumerate(tipos, start=1):
        print(f'{i}.{tipo}')
    try:
        eleccion= int(input('Elige del 1 al 4: '))
        
        if 1 <= eleccion <= 4:
            tipo_entrenador= tipos[eleccion - 1]
            print(f'Tu pokémon es de tipo {tipo_entrenador}')
            break
        else:
            print('Por favor, elige una opción válida entre 1 y 4')
    except ValueError:
        print(f'Hey {entrenador} solo se admiten números >:T')

print(f'Tu pokemón tiene {atqpoke1} puntos de ATQ, {defpoke1} puntos de DEF y {hp1} HP')
print('\nAhora veamos a tu oponente')
print(f'\nPokeRival es un pokemon tipo {PokeRival}. Con {atqpoke2} de ATQ , {defpoke2} de DEF y {hp2} HP')

# SEGUNDA FASE - Combate pokemon
print('\nQue comienze la batalla!!')
print('\nHaces el primer ataque...')

while hp1> 0 and hp2 >0:
    #Entrenador vs Rival - primer ataque
    efectividad= calcular_efectividad(tipo_entrenador, PokeRival)
    # Daño del primer ataque
    dmg= dmg_hecho(atqpoke1,defpoke2,efectividad)
    hp2= max(0,round(hp2 - dmg)) #evitar que de negativo la vida del rival
    efecto= obtner_efecto(efectividad)

    print(f'\nPokeRival recibe {dmg} de daño.')
    print(f'Efectividad: {efecto}')
    print(f'PokeRival quedó con {hp2} de vida')

    if hp2 <= 0:
        print(f'GANASTE EL COMBATE!!!\nFelicidades {entrenador}!')
        break
    else:
        print('\nPokeRival ataca...')
        #atque rival
        efectividad= calcular_efectividad(PokeRival, tipo_entrenador)
        # Daño del primer ataque
        dmgRival= dmg_hecho(atqpoke2,defpoke1,efectividad)
        hp1= max(0,round(hp1 - dmgRival)) #asegura que tu vida no baje de 0
        efectoRival = obtner_efecto(efectividad)

        print(f'\nRecibes {dmgRival} de daño')
        print(f'Efectividad:{efectoRival}')
        print(f'Quedaste con {hp1} de vida')
        if hp1 <= 0:
            print('Perdiste el combate :c ¡Corre al centro pokémon!')
            break
        else:
            print('\nSigue el combate...')
        