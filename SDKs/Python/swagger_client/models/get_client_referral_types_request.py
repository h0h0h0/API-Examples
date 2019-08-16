# coding: utf-8

"""
    MINDBODY Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GetClientReferralTypesRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'include_inactive': 'bool'
    }

    attribute_map = {
        'include_inactive': 'IncludeInactive'
    }

    def __init__(self, include_inactive=None):  # noqa: E501
        """GetClientReferralTypesRequest - a model defined in Swagger"""  # noqa: E501

        self._include_inactive = None
        self.discriminator = None

        if include_inactive is not None:
            self.include_inactive = include_inactive

    @property
    def include_inactive(self):
        """Gets the include_inactive of this GetClientReferralTypesRequest.  # noqa: E501

        When `true`, filters the results to include subtypes and inactive referral types.<br />  When `false`, includes no subtypes and only active types.  # noqa: E501

        :return: The include_inactive of this GetClientReferralTypesRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_inactive

    @include_inactive.setter
    def include_inactive(self, include_inactive):
        """Sets the include_inactive of this GetClientReferralTypesRequest.

        When `true`, filters the results to include subtypes and inactive referral types.<br />  When `false`, includes no subtypes and only active types.  # noqa: E501

        :param include_inactive: The include_inactive of this GetClientReferralTypesRequest.  # noqa: E501
        :type: bool
        """

        self._include_inactive = include_inactive

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(GetClientReferralTypesRequest, dict):
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
        if not isinstance(other, GetClientReferralTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other