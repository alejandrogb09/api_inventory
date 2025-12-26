# Inventory API

API REST para gestión de productos e inventario basada en movimientos como única fuente de verdad.

Construida con Django REST Framework, pensada como backend reutilizable para sistemas de:
- inventarios
- pedidos
- agenda
- automatizaciones y scripts

---

## 🧠 Concepto clave

El stock **no se modifica directamente**.

Toda variación se registra mediante **movimientos**:
- entradas
- salidas

Esto garantiza:
- historial inmutable
- trazabilidad
- consistencia de datos

---

## ⚙️ Tecnologías

- Python
- Django
- Django REST Framework
- Autenticación por Token (DRF)

---

## 📦 Modelos principales

### Product
- nombre
- precio
- stock (derivado de movimientos)
- activo / inactivo

### Movement
- producto
- tipo (IN / OUT)
- cantidad
- fecha

---

## 🔐 Autenticación

La API utiliza **Token Authentication**.

Todos los endpoints requieren autenticación.

---

## 🔗 Endpoints principales

### Productos
- `GET /api/products/`
- `POST /api/products/`
- `PUT /api/products/{id}/`
- `DELETE /api/products/{id}/`

### Movimientos
- `GET /api/movements/`
- `POST /api/movements/`

> No se permiten actualizaciones ni eliminaciones de movimientos para proteger el historial.

---

## 🧪 Pruebas

Los endpoints fueron probados usando **Postman**:
- creación de productos
- entradas y salidas
- validación de stock insuficiente
- autenticación por token

---

## 🚀 Estado del proyecto

- API funcional
- Lógica de negocio implementada
- Lista para:
  - despliegue
  - consumo desde frontend
  - automatización con scripts Python
