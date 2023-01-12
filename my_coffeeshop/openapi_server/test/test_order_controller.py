# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.order import Order  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOrderController(BaseTestCase):
    """OrderController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_order(self):
        """Test case for add_order

        Submit a new order
        """
        order = {"id":0,"items":"items","status":"placed"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v2/order',
            method='POST',
            headers=headers,
            data=json.dumps(order),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_order(self):
        """Test case for delete_order

        Deletes a order
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/order/{order_id}'.format(order_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_orders_by_status(self):
        """Test case for find_orders_by_status

        Finds Orders by status
        """
        query_string = [('status', ['status_example'])]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v2/order/findByStatus',
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
            '/v2/order/{order_id}'.format(order_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_order_with_form(self):
        """Test case for update_order_with_form

        Updates a order in the store with form data
        """
        query_string = [('items', 'items_example'),
                        ('status', 'status_example')]
        headers = { 
        }
        response = self.client.open(
            '/v2/order/{order_id}'.format(order_id=56),
            method='PATCH',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
