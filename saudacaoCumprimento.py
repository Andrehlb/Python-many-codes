from datetime import datetime

def saudacao():
    hora = datetime.now().hour
    if hora < 12:
        return "Bom dia!"
    elif hora < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"
    
    return f"{saudacao}, "

print(saudacao('Coders da Ada Tech | Santander'))
