import Pyro4
from enum import Enum

poke = Pyro4.Proxy('PYRONAME:poke')


class OperationOptions(Enum):
    CREATE = 1
    FIND_ALL = 2
    FIND_ONE = 3
    UPDATE = 4
    DELETE = 5
    EXIT = 6


# function that break the enum by the _ and return a string
def get_operation_name(operation_option):
    return operation_option.name.lower().replace('_', ' ')


def print_menu():
    print('Hello from Pokemon World, please choose an option')
    for operation_option in OperationOptions:
        print(f'{operation_option.value} - {get_operation_name(operation_option)}')


while True:
    print_menu()
    op = int(input('Select an option: '))

    if op == OperationOptions.CREATE.value:
        name = input('Pokemon name: ')
        type = input('Pokemon type: ')
        hp = int(input('Pokemon hp: '))
        attack = float(input('Pokemon attack: '))
        id = poke.create({"name": name, "type": type, "hp": hp, "attack": attack})
        print()
        print(f'Pokemon created with id: {id}')
    elif op == OperationOptions.FIND_ALL.value:
        pokemons = poke.getAll()
        print(pokemons)
    elif op == OperationOptions.FIND_ONE.value:
        id = int(input('Pokemon id: '))
        pokemon = poke.getOne(id)
        print(pokemon)
    elif op == OperationOptions.UPDATE.value:
        id = int(input('Pokemon id: '))
        name = input('Pokemon name: ')
        type = input('Pokemon type: ')
        hp = int(input('Pokemon hp: '))
        attack = float(input('Pokemon attack: '))
        poke.update(id, {"name": name})
    elif op == OperationOptions.DELETE.value:
        id = int(input('Pokemon id: '))
        poke.delete(id)
    elif op == OperationOptions.EXIT.value:
        print('Exit')
        break
    else:
        print('Invalid option')
