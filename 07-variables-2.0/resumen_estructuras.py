"""
RESUMEN: ESTRUCTURAS DE DATOS EN PYTHON (LISTA, TUPLA Y DICCIONARIO)

En Python, la diferencia principal entre una tupla, una lista y un diccionario radica en cómo almacenan los datos, si se pueden modificar después de creados (mutabilidad) y cómo se accede a ellos.

TABLA COMPARATIVA RÁPIDA:
--------------------------------------------------------------------------------
Característica | Lista (list)      | Tupla (tuple)     | Diccionario (dict)
--------------------------------------------------------------------------------
Mutabilidad    | Mutable           | Inmutable         | Mutable
Sintaxis       | [1, 2, "a"]       | (1, 2, "a")       | {"clave": "valor"}
Acceso         | Por índice        | Por índice        | Por clave
Orden          | Ordenada          | Ordenada          | Ordenado (Py 3.7+)
Uso típico     | Colecciones din.  | Datos fijos       | Pares clave-valor
--------------------------------------------------------------------------------

1. LISTA (list)
Las listas son colecciones ordenadas y mutables.
- Mutables: Puedes cambiar, añadir o eliminar elementos.
Ejemplo:
tareas = ["comprar pan", "estudiar Python", "limpiar"]
tareas.append("programar")

2. TUPLA (tuple)
Las tuplas son ordenadas pero inmutables.
- Inmutables: No se pueden modificar una vez creadas.
- Ventajas: Menor consumo de memoria, más rápidas, pueden ser claves en diccionarios.
Ejemplo:
coordenadas = (10.5, 20.3)

3. DICCIONARIO (dict)
Almacenan pares de "clave-valor".
- Claves únicas: Deben ser tipos inmutables.
- Mutables: Puedes añadir, modificar o eliminar dinámicamente.
Ejemplo:
usuario = {"nombre": "Ricardo", "nivel": "intermedio"}
print(usuario["nombre"])

¿CUÁNDO USAR CADA UNA?
- Lista: Cuando necesites una secuencia que cambiará o requiere operaciones frecuentes.
- Tupla: Cuando tengas datos fijos que deben mantenerse intactos.
- Diccionario: Cuando necesites buscar, asociar o actualizar datos rápidamente mediante etiquetas.
"""
