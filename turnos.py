import uuid
import json


class Turno(json.JSONEncoder):

    def __init__(self, dni_cliente, especialidad_medica, fecha, estado, nombre_medico):
        self.dni_cliente = dni_cliente
        self.especialidad_medica = especialidad_medica
        self.fecha = fecha
        self.estado = estado
        self.nombre_medico = nombre_medico
        self.turno_id = str(uuid.uuid4())

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def guardar_en_archivo(self, turno):
        archivo = open(f"./data/{self.turno_id}.json", "w")
        archivo.write(str(turno.toJSON()))

    def estado_de_turno(self):
        if self.estado == "CONFIRMADO":
            print("El turno fue confirmado")
        else:
            print("El turno no fue confirmado")
