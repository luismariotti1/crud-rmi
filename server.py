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
        return pokemon['id']

    def getAll(self):
        return db_data

    def getOne(self, id):
        pokemon = search(id)
        return pokemon

    def update(self, id, data):
        pokemon = search(id)
        pokemon.update(data)
        return pokemon

    def delete(self, id):
        pokemon = search(id)
        db_data.remove(pokemon)
        return pokemon['id']

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
