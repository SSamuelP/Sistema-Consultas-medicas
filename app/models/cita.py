class Cita:
    def __init__(self, paciente, medico, fecha, motivo_cancelacion=None):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.motivo_cancelacion = motivo_cancelacion

    def recordatorio_cita(self):
        print(f"Enviando notificación al paciente {self.paciente.nombre}")

    def reprogramar_cita(self, nueva_fecha):
        if self.medico.verificar_disponibilidad(nueva_fecha):
            print(f"Cita reprogramada del {self.fecha} al {nueva_fecha}")
            self.fecha = nueva_fecha
        else:
            print(f"No hay disponibilidad para reprogramar la cita en la fecha {nueva_fecha}")

    def cancelar_cita(self, motivo):
        self.motivo_cancelacion = motivo
        print(f"La cita ha sido cancelada por {self.paciente.nombre}, debido a: {self.motivo_cancelacion}")