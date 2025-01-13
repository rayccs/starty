import google.generativeai as genai

class Starty:
    def __init__(self):
        self.gemini_api_key = "AIzaSyC2id4JRddrF1vki75tu2YoaKlj1H6iRww"  # Tu API key de Google Gemini
        self.configure_gemini()
        self.conversation_history = []  # Historial de la conversación

    def configure_gemini(self):
        # Configurar la API de Gemini
        genai.configure(api_key=self.gemini_api_key)

    def generate_response(self, user_input):
        # Agregar la entrada del usuario al historial de la conversación
        self.conversation_history.append({"role": "user", "content": user_input})

        # Crear el prompt para Gemini basado en el historial de la conversación
        prompt = self._build_prompt()

        # Configurar el modelo de Gemini
        model = genai.GenerativeModel('gemini-pro')  # Usa el modelo adecuado
        response = model.generate_content(prompt)

        # Agregar la respuesta del agente al historial de la conversación
        self.conversation_history.append({"role": "assistant", "content": response.text})

        return response.text

    def _build_prompt(self):
        # Construir el prompt basado en el historial de la conversación
        prompt = "Eres Starty, un asesor especialista en creación de landing pages. Responde de manera amigable y profesional, como si estuvieras guiando a un cliente. Aquí está el historial de la conversación:\n\n"
        for message in self.conversation_history:
            role = message["role"]
            content = message["content"]
            prompt += f"{role}: {content}\n"
        return prompt