from utils import read_json
from datetime import date, time, datetime, timedelta, timezone

def tab_bill(payload: list[dict], filepath: str) -> dict:
    menu_itens = read_json(filepath)
    price_iten = 0
    total_price = 0
    datetime_atual = datetime.now()
    date_time = datetime_atual.strftime("%m/%d/%Y, %H:%M:%S")
    
    
    for value in payload:
        id_item = value['id']
        amount_item = value['amount']
        
        for value in menu_itens:
            if value['id'] == id_item:
                price_iten = value['price']
                
                total_item =+ price_iten * amount_item
                total_price = total_price + total_item


    return{'subtotal': total_price, 'created_at': date_time}



