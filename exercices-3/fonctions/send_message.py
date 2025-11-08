messages = [
    "Bonjour tout le monde!", 
            "Bienvenue dans le monde de Python.", 
            "Apprendre à programmer est amusant!", 
            "Les fonctions rendent le code réutilisable."
            ]
sent_messages = []
def send_messages(messages_list):
    
    messages_list.reverse()
    while messages_list:
        message = messages_list.pop()
        print(message)
        sent_messages.append(message)

send_messages(messages[:])
print(messages)
print(sent_messages)