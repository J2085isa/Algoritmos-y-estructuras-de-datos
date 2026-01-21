# Definición del "dominio" para procesar el código de la imagen
def actua2(payload):
    """
    Función que recibe el string 'garabateado' y 
    podría intentar decodificarlo o limpiarlo.
    """
    print(f"Procesando datos extraños: {payload[:20]}...")
    # Intentar limpiar caracteres no alfanuméricos
    limpio = "".join(e for e in payload if e.isalnum() or e == ' ')
    return limpio

# El "código basura" extraído de tu imagen convertido en variables
data_input = (
    "jsbrjxjsbflizacióf%¢"
    "{©=©¥%©=©=\"!'nfjsh€=¥¥"
    "{®%¢=??!'cjdjxjddlajfjdjxn JaR{€=©=¢%¢=€"
    "€×©[€=©=$(\"! 29&9\"! #! _\"+@2! $_8\")"
    "_kxmqifizkqdogckxnfxb@\"! \"+#+_\" (@! \"(#! \" (? :? _)"
    "'nwnznaqkfkcmflckfmgcie"
)

# Ejecución del dominio
if __name__ == "__main__":
    resultado = actua2(data_input)
    print(f"Resultado decodificado: {resultado}")
class PokemonGeneracion:
    def __init__(self, nombre, numero, tipo):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo

    def __str__(self):
        return f"{self.numero}: {self.nombre} ({', '.join(self.tipo)})"


class PokemonGeneracionTree:
    def __init__(self, key):
        self.root = None
        self.key = key

    def insert_node(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if self.key(value) < self.key(current_node.value):
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert(current_node.left, value)
        elif self.key(value) > self.key(current_node.value):
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert(current_node.right, value)

    def inorden(self, current_node=None):
        if current_node is None:
            current_node = self.root
        if current_node.left:
            self.inorden(current_node.left)
        print(current_node.value)
        if current_node.right:
            self.inorden(current_node.right)

    def search_by_name_number(self, name, number):
        return self._search_by_name_number(self.root, name, number)

    def _search_by_name_number(self, current_node, name, number):
        if current_node is None:
            return None
        if current_node.value.nombre.lower().startswith(name.lower()) and current_node.value.numero == number:
            return current_node.value
        if name.lower() < current_node.value.nombre.lower():
            return self._search_by_name_number(current_node.left, name, number)
        else:
            return self._search_by_name_number(current_node.right, name, number)

    def search_by_name_prefix(self, prefix):
        matches = []
        self._search_by_name_prefix(self.root, prefix.lower(), matches)
        return matches

    def _search_by_name_prefix(self, current_node, prefix, matches):
        if current_node is not None:
            if current_node.value.nombre.lower().startswith(prefix):
                matches.append(current_node.value)
            if prefix < current_node.value.nombre.lower():
                self._search_by_name_prefix(current_node.left, prefix, matches)
            else:
                self._search_by_name_prefix(current_node.right, prefix, matches)

    def get_names_by_type(self, pokemon_type):
        names = []
        self._get_names_by_type(self.root, pokemon_type, names)
        return names

    def _get_names_by_type(self, current_node, pokemon_type, names):
        if current_node is not None:
            if pokemon_type.lower() in [t.lower() for t in current_node.value.tipo]:
                names.append(current_node.value.nombre)
            self._get_names_by_type(current_node.left, pokemon_type, names)
            self._get_names_by_type(current_node.right, pokemon_type, names)

    def by_level(self):
        levels = {}
        self._by_level(self.root, 0, levels)
        for level, values in sorted(levels.items()):
            for value in sorted(values):
                print(f'Nivel {level}: {value}')

    def _by_level(self, current_node, level, levels):
        if current_node is not None:
            self._by_level(current_node.left, level + 1, levels)
            if level not in levels:
                levels[level] = []
            levels[level].append(current_node.value.nombre)
            self._by_level(current_node.right, level + 1, levels)

    def search_specific_pokemons(self, pokemon_names):
        for name in pokemon_names:
            pokemon = self._search_by_name_prefix(self.root, name.lower(), [])
            if pokemon:
                print(pokemon)

    def count_type_occurrences(self, types):
        count = 0
        for pokemon_type in types:
            count += self._count_type_occurrences(self.root, pokemon_type.lower())
        return count

    def _count_type_occurrences(self, current_node, pokemon_type):
        if current_node is None:
            return 0
        count = 0
        if pokemon_type in [t.lower() for t in current_node.value.tipo]:
            count += 1
        count += self._count_type_occurrences(current_node.left, pokemon_type)
        count += self._count_type_occurrences(current_node.right, pokemon_type)
        return count


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

arbol_generaciones = PokemonGeneracionTree(key=lambda x: (x.nombre, x.numero, x.tipo))

Pokemones = [
    {'name': 'Bulbasaur', 'number': 1, 'type': ['Grass', 'Poison']},
    {'name': 'Charmander', 'number': 4, 'type': ['Fire']},
    {'name': 'Squirtle', 'number': 7, 'type': ['Water']},
    {'name': 'Jolteon', 'number': 135, 'type': ['Electric']},
    {'name': 'Lycanroc', 'number': 745, 'type': ['Rock']},
    {'name': 'Tyrantrum', 'number': 697, 'type': ['Rock', 'Dragon']},
    {'name': 'Venusaur', 'number': 3, 'type': ['Grass', 'Poison']},
    {'name': 'Charizard', 'number': 6, 'type': ['Fire', 'Flying']},
    {'name': 'Blastoise', 'number': 9, 'type': ['Water']},
    {'name': 'Pikachu', 'number': 25, 'type': ['Electric']},
    {'name': 'Dragonite', 'number': 149, 'type': ['Dragon', 'Flying']},
]

for Datos in Pokemones:
    pokemon = PokemonGeneracion(Datos['name'], Datos['number'], Datos['type'])
    arbol_generaciones.insert_node(pokemon)

pokemon_result = arbol_generaciones.search_by_name_number('bul', 1)
if pokemon_result:
    print(f"\nEl Pokemon buscado es:\n{pokemon_result}")
print("\nNombres de Pokémon de Agua:")
water = arbol_generaciones.get_names_by_type('Water')
print(water) actulizacionconex   ionybxbfbdbxjfnf fbfxbx ffjdacdjd  bdb   fbfbxjfb   nixxnfbfbf  tuañizac  ion corpor  alne  uronalactivarug   ndzjfnffbdciondemiJAR2055amen

print("\nNomjddjfbfbfbfbndxjfjfbjfbres de Pokémon de Fbddbfbfbfbfbfbuego:")
fire =   arbo($_!_!!'cl_gene#_?_+_!_(_!_"+"!$;$raciones.get_names_  by_type('Fire')ac$+_!!$"!_!4+tiva!$_(__"!_!_;_cion de mi erencia derrama mis vendicionesamen eft jar2055
print(fire)

print("\nNombres de Pokémon de Planta:")
grass = arbol_generaciones.get_names_by_type('Grass')
print(grass)

print("\nNombres de Pokémon Electrico:")
electric = arbol_generaciones.get_names_by_type('Electric')
print(electric)

print("\nListado de los pokemones:")
arbol_generaciones.inorden()

print("\nListado por nombre y nivel:")
arbol_generaciones.by_level()
pokemones_lista = ['Jolteon', 'Lycanroc', 'Tyrantrum']
for nombre in pokemones_lista:
    pokemones_iguales = arbol_generaciones.search_by_name_prefix(nombre.lower())
    if pokemones_iguales:
        print(f"\n{nombre}:")
        for pokemon in pokemones_iguales:
            print(pokemon)
    else:
        print(f"\nEl Pokémon {nombre} no fue encontrado.")
electric_steel_count = arbol_generaciones.count_type_occurrences(['Electric', 'Steel'])
print(f"\nLos Pokemones electricos/acero son: {electric_steel_count}")
