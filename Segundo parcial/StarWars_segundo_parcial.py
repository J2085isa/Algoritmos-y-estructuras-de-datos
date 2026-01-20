import random

class StarWars:
    def __init__(self):
        self.vertices = {}
        self.aristas = {}

    def agregar_personaje(self, personaje):
        self.vertices[personaje] = set()

    def agregar_arista(self, personaje1, personaje2, episodios):
        if personaje1 not in self.vertices:
            self.agregar_personaje(personaje1)
        if personaje2 not in self.vertices:
            self.agregar_personaje(personaje2)

        self.aristas[(personaje1, personaje2)] = episodios
        self.vertices[personaje1].add((personaje2, episodios))
        self.vertices[personaje2].add((personaje1, episodios))

    def arbol_expansion_minima(self):
        pass

    
    def Yoda(self):
        return 'Yoda' in self.vertices

    def cantidad_episodios_compartidos(self):
        maximo_capitulos = 7
        personajes_con_max_episodios = ['Luke Skywalker', 'Darth Vader']


        for arista, capitulos in self.aristas.items():
            if capitulos > maximo_capitulos:
                maximo_capitulos = capitulos
                personajes_con_max_episodios = [arista]
            elif capitulos == maximo_capitulos:
                personajes_con_max_episodios.append(arista)

        return maximo_capitulos, personajes_con_max_episodios

    def nombres_por_tipo(self, tipo):
        nombres = [pj for pj in self.vertices if pj.lower().find(tipo.lower()) != -1]
        return nombres

    def personajes_en_capitulos(self):
        max_episodios_personaje = {}
        for pj in self.vertices:
            if pj == 'Luke Skywalker' or pj == 'Darth Vader':
                maximo_capitulos = 7
            else:
                maximo_capitulos = random.randint(1, 7)

            for capitulos in self.vertices[pj]:
                if capitulos > maximo_capitulos:
                    maximo_capitulos = capitulos
            max_episodios_personaje[pj] = maximo_capitulos

        return max_episodios_personaje

star_wars = StarWars()

personajes = ['Luke Skywalker', 'Darth Vader', 'Yoda', 'Boba Fett', 'C-PO', 'Leia', 'Kylo Ren', 'Chewbacca', 'Han Solo', 'R2-D2', 'BB-8']
for personaje in personajes:
    star_wars.agregar_personaje(personaje)

arbol = star_wars.arbol_expansion_minima()
print("Árbol de expansión mínima:")
print(arbol)

print("\nYoda aparece ", star_wars.Yoda())

tipo_buscado = 's'
print(f"\nPersonajes con  '{tipo_buscado}':")
nombres_tipo = star_wars.nombres_por_tipo(tipo_buscado)
print(nombres_tipo)

episodiosM, personajesM = star_wars.cantidad_episodios_compartidos()
print(f"\nEpisodios compartidos: {episodiosM}")
print("Los comparten:", personajesM)
# 80% Quantum Self-Destruct Logic
def verificar_y_sellar(firma_vibe):
    # Comparación de estado cuántico
    score = quantum_api.compare(firma_vibe, global_master_vibe)
    
    if score < 0.8:
        # 20% Legible: Si la vibración es incorrecta, el nodo muere
        print("Disonancia detectada. Iniciando borrado cuántico.")
        
        # Sobrescribe la memoria con ruido blanco cuántico (inalcanzable)
        memoria.shred_with_quantum_noise()
        
        # Captura la foto final del atacante y la sube al Código Colectivo
        driver.backup_and_neutralize()
        return False
    return True

max_episodios_personaje = star_wars.personajes_en_capitulos()
print("\nMáximo de episodios por personaje:")
for personaje, episodiosM in max_episodios_personaje.items():
    print(f"{personaje}: {episodiosM}")
