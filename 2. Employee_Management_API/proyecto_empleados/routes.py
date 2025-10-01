# Import Flask tools for creating routes
from flask import Blueprint, jsonify, request 

# Import service functions that handle the business logic
from .services import (
    agregar_empleado,
    obtener_empleados,
    obtener_empleado_por_id,
    modificar_empleado,
    borrar_empleado
)

# Import schema for validating and serializing employee data
from .schemas import EmpleadoSchema

# Create a Blueprint for the employee routes
# This groups all routes under a single logical module
empleados_bp = Blueprint('empleados', __name__)

# Initialize the schema (used for validation and JSON serialization)
empleado_schema = EmpleadoSchema()


# ROUTES 

# Add a new employee (CREATE)
@empleados_bp.route('/empleados', methods=['POST'])
def agregar_empleado_route():
    datos = request.json  # Get request body (JSON data)
    errors = empleado_schema.validate(datos)  # Validate input against schema
    if errors:
        return jsonify({"error": errors}), 400  # Return validation errors

    # Call the service function to create a new employee
    empleado = agregar_empleado(datos['nombre'], datos['correo'], datos['cargo'], datos['salario'])
    # Return the new employee data as JSON with 201 Created status
    return jsonify(empleado_schema.dump(empleado)), 201


# Get all employees (READ ALL)
@empleados_bp.route('/empleados', methods=['GET'])
def obtener_empleados_route():
    empleados = obtener_empleados()  # Get the list of employees
    # Serialize multiple objects (many=True)
    return jsonify(empleado_schema.dump(empleados, many=True))


# Get a single employee by ID (READ ONE)
@empleados_bp.route('/empleados/<int:id>', methods=['GET'])
def obtener_empleado_route(id):
    empleado = obtener_empleado_por_id(id)  # Find employee by ID
    if empleado:
        return jsonify(empleado_schema.dump(empleado))  # Return if found
    else:
        return jsonify({"error": "Employee not found"}), 404


# Update employee information (UPDATE)
@empleados_bp.route('/empleados/<int:id>', methods=['PUT'])
def modificar_empleado_route(id):
    datos = request.json  # Get request body
    # Allow partial validation (not all fields required)
    errors = empleado_schema.validate(datos, partial=True)  
    if errors:
        return jsonify({"error": errors}), 400

    # Call service to update employee
    empleado = modificar_empleado(
        id, 
        datos.get('nombre'), 
        datos.get('correo'), 
        datos.get('cargo'), 
        datos.get('salario')
    )
    if empleado:
        return jsonify(empleado_schema.dump(empleado))  # Return updated data
    else:
        return jsonify({"error": "Employee not found"}), 404


# Delete an employee (DELETE)
@empleados_bp.route('/empleados/<int:id>', methods=['DELETE'])
def borrar_empleado_route(id):
    if borrar_empleado(id):  # Try deleting employee
        return jsonify({"mensaje": "Employee deleted successfully"})
    else:
        return jsonify({"error": "Employee not found"}), 404
