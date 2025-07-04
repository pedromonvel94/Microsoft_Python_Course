Actividad: Trabajar con una lista
Escenario

Imagínese que va al supermercado, pero se le olvidan constantemente los productos que necesita. Es frustrante y te obliga a hacer varias veces la compra ¿No sería estupendo contar con un ayudante digital que te ayudara a hacer la lista de la compra? 

Aquí es donde entra Python. Construirás un sencillo programa que te permitirá añadir artículos a tu lista de la compra virtual, cargar artículos desde un Archivo CSV y gestionar tu lista de la compra de forma eficiente. Se acabaron los huevos y la leche olvidados

Objetivo

El objetivo de esta actividad es introducirte en la aplicación práctica de las listas de Python, que son como contenedores ordenados que almacenan colecciones de elementos. Aprenderás a crear, manipular e interactuar con listas, adquiriendo experiencia práctica con conceptos esenciales de programación. Verás cómo las listas son perfectas para hacer la compra porque mantienen el orden de los elementos, te permiten añadir o quitar cosas fácilmente según sea necesario, e incluso pueden almacenar diferentes tipos de información (como nombres de elementos y cantidades). 

Utilizará acciones especiales denominadas métodos, como append() y remove(), para gestionar eficazmente su lista. Además, explorarás cómo cargar datos de archivos externos, como Valores separados por comas (CSV) en tu programa Python, ampliando aún más tus capacidades de manejo de datos. Al final de esta actividad, tendrás una lista de la compra digital funcional y una base sólida en el trabajo con listas, una estructura de datos fundamental en Python.

Al final de esta actividad, responderás a las preguntas del cuestionario para recibir una calificación por esta actividad. No será necesario que envíes ningún archivo.

Instrucciones

Descarga PYTC1M2P01_Activity_Workingwithalist.zip y guárdalo en el escritorio de tu máquina y extráelo a una carpeta donde sea fácilmente accesible. Ten en cuenta que este archivo ZIP contiene varios archivos, por lo que debes extraerlo. Si simplemente "abres" el Notebook de Jupyter, puedes obtener un error.

Paso 1: Cargar su Lista Inicial de Comestibles desde un Archivo CSV

Empecemos cargando su lista de la compra desde un Archivo CSV (Valores separados por coma). Piense en un archivo CSV como una simple hoja de cálculo en la que cada fila representa un elemento de su lista. Utilizaremos la biblioteca pandas, una potente herramienta para trabajar con datos en Python, para leer el archivo CSV y extraer los elementos en una lista de Python.

Ya se ha proporcionado un Archivo CSV ('lista_de_comestibles.csv') que contiene un conjunto inicial de artículos. No necesitas cambiar el código para esto.

El código necesario para importar la librería pandas, cargar el Archivo CSV, y extraer su contenido en una lista Python llamada grocery_list también está presente. Tampoco necesitarás cambiar este código. Volverás a ver la librería pandas en un curso futuro.

Simplemente ejecute la celda para imprimir el contenido de grocery_list y observe la salida.

Deberías ver una lista de comestibles.

Si recibe el siguiente error:

Error: The file 'grocery_list.csv' was not found in the current directory. 

Asegúrese de haber extraído el contenido de la carpeta ZIP como se indica más arriba.