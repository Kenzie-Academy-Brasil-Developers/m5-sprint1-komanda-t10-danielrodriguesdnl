from utils import read_json, generate_id
from management import tab_bill
import json

FILEPATH = 'menu.json'

def main():
    try:
        read_json(FILEPATH)
    except (json.JSONDecodeError, FileNotFoundError):
        return [ ]

    generate_id(FILEPATH)

    tab_bill(table_1, FILEPATH)





if __name__ == "__main__":
    table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
    table_2 = [
      {"id": 10, "amount": 3},
      {"id": 20, "amount": 2},
      {"id": 21, "amount": 5},
    ]
    main()
