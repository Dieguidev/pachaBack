Proceso Reloj
	
	hora=0
	minuto=0
	segundo=0
	
	Escribir "Ingrese la hora (formato 24 horas): "
	Leer hora
	
	Escribir "Ingrese los minutos: "
	Leer minuto
	
	Escribir "Ingrese los segundos: "
	Leer segundo
	
	segundo = segundo + 1
	
	Si segundo == 60 Entonces
		segundo = 0
		minuto = minuto + 1
		Si minuto == 60 Entonces
			minuto = 0
			hora = hora + 1
			Si hora == 24 Entonces
				hora = 0
			FinSi
		FinSi
	FinSi
	
	Escribir "La nueva hora es: ", hora, ":", minuto, ":", segundo
FinProceso
