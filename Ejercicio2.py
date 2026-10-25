#Curso: Fundamentos de Tecnología Digitales
#Profesor: Adonis Aleman G.
#Estudiante: Greivin Mora Hidalgo


temperatura = float(input("Ingrese la temperatura del motor en grados Celsisus:"))
presion = float(input("Ingrese la presion hidraulica en PSI:"))
certificado = input("El operador tienecertificacion vigente?:").lower().strip()
horas_trabajo =float(input("ingrese las horas trabajadas del operador:"))

Certificado_ok = certificado == "si"
sin_fatiga = horas_trabajo <= 8
maquina_ok = (temperatura >= 60 and temperatura <= 95) and (presion >= 150 and presion <= 200)

if maquina_ok and Certificado_ok and sin_fatiga:
    estado_motor = "Arranque autorizado"
elif maquina_ok and (not Certificado_ok and sin_fatiga) or (Certificado_ok and not sin_fatiga):
    estado_motor = "Arranque con supervision"
else:
    estado_motor = "Arranque bloquedo"

print(f"Estado del motor: {estado_motor}")