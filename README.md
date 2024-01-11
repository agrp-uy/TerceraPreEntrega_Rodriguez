# TerceraPreEntrega_Rodriguez

La web se accede desde la direccion del server, la cual ya está configurada para que nos lleve a la página de inicio, sin la necesidad de poner la URL '/inicio'. De todas formas se puede hacer y también es funcional.
Si se desea ingresar al panel de admin, el superusuario es admin y la pass admin123.

El proyecto trata sobre un Foodtruck. En la barra de menú superior se pueden encontrar 3 links (los 3 funcionales) a **Inicio**, **Carta** y **Hacé tu Pedido**. 
1) **Inicio** lleva a la página de inicio.
2) **Carta** nos da acceso a lo que sería la Carta, donde están integrados los 4 modelos a través de 4 botones. Al ingresar a los mismos se accede al read de la base de datos. Y debajo nos brinda la opción (a través de su respectivo botón) de **Agregar**.
3) **Hacé tu Pedido** lleva a un formulario que, para el proyecto final, será el Carrito de Compras.

Las URL con las que cuenta el proyecto al momento son las siguientes (copio y pego desde urls.py):

    path('admin/', admin.site.urls),

    #URLs de la app
    path('', inicio, name='Inicio'),
    path('inicio/', inicio, name='Inicio'),
    path('carta/', carta, name='Carta'),
    path('pedido/', pedido, name='Pedido'),

    #URLs de los modelos creados
    path('comida/', comida, name='Comidas'),
    path('bebida/', bebida, name='Bebidas'),
    path('guarnicion/', guarnicion, name='Guarniciones'),
    path('postre/', postre, name='Postres'),

    #URLs para agregar elementos
    path('agregarComida/', agregarComida, name='Agregar Comida'),
    path('agregarBebida/', agregarBebida, name='Agregar Bebida'),
    path('agregarGuarnicion/', agregarGuarnicion, name='Agregar Guarnicion'),
    path('agregarPostre/', agregarPostre, name='Agregar Postre'),

    

