from openpyxl import Workbook

libro = Workbook()
pagina = libro.active

hoja_datos = libro.create_sheet("Datos")

libro.save("mi_libro.xlsx")

print("Archivo 'mi_libro.xlsx' creado con una hoja llamada 'Datos'")
