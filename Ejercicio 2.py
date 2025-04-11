from openpyxl import Workbook

libro = Workbook()
hoja = libro.active

hoja.title = "Ventas"

datos = [
    ["Producto", "Cantidad", "Precio"],
    ["Manzanas", 50, 0.5],
    ["Naranjas", 30, 0.75]
]

for indice_fila, fila in enumerate(datos, start=1):
    for indice_col, valor in enumerate(fila, start=1):
        hoja.cell(row=indice_fila, column=indice_col, value=valor)

nombre_archivo = "ventas.xlsx"
libro.save(nombre_archivo)
print(f"Archivo '{nombre_archivo}' creado con éxito.")
