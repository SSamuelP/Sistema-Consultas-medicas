from app.Personas.paciente import Paciente
from app.Personas.medico import Medico

class PersonasFactory:
    @staticmethod
    def crear_persona(tipo, identificacion, nombre, celular, **kwargs):
        if tipo.lower() == 'medico':
            especialidad = kwargs.get('especialidad')
            return Medico(identificacion, nombre, celular, especialidad)
        
        elif tipo.lower() == 'paciente':
            correo = kwargs.get('correo')
            return Paciente(identificacion, nombre, celular, correo)
        
        else:
            raise ValueError(f"Tipo de persona desconocido: {tipo}")