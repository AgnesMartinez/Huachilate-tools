# Huachilate-tools
Sistema de rifa automatizado para subforos

¿Como funciona?
- - - - - - - - - - - - - -

Se requiere del huachicore, core bancario para realizar movimientos y consultar la huachiclave de la rifa vigente, o generar una nueva en caso necesario.

La huachiclave es un string alfanumerico de 7 caracteres, como un uuid, es generada por el huachicore, mientras exista una activa, no se genera una nueva.

Se genera un monto especifico asociado a la huachiclave, la idea es acumular esa cantidad en la huachicuenta, un numero al azar entre 5k y 50k.

huachilate()
- - - - - - - - - - - - - 

Funcion usada por el empleado para comprar un boletito de huachilate y agregarlo a la tabla boletitos, en la base de datos, el registro de la tabla es el siguiente:

Timestamp | Usuario | huachiclave

Posterior a la compra del huachilate, el empleado verifica si el saldo de la huachicuenta ya llego o rebaso el monto especifico de la rifa, en caso de cumplirse esa condicion, ejecuta la funcion premio_huachilate()

premio_huachilate()
- - - - - - - - - - - - -
Al ser llamada, obtiene la lista de boletitos comprados con la huachiclave vigente, elige 3 usuarios al azar y reparte premios en el siguiente orden:

Primer lugar =  50% de la huachicuenta

Segundo lugar = 30% de la huachicuenta

Tercer lugar = 20% de la huachicuenta

Entrega el dinero a los ganadores, posteriormente publica la lista de ganadores en el subforo.

cambia la columna entregado en huachilate por 1.

La proxima rifa inicia en cuanto se compra el siguiente boletito, el huachicore genera una nueva huachiclave con su monto especifico.

rinse and repeat.