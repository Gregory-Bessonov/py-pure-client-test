# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_20 import models

class ArrayConnection(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'management_address': 'str',
        'replication_addresses': 'list[str]',
        'status': 'str',
        'type': 'str',
        'replication_transport': 'str',
        'version': 'str',
        'throttle': 'Throttle'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'management_address': 'management_address',
        'replication_addresses': 'replication_addresses',
        'status': 'status',
        'type': 'type',
        'replication_transport': 'replication_transport',
        'version': 'version',
        'throttle': 'throttle'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        management_address=None,  # type: str
        replication_addresses=None,  # type: List[str]
        status=None,  # type: str
        type=None,  # type: str
        replication_transport=None,  # type: str
        version=None,  # type: str
        throttle=None,  # type: models.Throttle
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A locally unique, system-generated name. The name cannot be modified.
            management_address (str): Management IP address or FQDN of the target array.
            replication_addresses (list[str]): IP addresses of the target arrays when `replication_transport` is `ip`. WWNs of the target arrays when `replication_transport` is `fc`.
            status (str): Status of the connection. Valid values are `connected`, `connecting`, `partially_connected`, and `unbalanced`. A status of `connected` indicates that arrays are communicating. A status of `connecting` indicates that the array is trying to establish a connection. A status of `partially_connected` indicates that some replication addresses are communicating but others are not. A status of `unbalanced` indicates that the arrays are communicating, but the set of paths is either not redundant or not symmetric.
            type (str): The type of replication. Valid values are `async-replication` and `sync-replication`.
            replication_transport (str): The protocol used to transport data between the local array and the remote array. Valid values are `ip` and `fc`. The default is `ip`.
            version (str): The version of the target array.
            throttle (Throttle)
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if management_address is not None:
            self.management_address = management_address
        if replication_addresses is not None:
            self.replication_addresses = replication_addresses
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if replication_transport is not None:
            self.replication_transport = replication_transport
        if version is not None:
            self.version = version
        if throttle is not None:
            self.throttle = throttle

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ArrayConnection`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(ArrayConnection, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArrayConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
