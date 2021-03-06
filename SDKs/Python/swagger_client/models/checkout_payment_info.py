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


class CheckoutPaymentInfo(object):
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
        'type': 'str',
        'metadata': 'dict(str, object)'
    }

    attribute_map = {
        'type': 'Type',
        'metadata': 'Metadata'
    }

    def __init__(self, type=None, metadata=None):  # noqa: E501
        """CheckoutPaymentInfo - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._metadata = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if metadata is not None:
            self.metadata = metadata

    @property
    def type(self):
        """Gets the type of this CheckoutPaymentInfo.  # noqa: E501

        The type of payment. Possible values are:  * CreditCard - Indicates that this payment item is a credit card.  * StoredCard - Indicates that this payment item is a credit card stored on the client’s account.  * EncryptedTrackData - Indicates that this payment item is a swiped credit card.  * TrackData - Indicates that this payment item is a swiped credit card.  * DebitAccount - Indicates that funds should be debited from the client’s account.  * Custom - Indicates that this payment item is a custom payment method configured by the business.  * Comp - Indicates that this payment item is making all or part of the cart’s total complementary.  * Cash - Indicates that this payment item is cash.  * Check - Indicates that this payment item is a check.  * GiftCard - Indicates that this payment item is a gift card.  # noqa: E501

        :return: The type of this CheckoutPaymentInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CheckoutPaymentInfo.

        The type of payment. Possible values are:  * CreditCard - Indicates that this payment item is a credit card.  * StoredCard - Indicates that this payment item is a credit card stored on the client’s account.  * EncryptedTrackData - Indicates that this payment item is a swiped credit card.  * TrackData - Indicates that this payment item is a swiped credit card.  * DebitAccount - Indicates that funds should be debited from the client’s account.  * Custom - Indicates that this payment item is a custom payment method configured by the business.  * Comp - Indicates that this payment item is making all or part of the cart’s total complementary.  * Cash - Indicates that this payment item is cash.  * Check - Indicates that this payment item is a check.  * GiftCard - Indicates that this payment item is a gift card.  # noqa: E501

        :param type: The type of this CheckoutPaymentInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def metadata(self):
        """Gets the metadata of this CheckoutPaymentInfo.  # noqa: E501

        Contains information about the cart’s payments. See [Payment Item Metadata](https://developers.mindbodyonline.com/PublicDocumentation/V6#payment-item-metadata) for more information.  # noqa: E501

        :return: The metadata of this CheckoutPaymentInfo.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CheckoutPaymentInfo.

        Contains information about the cart’s payments. See [Payment Item Metadata](https://developers.mindbodyonline.com/PublicDocumentation/V6#payment-item-metadata) for more information.  # noqa: E501

        :param metadata: The metadata of this CheckoutPaymentInfo.  # noqa: E501
        :type: dict(str, object)
        """

        self._metadata = metadata

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
        if issubclass(CheckoutPaymentInfo, dict):
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
        if not isinstance(other, CheckoutPaymentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
