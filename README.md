# TerceraPreEntrega_Rodriguez

La web se accede desde la direccion del server, la cual ya está configurada para que nos lleve a la página de inicio, sin la necesidad de poner la URL '/inicio'. De todas formas se puede hacer y también es funcional.
Si se desea ingresar al panel de admin, el superusuario es admin y la pass admin123.

El proyecto es una web para un local de comidas rápidas. En la barra de menú superior se pueden encontrar 3 links (los 3 funcionales) a **Inicio**, **Carta** y **Hacé tu Pedido**. 
1) **Inicio** lleva a la página de inicio.
2) **Carta** nos da acceso a lo que sería la Carta, donde están integrados los 4 modelos a través de 4 botones. Al ingresar a los mismos nos muestra un read de la base de datos con los productos de la categoría seleccionada. Y debajo nos brinda la opción (a través de su respectivo botón) de **Agregar**, que nos permite agregar productos a la BD. También está la opción de **Buscar**, que nos permite buscar en la BD por el nombre (o incluso por algunas letras) del producto.
3) **Hacé tu Pedido** lleva a un formulario que por el momento no es funcional, pero se pretende que para el proyecto final, sea el Carrito de Compras.

Las URL con las que cuenta el proyecto son las siguientes (copio y pego desde urls.py):

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

    #URLs para buscar elementos
    path('buscarComida/', buscarComida, name='Buscar Comida'),
    path('resultadosComida/', resultadosComida, name='Resultados Comida'),
    path('buscarBebida/', buscarBebida, name='Buscar Bebida'),
    path('resultadosBebida/', resultadosBebida, name='Resultados Bebida'),
    path('buscarGuarnicion/', buscarGuarnicion, name='Buscar Guarnicion'),
    path('resultadosGuarnicion/', resultadosGuarnicion, name='Resultados Guarnicion'),
    path('buscarPostre/', buscarPostre, name='Buscar Postre'),
    path('resultadosPostre/', resultadosPostre, name='Resultados Postre'),

    

