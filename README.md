# URBAN ROUTES
<p>
Urban Routes es una aplicación web de servicios de taxi que permite a los usuarios solicitar viajes de manera sencilla e intuitiva. La aplicación ofrece funcionalidades completas para la gestión de viajes urbanos.

**Características principales:**
🚗 Servicios de Taxi:

Configuración de rutas (origen y destino)
Selección de diferentes tarifas (Comfort, etc.)
Solicitud y búsqueda automática de conductores
💳 Gestión de Pagos:

Registro de números de teléfono
Integración de tarjetas de crédito con validación CVV
Confirmación por código SMS
🛠️ Servicios Adicionales:

Mensajes personalizados para conductores
Solicitud de extras (mantas, pañuelos)
Pedido de productos adicionales (helados)
Información en tiempo real del conductor asignado

La aplicación está diseñada para proporcionar una experiencia completa y fluida en la solicitud de servicios de transporte urbano.

</p>

##🔧 Tecnologías y Herramientas Utilizadas:
**Selenium WebDriver**
Automatización de pruebas web
**Python**
Lenguaje de programación
**Pytest**
Framework de pruebas
**Chrome WebDriver**
Navegador para ejecución de pruebas

##📋 Funcionalidades Probadas:
**Configuración de Rutas:**

- Ingreso de direcciones "Desde" y "Hasta"
- Validación de campos de origen y destino
- Cálculo automático de rutas

** Selección de Tarifas:**
- Selección de tarifa "Comfort"
- Verificación de precios y tiempos estimados
- Funcionalidad de botones de tarifa

**Gestión de Métodos de Pago:**
- Registro y validación de números de teléfono
- Agregado de tarjetas de crédito
- Validación de campos CVV
- Confirmación por código SMS

**Servicios Adicionales:**

- Envío de mensajes personalizados al conductor
- Solicitud de extras (mantas, pañuelos)
- Pedido de productos adicionales (helados)

**Proceso de Solicitud de Taxi:**

- Búsqueda y asignación de conductores
- Modal de búsqueda de taxi
- Información del conductor asignado
- Flujo completo de solicitud de servicio


##🎯 Tipos de Pruebas Implementadas:
- Pruebas de Interfaz de Usuario (UI)
- Pruebas de Funcionalidad
- Pruebas de Integración
- Pruebas de Flujo de Usuario End-to-End


📊 Cobertura de Pruebas:
- Interacción con elementos de formulario
- Validación de campos obligatorios
- Flujos de navegación entre pantallas
- Manejo de modales y ventanas emergentes
- Verificación de estados de botones y elementos

##Framework
<p>
Este proyecto implementa un framework de automatización de pruebas basado en el patrón Page Object Model (POM) 
El framework está desarrollado en Python utilizando Selenium WebDriver y pytest como herramienta de ejecución de pruebas.
</p>

<p>

📁 **Pages/**
Contiene los objetos de página
📁 **Helpers/utilities/**
Incluye funciones auxiliares y utilidades reutilizables
📁 **Data/**
Almacena los datos de prueba utilizados en los casos de prueba
📁 **Tests/**
Contiene los casos de prueba organizados por funcionalidad
<p>

##Instalación⚙️


####Clonar Repositorio
> git clone https://github.com/usuario/qa-project-Urban-Routes-es.git

#### Instalar dependencias
> pip install -r requirements.txt

#### Ejecución de pruebas
> pytest .\test\TestUrbanRoutes.py






