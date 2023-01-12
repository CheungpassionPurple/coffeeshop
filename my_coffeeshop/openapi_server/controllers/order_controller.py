import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.order import Order  # noqa: E501
from openapi_server import util

import sqlite3

DB_PATH='/home/justincheung/ACourse/Week13Microservices/coffeeshop/my_coffeeshop/openapi_server/controllers/orders_db.db'

def add_order():  # noqa: E501
    """Submit a new order

     # noqa: E501

    :param order: Order object that needs to be added to the store
    :type order: dict | bytes

    :rtype: Union[Order, Tuple[Order, int], Tuple[Order, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        order = Order.from_dict(connexion.request.get_json())  # noqa: E501

    with sqlite3.connect(DB_PATH) as conn:
        tmporder = str(str(order.id) + ",'" + order.items + "','" + order.status + "'")
        conn.execute(f"INSERT INTO OrderTable VALUES ({tmporder})")
    return order


def delete_order(order_id):  # noqa: E501
    """Deletes a order

     # noqa: E501

    :param order_id: Order id to delete
    :type order_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(f"DELETE FROM OrderTable WHERE id = {order_id}")
    return f"Deleted order {order_id}!"


def find_orders_by_status(status):  # noqa: E501
    """Finds Orders by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: Union[List[Order], Tuple[List[Order], int], Tuple[List[Order], int, Dict[str, str]]
    """
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(f"SELECT * FROM OrderTable WHERE status = '{status[0]}'")
        a = ""
        for row in rows:
            a += str(row)
    return str(a)


def get_order_by_id(order_id):  # noqa: E501
    """Find order by ID

    Returns a single order # noqa: E501

    :param order_id: ID of order to return
    :type order_id: int

    :rtype: Union[Order, Tuple[Order, int], Tuple[Order, int, Dict[str, str]]
    """
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(f"SELECT * FROM OrderTable WHERE id = {order_id}")
        a = ""
        for row in rows:
            a += str(row)
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

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(f"UPDATE OrderTable SET items = '{items}', status = '{status}' WHERE id = {order_id}")
    return 'do some magic!'
