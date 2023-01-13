import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.order import Order  # noqa: E501
from openapi_server import util


import sqlite3
import urllib3
import uuid
import os

# Find absolute path of SQLite db file
DB_PATH=os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'orders_db.db'
)

def initialize_database():
    """Initialize a dummy data base for coffee orders
    """
    with sqlite3.connect(DB_PATH) as conn:
        # Init the order table
        columns = [
            "id INTEGER PRIMARY KEY",
            "name VARCHAR",
            "size VARCHAR",
            "temperature VARCHAR",
            "milk VARCHAR",
            "status VARCHAR",
        ]

        create_table_cmd = f"CREATE TABLE OrderTable ({','.join(columns)})"

        conn.execute(create_table_cmd)

        #Init a few sample items into DB
        initItems = [
            "61396441, 'latte', 'small', 'cold', 'oat', 'placed'",
            "15456372, 'espresso', 'large', 'cold', 'soy', 'making'",
            "30876545, 'drip coffee', 'medium', 'hot', 'noMilk', 'made'",
            "25425104, 'espresso', 'small', 'hot', 'oat', 'delivered'",
        ]

        # Insert the items
        for i_data in initItems:
            insert_cmd = f"INSERT INTO OrderTable VALUES ({i_data})"
            conn.execute(insert_cmd)

def add_order(name, size=None, temperature=None, milk=None):  # noqa: E501
    """Submit a new order for a coffee.

    Submit a coffee order and choose your drink type, whether or not you would like milk, your drink temperature, and size. # noqa: E501

    :param name: The name of type of coffee you want to order.
    :type name: str
    :param size: The size of coffee you want to order.
    :type size: str
    :param temperature: The temperature of coffee you want to order.
    :type temperature: str
    :param milk: The type of milk you want to order.
    :type milk: str

    :rtype: Union[Order, Tuple[Order, int], Tuple[Order, int, Dict[str, str]]
    """
    id = uuid.uuid4().int % 2**32 # Randomly generated unique ID that fits in a 64-bit signed int.
    status = "placed"
    with sqlite3.connect(DB_PATH) as conn:
        tmporder = str(
            str(id) + \
            ",'" + str(name) + \
            "','" + str(size) + \
            "','" + str(temperature) + \
            "','" + str(milk) + \
            "','" + str(status) + "'")
        conn.execute(f"INSERT INTO OrderTable VALUES ({tmporder})")
    return Order(id=id,name=name,size=size,temperature=temperature,milk=milk,status=status)


def delete_order(order_id):  # noqa: E501
    """Deletes a record of an order.

    Deletes order record from database. The order must be identified by its ID. # noqa: E501

    :param order_id: ID of order to delete
    :type order_id: int

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    order = _get_order_by_id(order_id)
    if order is not None:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(f"DELETE FROM OrderTable WHERE id = {order_id}")
        return f"Deleted order {order_id}"
    else:
        return "Couldn't find an order with that ID",404


def find_orders_by_status(status):  # noqa: E501
    """Finds orders by status

    Returns a list of json schema filtered by status where each returned schema describes a coffee order stored within the database. # noqa: E501

    :param status: A state that a coffee order can be in as it is fufilled
    :type status: str

    :rtype: Union[List[Order], Tuple[List[Order], int], Tuple[List[Order], int, Dict[str, str]]
    """
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(f"SELECT * FROM OrderTable WHERE status = '{status}'")
        found_orders = []
        for row in rows:
            found_order = Order(
                id=row[0],
                name=row[1],
                size=row[2],
                temperature=row[3],
                milk=row[4],
                status=row[5]
            )
            found_orders.append(found_order)
    return found_orders


def _get_order_by_id(order_id):  # noqa: E501
    """Find order by ID

    Returns all information regarding a single order. # noqa: E501

    :param order_id: ID of order to return all information on.
    :type order_id: int

    :rtype: Union[Order, Tuple[Order, int], Tuple[Order, int, Dict[str, str]]
    """
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(f"SELECT * FROM OrderTable WHERE id = {order_id}")
        for row in rows:
            found_order = Order(
                id=row[0],
                name=row[1],
                size=row[2],
                temperature=row[3],
                milk=row[4],
                status=row[5]
            )
            return found_order
        return None

def get_order_by_id(order_id):  # noqa: E501
    """Find order by ID

    Returns all information regarding a single order. # noqa: E501

    :param order_id: ID of order to return all information on.
    :type order_id: int

    :rtype: Union[Order, Tuple[Order, int], Tuple[Order, int, Dict[str, str]]
    """
    order = _get_order_by_id(order_id)
    if order is not None:
        return order
    else:
        return "Couldn't find an order with that ID",404


def get_orders():  # noqa: E501
    """Retrieve all records of coffee orders from the store.

    Returns a list of json schema where each one describes a coffee order stored within the database. # noqa: E501


    :rtype: Union[List[Order], Tuple[List[Order], int], Tuple[List[Order], int, Dict[str, str]]
    """
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(f"SELECT * FROM OrderTable")
        orders = []
        for row in rows:
            orders.append(
                Order(
                    id=row[0],
                    name=row[1],
                    size=row[2],
                    temperature=row[3],
                    milk=row[4],
                    status=row[5]
                )
            )
    return orders


def update_order(order_id, status):  # noqa: E501
    """Updates the status of an individual order.

    Change the status of a single order in the store. The order must be identified by its ID. # noqa: E501

    :param order_id: ID of order to be updated
    :type order_id: int
    :param status: new status to update order to
    :type status: str

    :rtype: Union[List[Order], Tuple[List[Order], int], Tuple[List[Order], int, Dict[str, str]]
    """
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(f"UPDATE OrderTable SET status = '{status}' WHERE id = {order_id}")
    with sqlite3.connect(DB_PATH) as conn:
        return _get_order_by_id(order_id)


def update_order_coffee(order_id, name):  # noqa: E501
    """Updates the coffee type in the order

    Changes the type of a coffee ordered. The order must be identified by its ID. # noqa: E501

    :param order_id: ID of order whose type needs to be updated
    :type order_id: int
    :param name: new coffee type to update order to
    :type name: str

    :rtype: Union[List[Order], Tuple[List[Order], int], Tuple[List[Order], int, Dict[str, str]]
    """
    order = _get_order_by_id(order_id)
    if order is not None:
        if order.status != 'placed':
            return "Cannot change name parameter. Order is in progress. Parameters locked.",403
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(f"UPDATE OrderTable SET name = '{name}' WHERE id = {order_id}")
        with sqlite3.connect(DB_PATH) as conn:
            return _get_order_by_id(order_id)
    else:
        return "Couldn't find an order with that ID",404


def update_order_milk(order_id, milk):  # noqa: E501
    """Updates the milk type in the order

    Change the type of milk ordered. The order must be identified by its ID. # noqa: E501

    :param order_id: ID of order that needs to be updated
    :type order_id: int
    :param milk: new milk type to update order to
    :type milk: str

    :rtype: Union[List[Order], Tuple[List[Order], int], Tuple[List[Order], int, Dict[str, str]]
    """
    order = _get_order_by_id(order_id)
    if order is not None:
        if order.status != 'placed':
            return "Cannot change name parameter. Order is in progress. Parameters locked.",403
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(f"UPDATE OrderTable SET milk = '{milk}' WHERE id = {order_id}")
        with sqlite3.connect(DB_PATH) as conn:
            return _get_order_by_id(order_id)
    else:
        return "Couldn't find an order with that ID",404


def update_order_size(order_id, size):  # noqa: E501
    """Updates the size of the drink ordered

    Change the size of the order. The order must be identified by its ID. # noqa: E501

    :param order_id: ID of order that needs to be updated
    :type order_id: int
    :param size: new size to update order to
    :type size: str

    :rtype: Union[List[Order], Tuple[List[Order], int], Tuple[List[Order], int, Dict[str, str]]
    """ 
    order = _get_order_by_id(order_id)
    if order is not None:
        if order.status != 'placed':
            return "Cannot change name parameter. Order is in progress. Parameters locked.",403
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(f"UPDATE OrderTable SET size = '{size}' WHERE id = {order_id}")
        with sqlite3.connect(DB_PATH) as conn:
            return _get_order_by_id(order_id)
    else:
        return "Couldn't find an order with that ID",404

def update_order_temp(order_id, temperature):  # noqa: E501
    """Updates the temperature of the order

    Change the temperature of the order. The order must be identified by its ID. # noqa: E501

    :param order_id: ID of order that needs to be updated
    :type order_id: int
    :param temperature: new temperature to update order to
    :type temperature: str

    :rtype: Union[List[Order], Tuple[List[Order], int], Tuple[List[Order], int, Dict[str, str]]
    """
    order = _get_order_by_id(order_id)
    if order is not None:
        if order.status != 'placed':
            return "Cannot change name parameter. Order is in progress. Parameters locked.",403
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(f"UPDATE OrderTable SET temperature = '{temperature}' WHERE id = {order_id}")
        with sqlite3.connect(DB_PATH) as conn:
            return _get_order_by_id(order_id)
    else:
        return "Couldn't find an order with that ID",404

if not os.path.exists(DB_PATH):
    initialize_database()
