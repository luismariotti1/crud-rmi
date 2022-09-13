import Pyro4

db_data = []
index = 1


@Pyro4.expose
class PokemonCRUD:
    def create(self, pokemon):
        global index
        pokemon['id'] = index
        index += 1
        db_data.append(pokemon)
        return {'code': 201, 'message': 'Pokemon created: {}'.format(pokemon)}

    def getAll(self):
        return {'code': 200, 'pokemons': db_data}

    def getOne(self, id):
        pokemon = search(id)
        if pokemon:
            return {'code': 200, 'pokemon': pokemon}
        else:
            return {'code': 404, 'message': 'Pokemon not found'}

    def update(self, id, data):
        pokemon = search(id)
        if pokemon:
            pokemon.update(data)
            return 'Pokemon updated: {}'.format(pokemon)
        else:
            return {'code': 404, 'message': 'Pokemon not found'}

    def delete(self, id):
        pokemon = search(id)
        if pokemon:
            db_data.remove(pokemon)
            return {'code': 200, 'message': 'Pokemon deleted: {}'.format(pokemon)}
        else:
            return {'code': 404, 'message': 'Pokemon not found'}


# search pokemon by id
def search(id):
    for pokemon in db_data:
        if pokemon['id'] == id:
            return pokemon
    return None


def main():
    # create a pokemon crud object
    poke = PokemonCRUD()

    # register calculator object with Pyro
    daemon = Pyro4.Daemon()
    uri = daemon.register(poke)
    print(uri)

    # register dns name
    Pyro4.locateNS().register("poke", uri)

    daemon.requestLoop()


if __name__ == '__main__':
    main()
