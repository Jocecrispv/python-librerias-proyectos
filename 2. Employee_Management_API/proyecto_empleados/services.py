# Import the Employee class and the in-memory list from models
from .models import empleados, Empleado

# SERVICE FUNCTIONS 

# Add a new employee
def agregar_empleado(nombre, correo, cargo, salario):
    # Generate a new unique ID based on current list length
    nuevo_id = len(empleados) + 1
    # Create a new Employee object
    nuevo_empleado = Empleado(nuevo_id, nombre, correo, cargo, salario)
    # Add it to the in-memory list
    empleados.append(nuevo_empleado)
    # Return the newly created employee
    return nuevo_empleado


# Retrieve all employees
def obtener_empleados():
    # Simply return the full list
    return empleados


# Retrieve a single employee by ID
def obtener_empleado_por_id(id):
    # Iterate through the list to find the employee
    for empleado in empleados:
        if empleado.id == id:
            return empleado
    # Return None if not found
    return None


# Update an existing employee
def modificar_empleado(id, nombre=None, correo=None, cargo=None, salario=None):
    # Find the employee first
    empleado = obtener_empleado_por_id(id)
    if empleado:
        # Update only the fields provided (partial update)
        if nombre:
            empleado.nombre = nombre
        if correo:
            empleado.correo = correo
        if cargo:
            empleado.cargo = cargo
        if salario is not None:  # Allow updating salary to 0
            empleado.salario = salario
        return empleado
    # Return None if employee not found
    return None


# Delete an employee by ID
def borrar_empleado(id):
    global empleados
    # Rebuild the list excluding the employee with the given ID
    empleados = [empleado for empleado in empleados if empleado.id != id]
    # Always return True (could be improved to return False if employee not found)
    return True
