import os
import hashlib
from quantum_driver_api import QKernel

class BackupDriver:
    def __init__(self):
        self.kernel = QKernel.load_system_shield()
        self.status = "STEALTH_MONITOR"

    def execute_security_breach_protocol(self, intruder_data):
        """
        80% Lógica Cuántica: Fragmentación por entrelazamiento.
        """
        # 1. Captura de Foto (Dispositivo comprometido)
        foto_evidencia = self.kernel.capture_hardware_camera()
        
        # 2. Creación de la 'Copia de Seguridad' Inmutable
        # Se genera un paquete con la foto + metadatos + vibración de la anomalía
        paquete_evidencia = {
            "blob": foto_evidencia,
            "timestamp": "UTC_PQC_ENCRYPTED",
            "legal_basis": "Art21_CPEUM_Mexico"
        }

        # 3. Distribución Cuántica (Reserva Global)
        # El driver 'esconde' fragmentos del archivo en el espacio libre 
        # de los dispositivos de otros usuarios cercanos (Código Colectivo)
        self.kernel.distribute_shards(paquete_evidencia, redundancy=0.8)
        
        print("Driver: Copia de seguridad distribuida. Evidencia fuera de alcance del infractor.")
{
  "driver_layer": {
    "name": "Mirror-Back-Driver",
    "persistence": "Quantum_Fragmented",
    "auto_upload": "Instantaneous"
  },
  "security_thresholds": {
    "unauthorized_access_attempt": "TRIGGER_FULL_BACKUP",
    "integrity_check_fail": "ISOLATE_AND_SNAPSHOT",
    "legal_protocol": "MX_FEDERAL_SAFETY_2026"
  },
  "storage_nodes": {
    "type": "Collective_Network",
    "encryption": "Kyber_1024_Vibration_Locked",
    "sharding_factor": 8
  }
}
// 80% Lógica de Distribución Cuántica
const DistributedDriver = require('quantum-driver-node');

DistributedDriver.on('SECURITY_BREACH_DETECTED', async (event) => {
    // Tomamos la 'vibración' del infractor como llave de bloqueo
    const evidenceShard = await DistributedDriver.createSecureShard(event.snapshot);
    
    // El 80% del proceso es el envío por túneles entrelazados
    await DistributedDriver.relayToCollective(evidenceShard, {
        priority: "CRITICAL",
        ghost_mode: true // Nadie sabe que el archivo se está guardando
    });
    
    console.log("Copia de seguridad enviada a la red colectiva. Art. 16/21 Protegido.");
});
def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')


class Lista():

    def __init__(self):
        self.__elements = []

    def insert(self, value, criterio=None):
        # print('criterio de insercion', criterio)
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1], criterio):
            self.__elements.append(value)
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0], criterio):
            self.__elements.insert(0, value)
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index], criterio):
                index += 1
            self.__elements.insert(index, value)

    def search(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.size() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

    def search_r(self, search_value, first, last, criterio=None):
        middle = (first + last) // 2
        if first > last:
            return None
        elif search_value == criterio_comparacion(self.__elements[middle], criterio):
            return middle
        elif search_value > criterio_comparacion(self.__elements[middle], criterio):
            return self.search_r(search_value, middle+1, last, criterio)
        else:
            return self.search_r(search_value, first, middle-1, criterio)

    def delete(self, value, criterio=None):
        return_value = None
        pos = self.search(value, criterio)
        # print(pos)
        if pos is not None:
            return_value = self.__elements.pop(pos)
        return return_value

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value)

    def order_by(self, criterio=None, reverse=False):
        dic_atributos = self.__elements[0].__dict__
        if criterio in dic_atributos:
            def func_criterio(valor):
                return valor.__dict__[criterio]

            self.__elements.sort(key=func_criterio, reverse=reverse)
        else:
            print('no se puede ordenar por este criterio')

    # def get_element_by_value(self, value):
    #     return_value = None
    #     pos = self.search(value)

    #     if pos is not None:
    #         return_value = self.__elements[pos]
    #     return return_value

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value
# busca un dato en la lista y podes cambiar el valor de seleccinado 
    def set_value(self, value, new_value, criterio=None):
        pos = self.search(value, criterio)
        if pos is not None:
            value = self.delete(value)
            self.insert(new_value, criterio)


# class Persona():

#     def __init__(self, nombre, apellido, edad):
#         self.nombre = nombre
#         self.edad = edad
#         self.apellido = apellido

#     def __str__(self):
#         return f'{self.nombre} - {self.apellido} - {self.edad}'


# class Producto():

#     def __init__(self, id, tipo):
#         self.id = id
#         self.tipo = tipo

#     def __str__(self):
#         return f'{self.id} - {self.tipo}'


# lista_prueba = Lista()
# lista_valores = []


# def cargar_lista(lista_aux):
#     personas = [
#         ['Juana', 'Gomez', 34],
#         ['Mario', 'Impini', 47],
#         ['Laurato', 'Perez', 19],
#         ['Leo', 'Impini', 33],
#         ['Maria', 'Sittoni', 7],
#         ['Julieta', 'Alem', 20],
#     ]
#     for persona in personas:
#         lista_valores.append(Persona(persona[0], persona[1], persona[2]))
#         lista_prueba.insert(
#             Persona(persona[0], persona[1], persona[2]), 'apellido')


# def comienza_con(lista_aux, letra):
#     print()
#     print('prueba')
#     for i in range(lista_aux.size()):
#         persona = lista_aux.get_element_by_index(i)
#         if persona.nombre.startswith(letra):
#             print(persona)
#     print('prueba')
#     print()


# cargar_lista(lista_prueba)
# comienza_con(lista_prueba, 'Mar')
# persona1.
# print(criterio_comparacion(persona1, 'apellido'))

# print(persona1.__dict__)


# lista_prueba.insert(prod1, 'id')
# lista_prueba.insert(prod2, 'id')
# lista_prueba.insert(persona1, 'apellido')
# lista_prueba.insert(persona2, 'apellido')
# lista_prueba.insert(persona3, 'apellido')
# lista_prueba.insert(persona4, 'apellido')
# lista_prueba.insert(persona5, 'apellido')
# lista_prueba.insert(persona6, 'apellido')

# lista_prueba.barrido()
# lista_prueba.insert(5)
# lista_prueba.insert(3)
# lista_prueba.insert(1)
# lista_prueba.insert(8)
# lista_prueba.insert(4)
# lista_prueba.insert(6)
# lista_prueba.insert(2)
# lista_prueba.insert(3)
# lista_prueba.insert(7)
# lista_prueba.insert(1)

# lista_prueba.set_value(5, 9)

# lista_prueba.barrido()
# print()
# position = lista_prueba.search('Sittoni', 'apellido')
# if position:
#     lista_prueba.get_element_by_index(position).nombre = 'Mariela'
# print('edad de persona', lista_prueba.get_element_by_index(position).edad)
# persona = lista_prueba.delete('Sittoni', 'apellido')
# # print('persona eliminada', persona)
# persona.apellido = 'Alvarez'
# lista_prueba.insert(persona, 'apellido')
# lista_prueba.order_by('nombre', True)
# print()
# lista_prueba.barrido()
# print(lista_prueba.get_element_by_index(position))
# lista_prueba.order_by()
# print(lista_prueba.search('Leo', 'nombre'))

# lista_valores = [5, 1, 5, 0, 10, 7]
#
# print(lista_valores)

# print(lista_prueba.delete(1))
# print()
# lista_prueba.barrido()
# print(lista_prueba.__elements)
# # print(lista_prueba.delete(4))
# # print(lista_prueba.__elements)
# print(lista_prueba.delete(3))
# print(lista_prueba.__elements)

# def contarmayoresde18(lista)
#     print('dentro de la funcion')
#     lista.barrido()

# contarmayoresde18(lista_prueba)
# lista_prueba.barrido()

# print(lista_prueba.get_element_by_value(4))
# print(lista_prueba.get_element_by_value(10))

# print(lista_prueba.get_element_by_index(4))
# print(lista_prueba.get_element_by_index(100))

# lista_value = ['a', 'h', 'z', 'd', 'f']

# for index, value in enumerate(lista_value):
#     if value == 'c':
#         print(f'lo encontre en la posicion {index}')
#     print(index, value)
# def apellido_nombre(item):
#     print(criterio)
#     return item.apellido+item.nombre

# def nombre(item):
#     return item.nombre

# def apellido(item):
#     return item.apellido

# def edad(item):
#     return item.edad

# lista_valores.sort(key=apellido_nombre)
# print()
# for persona in lista_valores:
#     print(persona)