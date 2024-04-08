import re
import random

class RuleBot:
    negative_responses = ("no", "nope", "nah", "claro que no", "lo siento", "perdona")
    exit_commands = ("adios", "nos vemos, gracias", "no quiero nada mas", "Chao", "bye", "para", )

    def __init__(self):
        self.alienable = {
                          'orientation_intent': r'.*\s*orientacion vocal mas afin a mi.*',
                          'demand_intent': r'.*\s*carrera mas demandada.*',
                          'info_intent': r'.*\s*informacion de las carreras ofertadas.*'
                          }

    def greet(self):
        will_help = "Bienvenido! soy Nige, tu orientador vocacional virtual personalizado. Sobre qué quieres hablar? \n"
        if will_help in self.negative_responses:
            print("Bueno, ten un buen dia!")
            return
        return will_help


    def make_exit(self, reply):
        for command in self.exit_commands:
            if command in reply:
                print("Bueno, ten un buen dia")
                return True

    def match_reply(self, reply):
        for key, value in self.alienable.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)

            if found_match and intent == 'orientation_intent':
                return self.orientation()
            elif found_match and intent == 'demand_intent':
                return self.demand()
            elif found_match and intent == 'info_intent':
                return self.info()
        if not found_match:
            return self.no_match_intent()


    def orientation(self):
        response = ("¡Perfecto! Hagamos un test para saber tus preferencias y habilidades para brindarte una propuesta de formación más personalizada\n")
        return response

    def demand(self):
        response = ("Te presento las carreras que ofertamos actualmente, ¿Cual quieres consultar primero?\n")
        return response

    def info(self):
        response = ("Te presento las carreras que ofertamos actualmente, ¿Cual quieres consultar primero?\n")
        return response


    def no_match_intent(self):
        responses = ("Hablame mas. \n ",
                     "Y que mas quieres conocer \n")
        return random.choice(responses)

