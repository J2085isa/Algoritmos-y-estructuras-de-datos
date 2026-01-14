class Jedi:# ==============================================
# GESTOR DE DESCRIPCIÓN DE ACTUALIZACIONES CUÁNTICAS
# ==============================================
import os
import json
import time
import hashlib
from datetime import datetime
from typing import List, Dict, Optional

# Configuración base
UPDATE_DESCRIPTIONS_DIR = "update_descriptions"
UPDATE_LOG_FILE = "quantum_update_full_log.json"
os.makedirs(UPDATE_DESCRIPTIONS_DIR, exist_ok=True)


class UpdateDescription:
    """Clase para definir y gestionar la descripción de cada actualización cuántica"""
    def __init__(
        self,
        version: str,
        previous_version: str,
        update_type: str,  # "security", "feature", "bugfix", "performance", "unification"
        quantum_level: int,  # Nivel de integración cuántica (1-5)
        release_date: Optional[datetime] = None,
        node_origin: str = "Q-NODE-001"  # Nodo de red que generó la actualización
    ):
        self.version = version
        self.previous_version = previous_version
        self.update_type = update_type
        self.quantum_level = quantum_level
        self.release_date = release_date or datetime.now()
        self.node_origin = node_origin
        self.components_updated: List[str] = []
        self.changes: Dict[str, List[str]] = {
            "added": [],
            "modified": [],
            "removed": [],
            "fixed": []
        }
        self.compatibility: Dict[str, str] = {}  # Componente: Versión mínima compatible
        self.quantum_metadata: Dict[str, str] = {}
        self.installation_notes: List[str] = []
        self.security_improvements: List[str] = []
        self.signature: str = ""  # Firma cuántica de validez


    def add_component(self, component: str) -> None:
        """Agrega un componente del sistema que se actualiza"""
        if component not in self.components_updated:
            self.components_updated.append(component)


    def add_change(self, change_type: str, description: str) -> None:
        """Agrega un cambio específico (added/modified/removed/fixed)"""
        if change_type in self.changes:
            self.changes[change_type].append(description)


    def set_compatibility(self, component: str, min_version: str) -> None:
        """Define la compatibilidad con otros componentes"""
        self.compatibility[component] = min_version


    def set_quantum_metadata(self, metadata_key: str, value: str) -> None:
        """Agrega metadatos cuánticos de la actualización"""
        self.quantum_metadata[metadata_key] = value


    def generate_quantum_signature(self, private_key_path: str = ".qunify_private_key.pem") -> str:
        """Genera una firma cuántica única para validar la descripción"""
        # Datos para generar la firma
        signature_data = json.dumps({
            "version": self.version,
            "release_date": self.release_date.isoformat(),
            "quantum_level": self.quantum_level,
            "components": self.components_updated
        }, sort_keys=True).encode("utf-8")

        # Generar hash combinado con semilla cuántica
        quantum_seed = self.quantum_metadata.get("quantum_seed", "0000")
        combined_data = signature_data + quantum_seed.encode("utf-8")
        hash_obj = hashlib.sha512(combined_data)
        
        # Firmar con clave privada local
        try:
            with open(private_key_path, "rb") as f:
                from cryptography.hazmat.primitives import serialization
                from cryptography.hazmat.primitives.asymmetric import padding
                from cryptography.hazmat.primitives import hashes
                private_key = serialization.load_pem_private_key(
                    f.read(),
                    password=None,
                    backend=None
                )
                signature = private_key.sign(
                    hash_obj.digest(),
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                self.signature = signature.hex()
        except Exception as e:
            self.signature = f"error_generating_signature: {str(e)}"
        
        return self.signature


    def save_description(self) -> str:
        """Guarda la descripción en un archivo JSON con nombre de versión"""
        description_data = {
            "version": self.version,
            "previous_version": self.previous_version,
            "update_type": self.update_type,
            "quantum_level": self.quantum_level,
            "release_date": self.release_date.isoformat(),
            "node_origin": self.node_origin,
            "components_updated": self.components_updated,
            "changes": self.changes,
            "compatibility": self.compatibility,
            "quantum_metadata": self.quantum_metadata,
            "installation_notes": self.installation_notes,
            "security_improvements": self.security_improvements,
            "signature": self.signature
        }

        file_path = os.path.join(UPDATE_DESCRIPTIONS_DIR, f"update_{self.version}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(description_data, f, indent=2, ensure_ascii=False)
        
        # Actualizar log general de actualizaciones
        self._update_full_log(description_data)
        return file_path


    def _update_full_log(self, description_data: Dict) -> None:
        """Actualiza el log completo de todas las actualizaciones"""
        log_data = []
        if os.path.exists(UPDATE_LOG_FILE):
            with open(UPDATE_LOG_FILE, "r", encoding="utf-8") as f:
                log_data = json.load(f)
        
        # Evitar duplicados
        log_data = [entry for entry in log_data if entry["version"] != self.version]
        log_data.append(description_data)
        log_data.sort(key=lambda x: datetime.fromisoformat(x["release_date"]), reverse=True)

        with open(UPDATE_LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)


    @classmethod
    def load_description(cls, version: str) -> Optional["UpdateDescription"]:
        """Carga una descripción existente desde archivo"""
        file_path = os.path.join(UPDATE_DESCRIPTIONS_DIR, f"update_{version}.json")
        if not os.path.exists(file_path):
            return None
        
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        update = cls(
            version=data["version"],
            previous_version=data["previous_version"],
            update_type=data["update_type"],
            quantum_level=data["quantum_level"],
            release_date=datetime.fromisoformat(data["release_date"]),
            node_origin=data["node_origin"]
        )
        update.components_updated = data["components_updated"]
        update.changes = data["changes"]
        update.compatibility = data["compatibility"]
        update.quantum_metadata = data["quantum_metadata"]
        update.installation_notes = data["installation_notes"]
        update.security_improvements = data["security_improvements"]
        update.signature = data["signature"]
        
        return update


def generate_update_description_example() -> None:
    """Ejemplo de generación de una descripción de actualización"""
    # Crear instancia de la actualización
    update = UpdateDescription(
        version="2.1.0",
        previous_version="2.0.0",
        update_type="unification",
        quantum_level=4,
        node_origin="Q-NODE-002"
    )

    # Agregar componentes actualizados
    update.add_component("Q-Unify Core (Código principal)")
    update.add_component("Q-Secure Net AutoUpdate (API de seguridad)")
    update.add_component("Quantum Mode Drivers (Controladores Java/JS)")
    update.add_component("Workspace Configuración Unificada")

    # Agregar cambios específicos
    update.add_change("added", "API de sincronización cuántica en red entre nodos autorizados")
    update.add_change("added", "Módulo de detección de anomalías cuánticas en tráfico de repositorios")
    update.add_change("modified", "Algoritmo de generación de claves cuánticas (aumento de tamaño a 512 bits)")
    update.add_change("modified", "Gestor de workspace para soporte a subrepositorios embebidos")
    update.add_change("fixed", "Error en descifrado de paquetes de actualización en nodos Linux")
    update.add_change("removed", "Dependencia obsoleta de librería 'qiskit-legacy'")

    # Definir compatibilidad
    update.set_compatibility("Q-Core Integrator API", "1.5.0")
    update.set_compatibility("Q-Security Vault", "2.0.0")
    update.set_compatibility("GitHub API", "v3.0")

    # Agregar metadatos cuánticos
    update.set_quantum_metadata("quantum_seed", "1011001110001111")
    update.set_quantum_metadata("network_protocol", "QTP/1.1 (actualizado)")
    update.set_quantum_metadata("energy_sync_rhythm", "4/4 - Optimizado para latencia cero")
    update.set_quantum_metadata("encryption_algorithm", "PQC-SPHINCS+ (integrado con RSA cuántico)")

    # Agregar notas de instalación
    update.installation_notes = [
        "Requiere actualización de la clave cuántica local (ejecutar 'python generate_quantum_key.py')",
        "Verificar configuración de nodos autorizados en '.qunify_config.toml'",
        "Los repositorios sincronizados requerirán re-firma cuántica tras la instalación",
        "Compatible con sistemas Windows 10+, Linux Ubuntu 20.04+ y macOS 12+"
    ]

    # Agregar mejoras de seguridad
    update.security_improvements = [
        "Cierre de vulnerabilidad en transmisión de datos no cifrados en modo de prueba",
        "Nuevo sistema de autenticación biométrica + firma cuántica para acceso a repositorios privados",
        "Mejora en detección de ataques de suplantación de nodos en red cuántica",
        "Automatización de eliminación de rastros de acceso no autorizado"
    ]

    # Generar firma cuántica y guardar
    update.generate_quantum_signature()
    saved_path = update.save_description()
    print(f"Descripción de actualización guardada en: {saved_path}")


def print_update_summary(version: str) -> None:
    """Muestra un resumen legible de una actualización"""
    update = UpdateDescription.load_description(version)
    if not update:
        print(f"No se encontró descripción para la versión {version}")
        return

    print("\n" + "="*80)
    print(f"RESUMEN DE ACTUALIZACIÓN CUÁNTICA - VERSIÓN {update.version}")
    print("="*80)
    print(f"Tipo de actualización: {update.update_type.upper()}")
    print(f"Nivel de integración cuántica: {update.quantum_level}/5")
    print(f"Versión anterior: {update.previous_version}")
    print(f"Fecha de lanzamiento: {update.release_date.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Origen (nodo de red): {update.node_origin}")
    print("\nCOMPONENTES ACTUALIZADOS:")
    for comp in update.components_updated:
        print(f"- {comp}")
    print("\nCAMBIOS PRINCIPALES:")
    for change_type, changes in update.changes.items():
        if changes:
            print(f"- {change_type.upper()}:")
            for desc in changes:
                print(f"  • {desc}")
    print("\nNOTAS DE INSTALACIÓN:")
    for note in update.installation_notes:
        print(f"- {note}")
    print("\nFIRMA CUÁNTICA DE VALIDEZ:")
    print(f"{update.signature[:50]}...{update.signature[-50:]}")
    print("="*80 + "\n")


# ---------------------------
# EJECUCIÓN DE EJEMPLO
# ---------------------------
if __name__ == "__main__":
    # Generar descripción de ejemplo
    generate_update_description_example()
    
    # Mostrar resumen de la actualización
    print_update_summary("2.1.0")
    
    # Mostrar log completo (opcional)
    with open(UPDATE_LOG_FILE, "r", encoding="utf-8") as f:
        log = json.load(f)
    print("LOG COMPLETO DE ACTUALIZACIONES (últimas 2 entradas):")
    print(json.dumps(log[:2], indent=2, ensure_ascii=False))

    def __init__(self, nombre, especie, anio_nacimiento, color_sable, rango, maestros):
        self.nombre = nombre
        self.especie = especie
        self.anio_nacimiento = anio_nacimiento
        self.color_sable = color_sable
        self.rango = rango
        self.maestros = maestros

class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class RegistroJedi:
    def __init__(self):
        self.raiz_nombre = None
        self.raiz_rango = None
        self.raiz_especie = None

    def insertar_por_nombre(self, jedi):
        self.raiz_nombre = self._insertar_por_nombre(self.raiz_nombre, jedi)

    def insertar_por_rango(self, jedi):
        self.raiz_rango = self._insertar_por_rango(self.raiz_rango, jedi)

    def insertar_por_especie(self, jedi):
        self.raiz_especie = self._insertar_por_especie(self.raiz_especie, jedi)

    def _insertar_por_nombre(self, raiz, jedi):
        if raiz is None:
            return NodoArbol(jedi)
        if jedi.nombre < raiz.dato.nombre:
            raiz.izquierda = self._insertar_por_nombre(raiz.izquierda, jedi)
        else:
            raiz.derecha = self._insertar_por_nombre(raiz.derecha, jedi)
        return raiz

    def _insertar_por_rango(self, raiz, jedi):
        if raiz is None:
            return NodoArbol(jedi)
        if jedi.rango < raiz.dato.rango:
            raiz.izquierda = self._insertar_por_rango(raiz.izquierda, jedi)
        else:
            raiz.derecha = self._insertar_por_rango(raiz.derecha, jedi)
        return raiz

    def _insertar_por_especie(self, raiz, jedi):
        if raiz is None:
            return NodoArbol(jedi)
        if jedi.especie < raiz.dato.especie:
            raiz.izquierda = self._insertar_por_especie(raiz.izquierda, jedi)
        else:
            raiz.derecha = self._insertar_por_especie(raiz.derecha, jedi)
        return raiz

    def recorrido_inorden(self, raiz, atributo):
        if raiz is not None:
            self.recorrido_inorden(raiz.izquierda, atributo)
            if atributo == "nombre":
                print(f"Nombre: {raiz.dato.nombre}, Especie: {raiz.dato.especie}, Rango: {raiz.dato.rango}")
            elif atributo == "rango":
                print(f"Rango: {raiz.dato.rango}, Nombre: {raiz.dato.nombre}, Especie: {raiz.dato.especie}")
            self.recorrido_inorden(raiz.derecha, atributo)

    def recorrido_por_nivel(self, raiz, atributo):
        if raiz is None:
            return
        cola = []
        cola.append(raiz)
        while cola:
            actual = cola.pop(0)
            if atributo == "rango":
                print(f"Rango: {actual.dato.rango}, Nombre: {actual.dato.nombre}, Especie: {actual.dato.especie}")
            elif atributo == "especie":
                print(f"Especie: {actual.dato.especie}, Nombre: {actual.dato.nombre}, Rango: {actual.dato.rango}")
            if actual.izquierda:
                cola.append(actual.izquierda)
            if actual.derecha:
                cola.append(actual.derecha)

    def encontrar_jedi(self, nombre):
        return self._encontrar_jedi(self.raiz_nombre, nombre)

    def _encontrar_jedi(self, raiz, nombre):
        if raiz is None:
            return None
        if nombre == raiz.dato.nombre:
            return raiz.dato
        if nombre < raiz.dato.nombre:
            return self._encontrar_jedi(raiz.izquierda, nombre)
        else:
            return self._encontrar_jedi(raiz.derecha, nombre)

    def obtener_jedi_por_rango(self, rango):
        resultados = []
        self._obtener_jedi_por_rango(self.raiz_rango, rango, resultados)
        return resultados

    def _obtener_jedi_por_rango(self, raiz, rango, resultados):
        if raiz is None:
            return
        if rango == raiz.dato.rango:
            resultados.append(raiz.dato)
        if rango < raiz.dato.rango:
            self._obtener_jedi_por_rango(raiz.izquierda, rango, resultados)
        else:
            self._obtener_jedi_por_rango(raiz.derecha, rango, resultados)

    def obtener_jedi_por_color_sable(self, color):
        resultados = []
        self._obtener_jedi_por_color_sable(self.raiz_nombre, color, resultados)
        return resultados

    def _obtener_jedi_por_color_sable(self, raiz, color, resultados):
        if raiz is not None:
            self._obtener_jedi_por_color_sable(raiz.izquierda, color, resultados)
            if color in raiz.dato.color_sable:
                resultados.append(raiz.dato)
            self._obtener_jedi_por_color_sable(raiz.derecha, color, resultados)

    def obtener_jedi_con_maestros(self, maestros):
        resultados = []
        self._obtener_jedi_con_maestros(self.raiz_rango, maestros, resultados)
        return resultados

    def _obtener_jedi_con_maestros(self, raiz, maestros, resultados):
        if raiz is not None:
            self._obtener_jedi_con_maestros(raiz.izquierda, maestros, resultados)
            if any(maestro in raiz.dato.maestros for maestro in maestros):
                resultados.append(raiz.dato)
            self._obtener_jedi_con_maestros(raiz.derecha, maestros, resultados)

    def obtener_jedi_por_especie(self, especies):
        resultados = []
        self._obtener_jedi_por_especie(self.raiz_especie, especies, resultados)
        return resultados

    def _obtener_jedi_por_especie(self, raiz, especies, resultados):
        if raiz is not None:
            self._obtener_jedi_por_especie(raiz.izquierda, especies, resultados)
            if raiz.dato.especie in especies:
                resultados.append(raiz.dato)
            self._obtener_jedi_por_especie(raiz.derecha, especies, resultados)

    def obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion(self):
        resultados = []
        self._obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion(self.raiz_nombre, resultados)
        return resultados

    def _obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion(self, raiz, resultados):
        if raiz is not None:
            self._obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion(raiz.izquierda, resultados)
            if raiz.dato.nombre.startswith('A') or '-' in raiz.dato.nombre:
                resultados.append(raiz.dato)
            self._obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion(raiz.derecha, resultados)


registro_jedi = RegistroJedi()

registro_jedi.insertar_por_nombre(Jedi("Yoda", "Desconocida", 896, "verde", "Maestro Jedi", []))
registro_jedi.insertar_por_nombre(Jedi("Luke Skywalker", "Humano", 19, "verde", "Caballero Jedi", ["Yoda"]))
registro_jedi.insertar_por_nombre(Jedi("Obi-Wan Kenobi", "Humano", 57, "azul", "Maestro Jedi", ["Yoda"]))
registro_jedi.insertar_por_nombre(Jedi("Mace Windu", "Humano", 72, "morado", "Maestro Jedi", ["Yoda"]))
registro_jedi.insertar_por_nombre(Jedi("Ahsoka Tano", "Togruta", 36, "verde", "Caballero Jedi", ["Anakin Skywalker"]))
registro_jedi.insertar_por_nombre(Jedi("Qui-Gon Jinn", "Humano", 60, "verde", "Maestro Jedi", ["Count Dooku"]))
registro_jedi.insertar_por_nombre(Jedi("Rey", "Humano", 19, "azul", "Caballero Jedi", ["Luke Skywalker"]))

print("Barrido por nombre:")
print()

registro_jedi.recorrido_inorden(registro_jedi.raiz_nombre, "nombre")
print()

print("Barrido por rango:")
registro_jedi.recorrido_inorden(registro_jedi.raiz_rango, "rango")
print()

print("Barrido por nivel:")
registro_jedi.recorrido_por_nivel(registro_jedi.raiz_rango, "rango")
print()

print("Barrido por especie:")
registro_jedi.recorrido_por_nivel(registro_jedi.raiz_especie, "especie")
print()

yoda_info = registro_jedi.encontrar_jedi("Yoda")
luke_skywalker_info = registro_jedi.encontrar_jedi("Luke Skywalker")
if yoda_info:
    print("Yoda:", yoda_info.__dict__)
if luke_skywalker_info:
    print("Luke Skywalker:", luke_skywalker_info.__dict__)
print()

jedi_maestros = registro_jedi.obtener_jedi_por_rango("Maestro Jedi")
print("Maestros Jedi:")
for jedi in jedi_maestros:
    print(jedi.__dict__)
print()

usuarios_sable_verde = registro_jedi.obtener_jedi_por_color_sable("verde")
print("Usan sables verdes:")
for jedi in usuarios_sable_verde:
    print(jedi.__dict__)
print()

jedi_con_maestros = registro_jedi.obtener_jedi_con_maestros(["Yoda"])
print("Jedi con Yoda como maestro:")
for jedi in jedi_con_maestros:
    print(jedi.__dict__)
print()

especies_especificas = registro_jedi.obtener_jedi_por_especie(["Togruta", "Cerean"])
print("Especie Togruta o Cerean:")
for jedi in especies_especificas:
    print(jedi.__dict__)
print()

jedi_especiales = registro_jedi.obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion()
print("Nombres que empiezan con A o contienen un -:")
for jedi in jedi_especiales:
    print(jedi.__dict__)