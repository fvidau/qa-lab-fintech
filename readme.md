# 🧪 QA Fintech Lab – Automation Portfolio

Repositorio de automatización QA que cubre **testing de APIs + testing UI** aplicados a un contexto fintech.  
El objetivo es demostrar habilidades reales de un QA moderno: validación de backend + automatización de frontend con arquitectura escalable.

---

# 🚀 Alcance del proyecto

El proyecto se divide en dos grandes áreas:

## 1. 🔌 API Testing (Fintech)

Pruebas automatizadas sobre servicios tipo fintech (simulación de transacciones, validaciones y lógica backend).

### ✔️ Qué valida

- Creación de datos
- Validación de respuestas
- Integridad de datos
- Casos negativos
- Lógica de negocio

### 📁 Ubicación
automation/tests/
├── test_transactions.py
├── test_negativos.py
└── conftest.py

---

## 2. 🌐 UI Testing (Playwright)

Automatización de interfaz usando Playwright + Pytest con patrón Page Object Model.

### ✔️ Caso de prueba implementado

Flujo automatizado:

1. Navegar a DuckDuckGo  
2. Realizar una búsqueda  
3. Esperar resultados  
4. Validar resultados visibles  

👉 Se utiliza DuckDuckGo en lugar de Google para evitar bloqueos por detección de bots.

---

# 🧱 Tecnologías utilizadas

- Python 3.13  
- Pytest  
- Playwright  
- Requests (API testing)  
- Page Object Model (POM)  

---

# 📁 Estructura del proyecto
QA-LAB/
│
├── automation/
│ └── tests/
│ ├── test_transactions.py
│ ├── test_negativos.py
│ └── conftest.py
│
├── playwright-ui/
│ ├── pages/
│ │ └── google_page.py
│ │
│ ├── tests/
│ │ ├── test_google.py
│ │ └── conftest.py
│
├── config.py
├── db.json
└── README.md

---

# 🧠 Arquitectura

## 🔹 API Testing

- Uso de Pytest para ejecución
- Separación de lógica de test y datos
- Validaciones sobre responses JSON

## 🔹 UI Testing (POM)

Se implementa **Page Object Model** para mantener el código limpio y escalable:

- `pages/` → interacción con UI  
- `tests/` → lógica de validación  

Ejemplo:

```python
google = GooglePage(page)
google.go_to_google()
google.search("Playwright Python")
google.wait_for_results()