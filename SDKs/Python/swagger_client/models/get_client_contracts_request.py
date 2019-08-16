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


class GetClientContractsRequest(object):
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
        'client_id': 'str',
        'cross_regional_lookup': 'bool',
        'client_associated_sites_offset': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'client_id': 'ClientId',
        'cross_regional_lookup': 'CrossRegionalLookup',
        'client_associated_sites_offset': 'ClientAssociatedSitesOffset',
        'limit': 'Limit',
        'offset': 'Offset'
    }

    def __init__(self, client_id=None, cross_regional_lookup=None, client_associated_sites_offset=None, limit=None, offset=None):  # noqa: E501
        """GetClientContractsRequest - a model defined in Swagger"""  # noqa: E501

        self._client_id = None
        self._cross_regional_lookup = None
        self._client_associated_sites_offset = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.client_id = client_id
        if cross_regional_lookup is not None:
            self.cross_regional_lookup = cross_regional_lookup
        if client_associated_sites_offset is not None:
            self.client_associated_sites_offset = client_associated_sites_offset
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def client_id(self):
        """Gets the client_id of this GetClientContractsRequest.  # noqa: E501

        The ID of the client.  # noqa: E501

        :return: The client_id of this GetClientContractsRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this GetClientContractsRequest.

        The ID of the client.  # noqa: E501

        :param client_id: The client_id of this GetClientContractsRequest.  # noqa: E501
        :type: str
        """
        if client_id is None:
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def cross_regional_lookup(self):
        """Gets the cross_regional_lookup of this GetClientContractsRequest.  # noqa: E501

        When `true`, indicates that the requesting client’s cross regional contracts are returned, if any.<br />  When `false`, indicates that cross regional contracts are not returned.  # noqa: E501

        :return: The cross_regional_lookup of this GetClientContractsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._cross_regional_lookup

    @cross_regional_lookup.setter
    def cross_regional_lookup(self, cross_regional_lookup):
        """Sets the cross_regional_lookup of this GetClientContractsRequest.

        When `true`, indicates that the requesting client’s cross regional contracts are returned, if any.<br />  When `false`, indicates that cross regional contracts are not returned.  # noqa: E501

        :param cross_regional_lookup: The cross_regional_lookup of this GetClientContractsRequest.  # noqa: E501
        :type: bool
        """

        self._cross_regional_lookup = cross_regional_lookup

    @property
    def client_associated_sites_offset(self):
        """Gets the client_associated_sites_offset of this GetClientContractsRequest.  # noqa: E501

        Determines how many sites are skipped over when retrieving a client’s cross regional contracts. Used when a client ID is linked to more than ten sites in an organization. Only a maximum of ten site databases are queried when this call is made and `CrossRegionalLookup` is set to `true`. To change which sites are queried, change this offset value.  Default: **0**  # noqa: E501

        :return: The client_associated_sites_offset of this GetClientContractsRequest.  # noqa: E501
        :rtype: int
        """
        return self._client_associated_sites_offset

    @client_associated_sites_offset.setter
    def client_associated_sites_offset(self, client_associated_sites_offset):
        """Sets the client_associated_sites_offset of this GetClientContractsRequest.

        Determines how many sites are skipped over when retrieving a client’s cross regional contracts. Used when a client ID is linked to more than ten sites in an organization. Only a maximum of ten site databases are queried when this call is made and `CrossRegionalLookup` is set to `true`. To change which sites are queried, change this offset value.  Default: **0**  # noqa: E501

        :param client_associated_sites_offset: The client_associated_sites_offset of this GetClientContractsRequest.  # noqa: E501
        :type: int
        """

        self._client_associated_sites_offset = client_associated_sites_offset

    @property
    def limit(self):
        """Gets the limit of this GetClientContractsRequest.  # noqa: E501

        Number of results to include, defaults to 100  # noqa: E501

        :return: The limit of this GetClientContractsRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this GetClientContractsRequest.

        Number of results to include, defaults to 100  # noqa: E501

        :param limit: The limit of this GetClientContractsRequest.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this GetClientContractsRequest.  # noqa: E501

        Page offset, defaults to 0.  # noqa: E501

        :return: The offset of this GetClientContractsRequest.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this GetClientContractsRequest.

        Page offset, defaults to 0.  # noqa: E501

        :param offset: The offset of this GetClientContractsRequest.  # noqa: E501
        :type: int
        """

        self._offset = offset

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
        if issubclass(GetClientContractsRequest, dict):
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
        if not isinstance(other, GetClientContractsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other