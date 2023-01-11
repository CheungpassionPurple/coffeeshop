# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.coffee import Coffee  # noqa: E501
from openapi_server.test import BaseTestCase


class TestCoffeeController(BaseTestCase):
    """CoffeeController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_coffee(self):
        """Test case for add_coffee

        Add a new coffee to the store
        """
        coffee = {"photoUrls":["photoUrls","photoUrls"],"name":"doggie","id":0,"category":{"name":"name","id":6},"tags":[{"name":"name","id":1},{"name":"name","id":1}],"status":"available"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/coffee',
            method='POST',
            headers=headers,
            data=json.dumps(coffee),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_coffee(self):
        """Test case for delete_coffee

        Deletes a coffee
        """
        headers = { 
            'api_key': 'api_key_example',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/coffee/{coffee_id}'.format(coffee_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_coffees_by_status(self):
        """Test case for find_coffees_by_status

        Finds Coffees by status
        """
        query_string = [('status', ['status_example'])]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/coffee/findByStatus',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_coffees_by_tags(self):
        """Test case for find_coffees_by_tags

        Finds Coffees by tags
        """
        query_string = [('tags', ['tags_example'])]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/coffee/findByTags',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_coffee_by_id(self):
        """Test case for get_coffee_by_id

        Find coffee by ID
        """
        headers = { 
            'Accept': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v2/coffee/{coffee_id}'.format(coffee_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_update_coffee(self):
        """Test case for update_coffee

        Update an existing coffee
        """
        coffee = {"photoUrls":["photoUrls","photoUrls"],"name":"doggie","id":0,"category":{"name":"name","id":6},"tags":[{"name":"name","id":1},{"name":"name","id":1}],"status":"available"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/coffee',
            method='PUT',
            headers=headers,
            data=json.dumps(coffee),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("application/x-www-form-urlencoded not supported by Connexion")
    def test_update_coffee_with_form(self):
        """Test case for update_coffee_with_form

        Updates a coffee in the store with form data
        """
        headers = { 
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer special-key',
        }
        data = dict(name='name_example',
                    status='status_example')
        response = self.client.open(
            '/v2/coffee/{coffee_id}'.format(coffee_id=56),
            method='POST',
            headers=headers,
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_upload_file(self):
        """Test case for upload_file

        uploads an image
        """
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer special-key',
        }
        data = dict(additional_metadata='additional_metadata_example',
                    file='/path/to/file')
        response = self.client.open(
            '/v2/coffee/{coffee_id}/uploadImage'.format(coffee_id=56),
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
