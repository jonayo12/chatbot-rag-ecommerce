from rag import cargar_documentos, crear_vectorstore, crear_cadena_rag

def main():
    print("Cargando documentos...")
    documentos = cargar_documentos("../docs")

    print(f"Documentos encontrados: {len(documentos)}")
    print(documentos)

    print("Creando vectorstore...")
    vectorstore = crear_vectorstore(documentos)

    print("Inicializando chatbot...\n")
    cadena = crear_cadena_rag(vectorstore)

    print("¡Chatbot listo! Escribe 'salir' para terminar.\n")

    while True:
        pregunta = input("Tu pregunta: ")
        if pregunta.lower() == "salir":
            break

        respuesta = cadena.invoke(pregunta)
        print(f"\nRespuesta: {respuesta}\n")

if __name__ == "__main__":
    main()