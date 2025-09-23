notas_perez = [5, 4, 7, 2, 8, 9, 9, 4, 6, 7, 8, 2]
notas_suarez = [2, 4, 3, 10, 8, 9, 5, 4, 6, 4, 8, 2]

for i in range(len(notas_perez)):

    if notas_perez[i] < 6:
        print(f"Perez aún no aprobó la materia {i}")