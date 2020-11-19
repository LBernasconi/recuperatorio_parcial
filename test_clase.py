from turnos import Turno
import json


def test_creacion_archivo():
    turno_a = Turno(55990339, "PEDIATRIA", "30 - 11 - 2020", "CONFIRMADO", "Ruiz")
    transaccion_b = Turno(45990339, "OFTALMOLOGIA", "05 - 12 - 2020", "PENDIENTE", "Ortega")

    turno_a.guardar_en_archivo(turno_a)
    transaccion_b.guardar_en_archivo(transaccion_b)


def test_estado_turno():
    turno_a = Turno(45990339, "OBSTETRICIA", "10 - 12 - 2020", "PENDIENTE", "Arena")
    turno_a.estado_de_turno()


def test_json_turno():
    turno_a = Turno(30949303, "ODONTOLOGÍA", "31 - 11 - 2020", "CONFIRMADO", "Rossi")
    turno_to_dict = json.loads(turno_a.toJSON())

    print("Las keys del diccionario son: ", turno_to_dict.keys())
    print("Los items del diccionario son: ", dict(turno_to_dict.items()))
    print("El valor de la key 'especialidad medica' es: ", turno_to_dict["especialidad_medica"])


test_creacion_archivo()
test_estado_turno()
test_json_turno()
