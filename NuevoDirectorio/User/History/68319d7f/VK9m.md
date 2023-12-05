# Principios de la Arquitectura REST

La **Arquitectura de Transferencia de Estado Representacional (REST)** es un estilo arquitectónico utilizado en el diseño de sistemas distribuidos y aplicaciones web. Los principios fundamentales de la arquitectura REST se basan en la simplicidad, la escalabilidad y la interoperabilidad. A continuación, se describen los principales principios o restricciones de la arquitectura REST:

## 1. Arquitectura Cliente-Servidor

REST sigue el principio de separación de preocupaciones, dividiendo la aplicación en dos componentes independientes: el cliente y el servidor. Esto permite la evolución independiente de ambos, facilita la escalabilidad y mejora la reutilización de componentes.

## 2. Sin Estado (Statelessness)

Cada solicitud del cliente al servidor debe contener toda la información necesaria para comprender y procesar la solicitud. El servidor no debe almacenar información sobre el estado del cliente entre las solicitudes. Esto simplifica la implementación, mejora la escalabilidad y facilita la tolerancia a fallos.

## 3. Interfaz Uniforme

REST define una interfaz uniforme que simplifica la arquitectura y mejora la interoperabilidad. Esta interfaz consta de cuatro restricciones clave:

- **Identificación de Recursos:** Cada recurso debe tener un identificador único (URI).
  
- **Manipulación de Recursos a través de Representaciones:** Los recursos se manipulan a través de representaciones, que pueden ser en formato XML, JSON, HTML, entre otros.
  
- **Autodescriptivo (HATEOAS):** El servidor proporciona enlaces de hipertexto en las respuestas, permitiendo que el cliente navegue por la aplicación de manera dinámica.
  
- **Operaciones Limitadas (GET, POST, PUT, DELETE):** Las acciones realizadas sobre los recursos se limitan a un conjunto pequeño y uniforme de operaciones estándar.

## 4. Sistema en Capas (Layered System)

La arquitectura REST permite la construcción de sistemas en capas, donde cada componente (capa) realiza una función específica. Esto promueve la escalabilidad, ya que cada capa puede ser escalada de forma independiente, y facilita la implementación de la seguridad y el rendimiento.

## 5. Cacheabilidad

Las respuestas del servidor deben indicar si los datos son o no cacheables. El uso eficiente de la caché mejora la eficiencia de la red y la velocidad de acceso a los recursos.

## 6. Sistema de Código por Demanda (Optional)

Este es un principio opcional que permite al servidor enviar código ejecutable al cliente. Aunque no es ampliamente utilizado, brinda flexibilidad en la extensibilidad del cliente.

Estos principios de la arquitectura REST proporcionan una guía sólida para el diseño de sistemas distribuidos eficientes y escalables, priorizando la simplicidad y la interoperabilidad.