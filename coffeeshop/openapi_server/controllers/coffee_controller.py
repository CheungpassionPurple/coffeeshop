import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.coffee import Coffee  # noqa: E501
from openapi_server import util


def add_coffee(coffee):  # noqa: E501
    """Add a new coffee to the store

     # noqa: E501

    :param coffee: Coffee object that needs to be added to the store
    :type coffee: dict | bytes

    :rtype: Union[Coffee, Tuple[Coffee, int], Tuple[Coffee, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        coffee = Coffee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_coffee(coffee_id, api_key=None):  # noqa: E501
    """Deletes a coffee

     # noqa: E501

    :param coffee_id: Coffee id to delete
    :type coffee_id: int
    :param api_key: 
    :type api_key: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def find_coffees_by_status(status):  # noqa: E501
    """Finds Coffees by status

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: Union[List[Coffee], Tuple[List[Coffee], int], Tuple[List[Coffee], int, Dict[str, str]]
    """
    return 'do some magic!'


def find_coffees_by_tags(tags):  # noqa: E501
    """Finds Coffees by tags

    Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing. # noqa: E501

    :param tags: Tags to filter by
    :type tags: List[str]

    :rtype: Union[List[Coffee], Tuple[List[Coffee], int], Tuple[List[Coffee], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_coffee_by_id(coffee_id):  # noqa: E501
    """Find coffee by ID

    Returns a single coffee # noqa: E501

    :param coffee_id: ID of coffee to return
    :type coffee_id: int

    :rtype: Union[Coffee, Tuple[Coffee, int], Tuple[Coffee, int, Dict[str, str]]
    """
    return 'do some magic!'


def update_coffee(coffee):  # noqa: E501
    """Update an existing coffee

     # noqa: E501

    :param coffee: Coffee object that needs to be added to the store
    :type coffee: dict | bytes

    :rtype: Union[Coffee, Tuple[Coffee, int], Tuple[Coffee, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        coffee = Coffee.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_coffee_with_form(coffee_id, name=None, status=None):  # noqa: E501
    """Updates a coffee in the store with form data

     # noqa: E501

    :param coffee_id: ID of coffee that needs to be updated
    :type coffee_id: int
    :param name: Updated name of the coffee
    :type name: str
    :param status: Updated status of the coffee
    :type status: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def upload_file(coffee_id, additional_metadata=None, file=None):  # noqa: E501
    """uploads an image

     # noqa: E501

    :param coffee_id: ID of coffee to update
    :type coffee_id: int
    :param additional_metadata: Additional data to pass to server
    :type additional_metadata: str
    :param file: file to upload
    :type file: str

    :rtype: Union[ApiResponse, Tuple[ApiResponse, int], Tuple[ApiResponse, int, Dict[str, str]]
    """
    return 'do some magic!'
