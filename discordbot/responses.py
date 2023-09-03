import random

def get_response(message: str) -> str:
    p_mesage = message.lower()

    if p_mesage =='Leo':
        return 'Leo esta ahora mismo lavando ropa '
    
    if p_mesage =='Brayan':
        return 'Esta estudiando OK #sad'
    
    if p_mesage =='Shax':
        return 'Regalando wins a Daniel, #carryman'
    
    if p_mesage =='Daniel':
        return 'Jugando Lux o Morgana, Best support en el Team'

    if p_mesage == 'hello':
        return 'Leo es un Noob'
    
    if message == 'roll':
        return str(random.randint(1, 6))
    
    if p_mesage =='!help':
        return '`No te voy ayudar hasta que leo haga un penta kill #sad.`'
    

    return 'I didnt understand what you wrote fucking noob, btw Leo esta cocinando ahora. Try typing !help".'