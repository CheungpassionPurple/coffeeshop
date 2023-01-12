import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.order import Order  # noqa: E501
from openapi_server import util

import sqlite3

def add_order():  # noqa: E501
    """Submit a new order

     # noqa: E501

    :param order: Order object that needs to be added to the store
    :type order: dict | bytes

    :rtype: Union[Order, Tuple[Order, int], Tuple[Order, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        order = Order.from_dict(connexion.request.get_json())  # noqa: E501

    conn = sqlite3.connect("C:/Users/212809778/Documents/microservice-hw/flask_venv/MyCoffeeShop/openapi_server/controllers/orders_db.db")
    cursor = conn.cursor()
    tmporder = str(str(order.id) + ",'" + order.items + "','" + order.status + "'")
    print(tmporder)
    insert_cmd = f"INSERT INTO OrderTable VALUES ({tmporder})"
    cursor.execute(insert_cmd)
    conn.commit()
    return 'do some magic!'


def delete_order(order_id):  # noqa: E501
    """Deletes a order

     # noqa: E501

    :param order_id: Order id to delete
    :type order_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    conn = sqlite3.connect("C:/Users/212809778/Documents/microservice-hw/flask_venv/MyCoffeeShop/openapi_server/controllers/orders_db.db")
    cursor = conn.cursor()
    insert_cmd = f"DELETE FROM OrderTable WHERE id = {order_id}"
    cursor.execute(insert_cmd)
    conn.commit()

    return 'do some magic!'


def find_orders_by_status(status):  # noqa: E501
    """Finds Orders by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: Union[List[Order], Tuple[List[Order], int], Tuple[List[Order], int, Dict[str, str]]
    """
    conn = sqlite3.connect("C:/Users/212809778/Documents/microservice-hw/flask_venv/MyCoffeeShop/openapi_server/controllers/orders_db.db")
    cursor = conn.cursor()
    print(status[0])
    insert_cmd = f"SELECT * FROM OrderTable WHERE status = '{status[0]}'"
    rows = cursor.execute(insert_cmd)
    a = ""
    for row in rows:
        a += str(row)
    conn.commit()

    return str(a)


def get_order_by_id(order_id):  # noqa: E501
    """Find order by ID

    Returns a single order # noqa: E501

    :param order_id: ID of order to return
    :type order_id: int

    :rtype: Union[Order, Tuple[Order, int], Tuple[Order, int, Dict[str, str]]
    """
    conn = sqlite3.connect("C:/Users/212809778/Documents/microservice-hw/flask_venv/MyCoffeeShop/openapi_server/controllers/orders_db.db")
    cursor = conn.cursor()
    insert_cmd = f"SELECT * FROM OrderTable WHERE id = {order_id}"
    rows = cursor.execute(insert_cmd)
    a = ""
    for row in rows:
        a += str(row)
    conn.commit()

    return str(a)

def update_order_with_form(order_id, items, status):  # noqa: E501
    """Updates a order in the store with form data

     # noqa: E501

    :param order_id: ID of order that needs to be updated
    :type order_id: int
    :param items: items in order that can be updated
    :type items: str
    :param status: status order that needs to be updated
    :type status: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """

    conn = sqlite3.connect("C:/Users/212809778/Documents/microservice-hw/flask_venv/MyCoffeeShop/openapi_server/controllers/orders_db.db")
    cursor = conn.cursor()
    insert_cmd = f"UPDATE OrderTable SET items = '{items}', status = '{status}' WHERE id = {order_id}"
    cursor.execute(insert_cmd)
    conn.commit()

    return 'do some magic!'
