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

from swagger_client.models.checkout_payment_info import CheckoutPaymentInfo  # noqa: F401,E501


class PurchaseGiftCardRequest(object):
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
        'test': 'bool',
        'location_id': 'int',
        'layout_id': 'int',
        'purchaser_client_id': 'str',
        'gift_card_id': 'int',
        'send_email_receipt': 'bool',
        'recipient_email': 'str',
        'recipient_name': 'str',
        'title': 'str',
        'gift_message': 'str',
        'delivery_date': 'datetime',
        'payment_info': 'CheckoutPaymentInfo'
    }

    attribute_map = {
        'test': 'Test',
        'location_id': 'LocationId',
        'layout_id': 'LayoutId',
        'purchaser_client_id': 'PurchaserClientId',
        'gift_card_id': 'GiftCardId',
        'send_email_receipt': 'SendEmailReceipt',
        'recipient_email': 'RecipientEmail',
        'recipient_name': 'RecipientName',
        'title': 'Title',
        'gift_message': 'GiftMessage',
        'delivery_date': 'DeliveryDate',
        'payment_info': 'PaymentInfo'
    }

    def __init__(self, test=None, location_id=None, layout_id=None, purchaser_client_id=None, gift_card_id=None, send_email_receipt=None, recipient_email=None, recipient_name=None, title=None, gift_message=None, delivery_date=None, payment_info=None):  # noqa: E501
        """PurchaseGiftCardRequest - a model defined in Swagger"""  # noqa: E501

        self._test = None
        self._location_id = None
        self._layout_id = None
        self._purchaser_client_id = None
        self._gift_card_id = None
        self._send_email_receipt = None
        self._recipient_email = None
        self._recipient_name = None
        self._title = None
        self._gift_message = None
        self._delivery_date = None
        self._payment_info = None
        self.discriminator = None

        if test is not None:
            self.test = test
        self.location_id = location_id
        if layout_id is not None:
            self.layout_id = layout_id
        self.purchaser_client_id = purchaser_client_id
        self.gift_card_id = gift_card_id
        if send_email_receipt is not None:
            self.send_email_receipt = send_email_receipt
        if recipient_email is not None:
            self.recipient_email = recipient_email
        if recipient_name is not None:
            self.recipient_name = recipient_name
        if title is not None:
            self.title = title
        if gift_message is not None:
            self.gift_message = gift_message
        if delivery_date is not None:
            self.delivery_date = delivery_date
        if payment_info is not None:
            self.payment_info = payment_info

    @property
    def test(self):
        """Gets the test of this PurchaseGiftCardRequest.  # noqa: E501

        When `true`, allows you to test the request without affecting the database.<br />  When `false`, the request is carried out and the database is affected.  # noqa: E501

        :return: The test of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this PurchaseGiftCardRequest.

        When `true`, allows you to test the request without affecting the database.<br />  When `false`, the request is carried out and the database is affected.  # noqa: E501

        :param test: The test of this PurchaseGiftCardRequest.  # noqa: E501
        :type: bool
        """

        self._test = test

    @property
    def location_id(self):
        """Gets the location_id of this PurchaseGiftCardRequest.  # noqa: E501

        The ID of the location where the gift card is being sold.  # noqa: E501

        :return: The location_id of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this PurchaseGiftCardRequest.

        The ID of the location where the gift card is being sold.  # noqa: E501

        :param location_id: The location_id of this PurchaseGiftCardRequest.  # noqa: E501
        :type: int
        """
        if location_id is None:
            raise ValueError("Invalid value for `location_id`, must not be `None`")  # noqa: E501

        self._location_id = location_id

    @property
    def layout_id(self):
        """Gets the layout_id of this PurchaseGiftCardRequest.  # noqa: E501

        The ID of the layout used for the gift card’s image.  # noqa: E501

        :return: The layout_id of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: int
        """
        return self._layout_id

    @layout_id.setter
    def layout_id(self, layout_id):
        """Sets the layout_id of this PurchaseGiftCardRequest.

        The ID of the layout used for the gift card’s image.  # noqa: E501

        :param layout_id: The layout_id of this PurchaseGiftCardRequest.  # noqa: E501
        :type: int
        """

        self._layout_id = layout_id

    @property
    def purchaser_client_id(self):
        """Gets the purchaser_client_id of this PurchaseGiftCardRequest.  # noqa: E501

        The RSSID of the client who is purchasing the gift card.  # noqa: E501

        :return: The purchaser_client_id of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: str
        """
        return self._purchaser_client_id

    @purchaser_client_id.setter
    def purchaser_client_id(self, purchaser_client_id):
        """Sets the purchaser_client_id of this PurchaseGiftCardRequest.

        The RSSID of the client who is purchasing the gift card.  # noqa: E501

        :param purchaser_client_id: The purchaser_client_id of this PurchaseGiftCardRequest.  # noqa: E501
        :type: str
        """
        if purchaser_client_id is None:
            raise ValueError("Invalid value for `purchaser_client_id`, must not be `None`")  # noqa: E501

        self._purchaser_client_id = purchaser_client_id

    @property
    def gift_card_id(self):
        """Gets the gift_card_id of this PurchaseGiftCardRequest.  # noqa: E501

        The product ID of the gift card being purchased.  # noqa: E501

        :return: The gift_card_id of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: int
        """
        return self._gift_card_id

    @gift_card_id.setter
    def gift_card_id(self, gift_card_id):
        """Sets the gift_card_id of this PurchaseGiftCardRequest.

        The product ID of the gift card being purchased.  # noqa: E501

        :param gift_card_id: The gift_card_id of this PurchaseGiftCardRequest.  # noqa: E501
        :type: int
        """
        if gift_card_id is None:
            raise ValueError("Invalid value for `gift_card_id`, must not be `None`")  # noqa: E501

        self._gift_card_id = gift_card_id

    @property
    def send_email_receipt(self):
        """Gets the send_email_receipt of this PurchaseGiftCardRequest.  # noqa: E501

        When `true`, indicates that a purchase receipt email should be sent to the purchasing client, if all settings are correctly configured.<br />  When `false`, no email is sent to the purchaser.  # noqa: E501

        :return: The send_email_receipt of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_email_receipt

    @send_email_receipt.setter
    def send_email_receipt(self, send_email_receipt):
        """Sets the send_email_receipt of this PurchaseGiftCardRequest.

        When `true`, indicates that a purchase receipt email should be sent to the purchasing client, if all settings are correctly configured.<br />  When `false`, no email is sent to the purchaser.  # noqa: E501

        :param send_email_receipt: The send_email_receipt of this PurchaseGiftCardRequest.  # noqa: E501
        :type: bool
        """

        self._send_email_receipt = send_email_receipt

    @property
    def recipient_email(self):
        """Gets the recipient_email of this PurchaseGiftCardRequest.  # noqa: E501

        The email address to send the gift card image to. This parameter is required if the `LayoutId` is not 0.<br />  Maximum length: **100**  # noqa: E501

        :return: The recipient_email of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_email

    @recipient_email.setter
    def recipient_email(self, recipient_email):
        """Sets the recipient_email of this PurchaseGiftCardRequest.

        The email address to send the gift card image to. This parameter is required if the `LayoutId` is not 0.<br />  Maximum length: **100**  # noqa: E501

        :param recipient_email: The recipient_email of this PurchaseGiftCardRequest.  # noqa: E501
        :type: str
        """

        self._recipient_email = recipient_email

    @property
    def recipient_name(self):
        """Gets the recipient_name of this PurchaseGiftCardRequest.  # noqa: E501

        The name of the person who is to receive the gift card. This parameter is required if the `LayoutId` is not 0.<br />  Maximum length: **20**  # noqa: E501

        :return: The recipient_name of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: str
        """
        return self._recipient_name

    @recipient_name.setter
    def recipient_name(self, recipient_name):
        """Sets the recipient_name of this PurchaseGiftCardRequest.

        The name of the person who is to receive the gift card. This parameter is required if the `LayoutId` is not 0.<br />  Maximum length: **20**  # noqa: E501

        :param recipient_name: The recipient_name of this PurchaseGiftCardRequest.  # noqa: E501
        :type: str
        """

        self._recipient_name = recipient_name

    @property
    def title(self):
        """Gets the title of this PurchaseGiftCardRequest.  # noqa: E501

        The text to use as the title of the gift card, for example: Happy Birthday, Maria! This parameter is required if the `LayoutId` is not 0.<br />  Maximum length: **20**  # noqa: E501

        :return: The title of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PurchaseGiftCardRequest.

        The text to use as the title of the gift card, for example: Happy Birthday, Maria! This parameter is required if the `LayoutId` is not 0.<br />  Maximum length: **20**  # noqa: E501

        :param title: The title of this PurchaseGiftCardRequest.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def gift_message(self):
        """Gets the gift_message of this PurchaseGiftCardRequest.  # noqa: E501

        A personal message to include in the gift card.<br />  Maximum length: **300**  # noqa: E501

        :return: The gift_message of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: str
        """
        return self._gift_message

    @gift_message.setter
    def gift_message(self, gift_message):
        """Sets the gift_message of this PurchaseGiftCardRequest.

        A personal message to include in the gift card.<br />  Maximum length: **300**  # noqa: E501

        :param gift_message: The gift_message of this PurchaseGiftCardRequest.  # noqa: E501
        :type: str
        """

        self._gift_message = gift_message

    @property
    def delivery_date(self):
        """Gets the delivery_date of this PurchaseGiftCardRequest.  # noqa: E501

        The date that the gift card’s image is to be delivered to the recipient. This parameter cannot be set to a date in the past. This parameter is required if the `LayoutId` is not 0.  Default: **today**  Minimum: **today**  # noqa: E501

        :return: The delivery_date of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        """Sets the delivery_date of this PurchaseGiftCardRequest.

        The date that the gift card’s image is to be delivered to the recipient. This parameter cannot be set to a date in the past. This parameter is required if the `LayoutId` is not 0.  Default: **today**  Minimum: **today**  # noqa: E501

        :param delivery_date: The delivery_date of this PurchaseGiftCardRequest.  # noqa: E501
        :type: datetime
        """

        self._delivery_date = delivery_date

    @property
    def payment_info(self):
        """Gets the payment_info of this PurchaseGiftCardRequest.  # noqa: E501

        Contains information about the payment.  # noqa: E501

        :return: The payment_info of this PurchaseGiftCardRequest.  # noqa: E501
        :rtype: CheckoutPaymentInfo
        """
        return self._payment_info

    @payment_info.setter
    def payment_info(self, payment_info):
        """Sets the payment_info of this PurchaseGiftCardRequest.

        Contains information about the payment.  # noqa: E501

        :param payment_info: The payment_info of this PurchaseGiftCardRequest.  # noqa: E501
        :type: CheckoutPaymentInfo
        """

        self._payment_info = payment_info

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
        if issubclass(PurchaseGiftCardRequest, dict):
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
        if not isinstance(other, PurchaseGiftCardRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
