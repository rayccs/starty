import os

# Definir la estructura del proyecto
project_structure = {
    "app": {
        "__init__.py": "",
        "main.py": "# Punto de entrada del microservicio\n",
        "agent.py": "# Lógica del agente de IA\n",
        "questions.py": "# Preguntas predefinidas\n",
        "templates": {}
    },
    "requirements.txt": "# Dependencias del proyecto\nFlask==2.3.2\nopenai==0.27.0\n",
    "Dockerfile": "# Para containerizar el microservicio\n",
    "README.md": "# Documentación del proyecto\n"
}

# Función para crear directorios y archivos
def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)

# Ruta base donde se creará el proyecto
base_path = "landing_page_agent"

# Crear la estructura del proyecto
create_project_structure(base_path, project_structure)

print(f"Proyecto generado en: {os.path.abspath(base_path)}")