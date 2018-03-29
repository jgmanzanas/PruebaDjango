# Prueba Django

## Docker Compose
Ejecutar los siguientes comandos en orden desde el path del proyecto
```Terminal
docker-compose build
docker-composer run web
docker-compose up
```

##Prueba

No lo he subido porque no tenia claro que hacer, pero el archivo test.xml el enlace debe de estar en la carpeta del proyecto para que funcione

He dividido la prueba de Django en 3 metodos: 
* Ordenacion por Precios descendentes(20 productos). URL -> http://localhost:8000/order/price
* Ordenacion por Descuento descendente(20 productos). Este incluye el punto 2 y el 3 porque no he entendido muy bien la diferencia entre ellos. URL -> http://localhost:8000/order/discount 
* Productos con product_type "Comedy" URL -> http://localhost:8000/order/comedy
 