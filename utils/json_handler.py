import json

def read_json(filepath: str) -> list[dict]:

    with open(filepath, 'r') as file:
        
        json_data = json.load(file)
        
        return json_data

    
def write_json(filepath: str, payload: list[dict]):
    
    with open(filepath, 'w') as file:
    
        json.dump(payload, file, indent=2, ensure_ascii=False)


def generate_id(filepath: str) -> None:

    data = read_json(filepath)
    new_item_id = len(data) + 1
    new_item = {"name": "CHURROS DO M5", "price": 5.0, "id":new_item_id}
    data.append(new_item)

    write_json(filepath, data)
