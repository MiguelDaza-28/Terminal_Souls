import random

def damage_generation(min, max):
    return random.randint(min, max)


def status(name_h, hp, potions, name_e, enemy_hp):
    print("\n--- Actual Status ---")
    print(f"{name_h}: {hp} HP")
    print(f"Potions: {potions}")
    print(f"{name_e}: {enemy_hp} HP")


def turn(hp, enemy_hp, potions):

    option = ""

    while option not in ["1", "2", "3"]:
        print("\nWhat you want to do?\n")
        print("1. Attack")
        print("2. Heal")
        print("3. Special Attack")

        option = input("Choose an option: ")

    if option == "1":
        damage = damage_generation(10, 25)
        enemy_hp -= damage
        print(f"\n¡You made {damage} damage!\n")

    elif option == "2":
        if potions > 0:
            hp += 20
            potions -= 1
            print("\nYou healed 20 HP\n")
        else:
            print("\n You don't have potions!\n")
            return hp, enemy_hp, potions, False

    elif option == "3":
        if random.random() < 0.5:
            damage = damage_generation(30, 50)
            enemy_hp -= damage
            print(f"\n¡Special Attack! You inflicted {damage} damage!!!\n")
        else:
            print("\nYou failed the Special Attack\n")

    return hp, enemy_hp, potions, True


def enemy_turn(hp):
    damage = damage_generation(15, 20)
    hp -= damage
    print(f"You took {damage} damage!!\n")
    return hp


def winner_vf(hp, enemy_hp):
    if hp <= 0:
        print("\nDefeated...\n")
        return True
    elif enemy_hp <= 0:
        print("\nVictory!\n")
        return True
    return False


def play():
    hp_heroe = 100
    hp_enemigo = 120
    potions = 3

    print("\nWelcome to Terminal Souls\n")

    while hp_heroe > 0 and hp_enemigo > 0:

        status("Hero", hp_heroe, potions, "Enemy", hp_enemigo)

        hp_heroe, hp_enemigo, potions, turno_valido = turn(
            hp_heroe, hp_enemigo, potions)

        if not turno_valido:
            continue

        if winner_vf(hp_heroe, hp_enemigo):
            break

        hp_heroe = enemy_turn(hp_heroe)

        if winner_vf(hp_heroe, hp_enemigo):
            break


repeat = "s"

while repeat == "s":
    play()
    repeat = input("Do you want to play again? (s/n): ").lower()

print("\nThanks for playing")