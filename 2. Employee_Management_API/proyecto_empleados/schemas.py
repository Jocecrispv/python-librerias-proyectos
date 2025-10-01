# Import Marshmallow tools for schema definition and validation
from marshmallow import Schema, fields, validate

# Define a schema for employee data validation and serialization
class EmpleadoSchema(Schema):
    # Employee ID (read-only, automatically generated, not required in input)
    id = fields.Int(dump_only=True)  

    # Employee full name (required, must be 1-100 characters)
    nombre = fields.Str(required=True, validate=validate.Length(min=1, max=100))

    # Employee email (required, must be a valid email format)
    correo = fields.Email(required=True)

    # Job position (required, must be 1-50 characters)
    cargo = fields.Str(required=True, validate=validate.Length(min=1, max=50))

    # Salary (required, must be a positive number)
    salario = fields.Float(required=True, validate=validate.Range(min=0))
