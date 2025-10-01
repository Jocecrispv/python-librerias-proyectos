# Define the Employee class
class Empleado:
    def __init__(self, id, nombre, correo, cargo, salario):
        # Unique identifier for the employee
        self.id = id
        # Full name of the employee
        self.nombre = nombre
        # Employee email address
        self.correo = correo
        # Job position of the employee
        self.cargo = cargo
        # Employee salary
        self.salario = salario

    # Convert the object into a dictionary (useful for JSON responses in the API)
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "cargo": self.cargo,
            "salario": self.salario
        }

# In-memory list that stores all employees
# (⚠️ Note: This data will be lost when the app restarts. For persistence, use a database.)
empleados = []
