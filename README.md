1. Caso de Prueba: Creación de un Libro

Objetivo: Verificar que un libro se pueda crear correctamente con todos los campos obligatorios.

    Precondiciones: El módulo de gestión de librería está instalado.
    Pasos:
        Navega al menú Bookstore > Books.
        Haz clic en "Crear".
        Introduce el título del libro, selecciona un autor, ingresa la fecha de publicación, ISBN, precio y cantidad en stock.
        Guarda el registro.
    Resultado Esperado: El libro se guarda correctamente, y todos los campos obligatorios se completan.

2. Caso de Prueba: Creación de una Orden de Venta con un Libro

Objetivo: Verificar que un libro se pueda añadir a una línea de pedido en una orden de venta.

    Precondiciones: Existen libros y clientes creados.
    Pasos:
        Navega al menú Sales > Orders.
        Haz clic en "Crear".
        Selecciona un cliente.
        En las líneas de pedido, selecciona un libro de la lista de productos.
        Introduce la cantidad y precio del libro.
        Guarda la orden.
    Resultado Esperado: La orden de venta se guarda correctamente y el libro se vincula a la línea de pedido.

3. Caso de Prueba: Actualización Automática de Inventario tras una Venta

Objetivo: Verificar que la cantidad en stock de un libro se reduce automáticamente tras confirmar una venta.

    Precondiciones: Existe un libro con una cantidad en stock específica y una orden de venta creada con ese libro.
    Pasos:
        Navega al menú Sales > Orders.
        Abre la orden de venta creada anteriormente.
        Confirma la venta.
        Navega al menú Bookstore > Books.
        Revisa la cantidad en stock del libro vendido.
    Resultado Esperado: La cantidad en stock del libro se reduce por la cantidad vendida.

4. Caso de Prueba: Registro de Historial de Compras del Cliente

Objetivo: Verificar que las compras de un cliente se registran correctamente en su historial de compras.

    Precondiciones: Existen clientes y libros, y se ha creado una orden de venta para un cliente.
    Pasos:
        Navega al menú Sales > Orders.
        Abre la orden de venta creada para el cliente.
        Confirma la venta.
        Navega al menú Bookstore > Customers.
        Abre el registro del cliente asociado.
        Verifica el historial de compras.
    Resultado Esperado: El historial de compras del cliente muestra la orden de venta y los libros adquiridos.

5. Caso de Prueba: Acceso Restringido para Usuarios no Autorizados

Objetivo: Verificar que los usuarios sin permisos de gestión de inventario no puedan acceder a la gestión de libros.

    Precondiciones: Existen roles de usuario configurados.
    Pasos:
        Inicia sesión con un usuario que no tenga permisos de gestión de inventario.
        Intenta acceder al menú Bookstore > Books.
    Resultado Esperado: El usuario recibe un mensaje de acceso denegado o no puede ver la opción en el menú.

6. Caso de Prueba: Visualización en el Tablero de Control

Objetivo: Verificar que el tablero de control muestre los niveles de stock y las ventas recientes.

    Precondiciones: Se han realizado ventas de libros.
    Pasos:
        Navega al menú Bookstore > Dashboard.
        Revisa los widgets y gráficos que muestran el estado de inventario y ventas recientes.
    Resultado Esperado: El tablero muestra datos actualizados de los niveles de stock y las ventas recientes de libros.

7. Caso de Prueba: Edición de un Libro

Objetivo: Verificar que un libro existente se pueda editar y que los cambios se guarden correctamente.

    Precondiciones: Existe un libro creado.
    Pasos:
        Navega al menú Bookstore > Books.
        Abre un registro de libro existente.
        Edita uno o más campos (por ejemplo, cambia el precio o la cantidad en stock).
        Guarda los cambios.
    Resultado Esperado: Los cambios se guardan correctamente y se reflejan al volver a abrir el registro.
