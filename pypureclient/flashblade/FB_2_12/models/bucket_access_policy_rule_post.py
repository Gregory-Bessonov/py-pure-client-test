# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.12, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_12 import models

class BucketAccessPolicyRulePost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'actions': 'list[str]',
        'effect': 'str',
        'principals': 'BucketAccessPolicyRulePrincipal',
        'resources': 'list[str]'
    }

    attribute_map = {
        'actions': 'actions',
        'effect': 'effect',
        'principals': 'principals',
        'resources': 'resources'
    }

    required_args = {
    }

    def __init__(
        self,
        actions=None,  # type: List[str]
        effect=None,  # type: str
        principals=None,  # type: models.BucketAccessPolicyRulePrincipal
        resources=None,  # type: List[str]
    ):
        """
        Keyword args:
            actions (list[str]): The list of actions granted by this rule. Each included action may restrict other properties of the rule. The only currently supported action is `s3:GetObject`.
            effect (str): Effect of this rule. When `allow`, the rule allows the given actions to be performed on the given resources, subject to the given conditions. The only currently supported effect is `allow`.
            principals (BucketAccessPolicyRulePrincipal): The principals to which this rule applies. Currently, only all principals are supported.
            resources (list[str]): The list of resources which this rule applies to. The only currently supported resource is all objects in a bucket to which the parent policy belongs.
        """
        if actions is not None:
            self.actions = actions
        if effect is not None:
            self.effect = effect
        if principals is not None:
            self.principals = principals
        if resources is not None:
            self.resources = resources

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `BucketAccessPolicyRulePost`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
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
        if issubclass(BucketAccessPolicyRulePost, dict):
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
        if not isinstance(other, BucketAccessPolicyRulePost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
