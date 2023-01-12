# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.order import Order  # noqa: E501
from openapi_server.test import BaseTestCase


class TestStoreController(BaseTestCase):
    """StoreController integration test stubs"""

    def test_add_order(self):
        """Test case for add_order

        Submit a new order
        """
        query_string = [('name', 'name_example'),
                        ('size', 'medium'),
                        ('temperature', 'hot'),
                        ('milk', 'noMilk')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v3/store/order',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_order(self):
        """Test case for delete_order

        Deletes a record of an order.
        """
        headers = { 
        }
        response = self.client.open(
            '/v3/store/order/{order_id}'.format(order_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_orders_by_status(self):
        """Test case for find_orders_by_status

        Finds Orders by status
        """
        query_string = [('status', 'status_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v3/store/order/findByStatus',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_order_by_id(self):
        """Test case for get_order_by_id

        Find order by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v3/store/order/{order_id}'.format(order_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_order(self):
        """Test case for update_order

        Updates a order in the store
        """
        query_string = [('status', 'status_example')]
        headers = { 
        }
        response = self.client.open(
            '/v3/store/order/{order_id}'.format(order_id=56),
            method='PATCH',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
