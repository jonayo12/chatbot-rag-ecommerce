# 🤖 Chatbot RAG para Ecommerce

Chatbot de atención al cliente construido con RAG (Retrieval Augmented Generation) que responde preguntas usando los documentos propios de la empresa, sin inventar información.

## 🌐 Demo en vivo
👉 [Probar el chatbot](https://chatbot-rag-ecommerce-zfzs5xqsawlcba2gqyumso.streamlit.app)

## 🎯 Problema que resuelve

Las tiendas online reciben cientos de preguntas repetitivas cada día sobre precios, disponibilidad y políticas. Este chatbot las responde automáticamente 24/7, reduciendo la carga del equipo de atención al cliente.

## 🏗️ Arquitectura
Usuario pregunta
↓
Embedding de la pregunta (OpenAI)
↓
ChromaDB busca fragmentos relevantes
↓
GPT-4 responde usando ese contexto
↓
Respuesta precisa sin alucinaciones

## 🛠️ Stack tecnológico

- **LangChain** → pipeline RAG
- **OpenAI GPT-4** → modelo de lenguaje
- **ChromaDB** → base de datos vectorial
- **Streamlit** → interfaz web
- **Python 3.12**

## 🚀 Cómo ejecutarlo

1. Clona el repositorio
```bash
git clone https://github.com/jonayo12/chatbot-rag-ecommerce.git
cd chatbot-rag-ecommerce
```

2. Crea el entorno virtual e instala dependencias
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Configura tu API key
```bash
cp .env.example .env
# Edita .env y añade tu OPENAI_API_KEY
```

4. Añade tus documentos en la carpeta `docs/` en formato `.txt`

5. Lanza la aplicación
```bash
cd src
streamlit run app.py
```

## 📂 Estructura del proyecto
📁 chatbot-rag-ecommerce
├── 📁 src/
│ ├── app.py ← interfaz Streamlit
│ ├── rag.py ← lógica RAG
│ └── main.py ← versión terminal
├── 📁 docs/ ← documentos de la empresa
├── 📄 .env.example
├── 📄 requirements.txt
└── 📄 README.md

## 💡 Casos de uso

- Atención al cliente en ecommerce
- Chatbot interno para RRHH con políticas de empresa
- Asistente para equipos de ventas con catálogos de productos
- Soporte técnico con documentación de producto