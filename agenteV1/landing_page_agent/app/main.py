from flask import Flask, request, jsonify
from agent import Starty

app = Flask(__name__)
starty = Starty()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "El campo 'message' es requerido."}), 400

    # Generar una respuesta usando Starty
    response = starty.generate_response(user_input)
    return jsonify({"response": response})

def start_cli():
    print("Bienvenido a Starty, tu asesor especialista en landing pages. Escribe 'salir' para terminar la conversación.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Starty: ¡Gracias por usar el servicio! Hasta luego.")
            break

        # Enviar el mensaje a Starty
        response = starty.generate_response(user_input)
        print(f"Starty: {response}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        start_cli()
    else:
        app.run(host='0.0.0.0', port=5000)