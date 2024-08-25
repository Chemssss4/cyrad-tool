# par pitié ne pas volé mon code et ne rien modiffié svp sah

import base64

async def run():
    """Fonction principale pour convertir un ID en base64."""

    user_id = input("Veuillez entrer l'ID utilisateur : ")


    user_id_bytes = user_id.encode('utf-8')


    base64_encoded = base64.b64encode(user_id_bytes)


    base64_message = base64_encoded.decode('utf-8')


    print(f"La premiere partie du token de l'utilisateur est : {base64_message}")
