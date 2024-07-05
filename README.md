## 👋 ¡Hola, soy Nicolás! Analista de datos de Colombia 🇨🇴. ¡En este escenario vamos a estar revisando un caso de una empresa brasileña que tiene un problema con las entregas!
### Vamos a averiguar por qué!

Utilizamos las siguietes librerias:

- 🐼 PANDAS
- 📏 MATPLOTLIP
- 🌊 SEABORN
- 💣 PLOTY
- 📝 REPORTLAB

Algunas otras que nos son de ayuda ( OS & JSON)

El notebook 📑 https://drive.google.com/file/d/16dNwyTIjXHQv_huVnkGJCt_lvacFNnfW/view?usp=drive_link

La data 📦 https://drive.google.com/file/d/1U4lal8Ztw1lQmukoZN2vDaFgPVc1DWuq/view?usp=drive_link

### La idea

---

- La ides es empezar a tener el ritmo de las librerias de python, que ayudan a modelar datos empezando por los mas faciles los CSV

### Problemas

---

- ⚠️ La idea era utilizar Jupter desde chorme pero se me dificulto entonces voy a utilizar VSC = Visual Studio Code, estoy mas familiarizado con esta: para colocar la ruta de la carpeta pongo una ‘r’ antes de la ruta para que entienda que es un path, todo se soluciono corrigiendo las rutas del PATH
⚠️ Hay otro problema, es que habia una ruta repetida, ademas se soluciono el problema con el motor ‘engine=openpyxl’

en el siguiente codigo subplots tiene que importar la libreria matplotlib.pyplot para pdoer funcionar si importas matplotlib, en mi caso no funciono

```python
import matplotlib.pyplot as plt

# figura y eje de la figura
fig, ax = plt.subplots(figsize=(10, 5))
```

---

⚠️ La regla empirica debil que nos permite relacionar los datos junto con la media y la desviacion estandar 

### Crear un historiograma de la frecuencia de ventas totales

- Este es el primer intento donde utilizo codigo dado en el 📒 asi que reemplazo los valores y asi termino

```
python
import matplotlib.pyplot as plt

# figura y eje de la figura
fig, ax = plt.subplots(figsize=(10, 5))

# numero de intervalos para conteos
n_bins = 100

# creacion del objeto historgama
n, bins, patches = ax.hist(
    processed['total_sales'],
    n_bins
    )

ax.set_title('Fig.2 Histograma de frequencias de total_sales y regla empírica débil de todas las ordenes' )
ax.set_xlabel('Ventas totales')
ax.set_ylabel('# Ocurrencias')

## Agrega la media y las regiones de la regla empírica débil
## Linea para la media
plt.axvline(
    processed['total_sales'].mean(),
    color='r',
    linestyle='dashed',
    linewidth=3)

## Linea para la media + 3 veces la desv. estandar
plt.axvline(
    processed['total_sales'].mean() + 3*processed['total_sales'].std(),
    color='y',
    linestyle='dashed',
    linewidth=2)

## Linea para la media - 3 veces la desv. estandar
plt.axvline(
    processed['total_sales'].mean() - 3*processed['total_sales'].std(),
    color='y',
    linestyle='dashed',
    linewidth=2)

## limites de la figura
min_ylim, max_ylim = plt.ylim()

## Etiquetas
plt.text(
    processed['total_sales'].mean()*1.1,
    max_ylim*0.9,
    'Promedio: {:.2f}'.format(processed['total_sales'].mean())
    )

plt.show()
```

![image](https://github.com/NicoJSuarez2/OILIST/assets/174117595/ac3bfd99-0428-4aaa-8a8f-a1ce99802be1)


### Comparación

Aqui utilizo otro codigo que no esta en el 📒 para ver si el  resultado es comparable, 


## Problemas

⚠️ EL .iloc[cordenadas de los datos] Siempre me salva a la hora de hacer un print de un dato especifico, aunque, creo que se podria mejorar por medio de una función para no tener que buscar la coordenada del dato especifico 

⚠️ En el entregable 3_d, el nombre dice que es por .region, pero en la descripcion del scrip no menciona hacerlo con la region… ⁉️

## Aprendizajes

📘 Ploty es una herramienta que viene de un API que tiene una forma de escritura parecida a 🌊seaborn🌊

📘 siempre que utilices un groupby tienes que ponerle una operaciones sino el resultado sera <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000024FE56C5120>

📘 Para lograr hacer la escala de color hay que darse cuenta de que el tipo de dato de la columna color = ‘delay_status’ debe ser  un “int”



⚠️La libreria Scipy, es textual: ‘ A scientific computing package for Python’ hay que seguir trabajand con ella para aprender a manejarla de forma completa, en esta ocacion utilizamos el KERNEL GAUSSIANO, nos ayuda a encontrar la probabilidad.
