# coding: utf-8

"""
    Upstox Developer API

    Build your App on the Upstox platform  ![Banner](https://api.upstox.com/api-docs/images/banner.jpg \"banner\")  # Introduction  Upstox API is a set of rest APIs that provide data required to build a complete investment and trading platform. Execute orders in real time, manage user portfolio, stream live market data (using Websocket), and more, with the easy to understand API collection.  All requests are over HTTPS and the requests are sent with the content-type ‘application/json’. Developers have the option of choosing the response type as JSON or CSV for a few API calls.  To be able to use these APIs you need to create an App in the Developer Console and generate your **apiKey** and **apiSecret**. You can use a redirect URL which will be called after the login flow.  If you are a **trader**, you can directly create apps from Upstox mobile app or the desktop platform itself from **Apps** sections inside the **Account** Tab. Head over to <a href=\"http://account.upstox.com/developer/apps\" target=\"_blank\">account.upstox.com/developer/apps</a>.</br> If you are a **business** looking to integrate Upstox APIs, reach out to us and we will get a custom app created for you in no time.  It is highly recommended that you do not embed the **apiSecret** in your frontend app. Create a remote backend which does the handshake on behalf of the frontend app. Marking the apiSecret in the frontend app will make your app vulnerable to threats and potential issues.   # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PositionData(object):
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
        'exchange': 'str',
        'multiplier': 'float',
        'value': 'float',
        'pnl': 'float',
        'product': 'str',
        'instrument_token': 'str',
        'average_price': 'float',
        'buy_value': 'float',
        'overnight_quantity': 'int',
        'day_buy_value': 'float',
        'day_buy_price': 'float',
        'overnight_buy_amount': 'float',
        'overnight_buy_quantity': 'int',
        'day_buy_quantity': 'int',
        'day_sell_value': 'float',
        'day_sell_price': 'float',
        'overnight_sell_amount': 'float',
        'overnight_sell_quantity': 'int',
        'day_sell_quantity': 'int',
        'quantity': 'int',
        'last_price': 'float',
        'unrealised': 'float',
        'realised': 'float',
        'sell_value': 'float',
        'tradingsymbol': 'str',
        'trading_symbol': 'str',
        'close_price': 'float',
        'buy_price': 'float',
        'sell_price': 'float'
    }

    attribute_map = {
        'exchange': 'exchange',
        'multiplier': 'multiplier',
        'value': 'value',
        'pnl': 'pnl',
        'product': 'product',
        'instrument_token': 'instrument_token',
        'average_price': 'average_price',
        'buy_value': 'buy_value',
        'overnight_quantity': 'overnight_quantity',
        'day_buy_value': 'day_buy_value',
        'day_buy_price': 'day_buy_price',
        'overnight_buy_amount': 'overnight_buy_amount',
        'overnight_buy_quantity': 'overnight_buy_quantity',
        'day_buy_quantity': 'day_buy_quantity',
        'day_sell_value': 'day_sell_value',
        'day_sell_price': 'day_sell_price',
        'overnight_sell_amount': 'overnight_sell_amount',
        'overnight_sell_quantity': 'overnight_sell_quantity',
        'day_sell_quantity': 'day_sell_quantity',
        'quantity': 'quantity',
        'last_price': 'last_price',
        'unrealised': 'unrealised',
        'realised': 'realised',
        'sell_value': 'sell_value',
        'tradingsymbol': 'tradingsymbol',
        'trading_symbol': 'trading_symbol',
        'close_price': 'close_price',
        'buy_price': 'buy_price',
        'sell_price': 'sell_price'
    }

    def __init__(self, exchange=None, multiplier=None, value=None, pnl=None, product=None, instrument_token=None, average_price=None, buy_value=None, overnight_quantity=None, day_buy_value=None, day_buy_price=None, overnight_buy_amount=None, overnight_buy_quantity=None, day_buy_quantity=None, day_sell_value=None, day_sell_price=None, overnight_sell_amount=None, overnight_sell_quantity=None, day_sell_quantity=None, quantity=None, last_price=None, unrealised=None, realised=None, sell_value=None, tradingsymbol=None, trading_symbol=None, close_price=None, buy_price=None, sell_price=None):  # noqa: E501
        """PositionData - a model defined in Swagger"""  # noqa: E501
        self._exchange = None
        self._multiplier = None
        self._value = None
        self._pnl = None
        self._product = None
        self._instrument_token = None
        self._average_price = None
        self._buy_value = None
        self._overnight_quantity = None
        self._day_buy_value = None
        self._day_buy_price = None
        self._overnight_buy_amount = None
        self._overnight_buy_quantity = None
        self._day_buy_quantity = None
        self._day_sell_value = None
        self._day_sell_price = None
        self._overnight_sell_amount = None
        self._overnight_sell_quantity = None
        self._day_sell_quantity = None
        self._quantity = None
        self._last_price = None
        self._unrealised = None
        self._realised = None
        self._sell_value = None
        self._tradingsymbol = None
        self._trading_symbol = None
        self._close_price = None
        self._buy_price = None
        self._sell_price = None
        self.discriminator = None
        if exchange is not None:
            self.exchange = exchange
        if multiplier is not None:
            self.multiplier = multiplier
        if value is not None:
            self.value = value
        if pnl is not None:
            self.pnl = pnl
        if product is not None:
            self.product = product
        if instrument_token is not None:
            self.instrument_token = instrument_token
        if average_price is not None:
            self.average_price = average_price
        if buy_value is not None:
            self.buy_value = buy_value
        if overnight_quantity is not None:
            self.overnight_quantity = overnight_quantity
        if day_buy_value is not None:
            self.day_buy_value = day_buy_value
        if day_buy_price is not None:
            self.day_buy_price = day_buy_price
        if overnight_buy_amount is not None:
            self.overnight_buy_amount = overnight_buy_amount
        if overnight_buy_quantity is not None:
            self.overnight_buy_quantity = overnight_buy_quantity
        if day_buy_quantity is not None:
            self.day_buy_quantity = day_buy_quantity
        if day_sell_value is not None:
            self.day_sell_value = day_sell_value
        if day_sell_price is not None:
            self.day_sell_price = day_sell_price
        if overnight_sell_amount is not None:
            self.overnight_sell_amount = overnight_sell_amount
        if overnight_sell_quantity is not None:
            self.overnight_sell_quantity = overnight_sell_quantity
        if day_sell_quantity is not None:
            self.day_sell_quantity = day_sell_quantity
        if quantity is not None:
            self.quantity = quantity
        if last_price is not None:
            self.last_price = last_price
        if unrealised is not None:
            self.unrealised = unrealised
        if realised is not None:
            self.realised = realised
        if sell_value is not None:
            self.sell_value = sell_value
        if tradingsymbol is not None:
            self.tradingsymbol = tradingsymbol
        if trading_symbol is not None:
            self.trading_symbol = trading_symbol
        if close_price is not None:
            self.close_price = close_price
        if buy_price is not None:
            self.buy_price = buy_price
        if sell_price is not None:
            self.sell_price = sell_price

    @property
    def exchange(self):
        """Gets the exchange of this PositionData.  # noqa: E501

        Exchange to which the order is associated  # noqa: E501

        :return: The exchange of this PositionData.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this PositionData.

        Exchange to which the order is associated  # noqa: E501

        :param exchange: The exchange of this PositionData.  # noqa: E501
        :type: str
        """
        self._exchange = exchange

    @property
    def multiplier(self):
        """Gets the multiplier of this PositionData.  # noqa: E501

        The quantity/lot size multiplier used for calculating P&Ls  # noqa: E501

        :return: The multiplier of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this PositionData.

        The quantity/lot size multiplier used for calculating P&Ls  # noqa: E501

        :param multiplier: The multiplier of this PositionData.  # noqa: E501
        :type: float
        """

        self._multiplier = multiplier

    @property
    def value(self):
        """Gets the value of this PositionData.  # noqa: E501

        Net value of the position  # noqa: E501

        :return: The value of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PositionData.

        Net value of the position  # noqa: E501

        :param value: The value of this PositionData.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def pnl(self):
        """Gets the pnl of this PositionData.  # noqa: E501

        Profit and loss - net returns on the position  # noqa: E501

        :return: The pnl of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._pnl

    @pnl.setter
    def pnl(self, pnl):
        """Sets the pnl of this PositionData.

        Profit and loss - net returns on the position  # noqa: E501

        :param pnl: The pnl of this PositionData.  # noqa: E501
        :type: float
        """

        self._pnl = pnl

    @property
    def product(self):
        """Gets the product of this PositionData.  # noqa: E501

        Shows if the order was either Intraday, Delivery, CO or OCO  # noqa: E501

        :return: The product of this PositionData.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this PositionData.

        Shows if the order was either Intraday, Delivery, CO or OCO  # noqa: E501

        :param product: The product of this PositionData.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def instrument_token(self):
        """Gets the instrument_token of this PositionData.  # noqa: E501

        Key issued by Upstox for the instrument  # noqa: E501

        :return: The instrument_token of this PositionData.  # noqa: E501
        :rtype: str
        """
        return self._instrument_token

    @instrument_token.setter
    def instrument_token(self, instrument_token):
        """Sets the instrument_token of this PositionData.

        Key issued by Upstox for the instrument  # noqa: E501

        :param instrument_token: The instrument_token of this PositionData.  # noqa: E501
        :type: str
        """

        self._instrument_token = instrument_token

    @property
    def average_price(self):
        """Gets the average_price of this PositionData.  # noqa: E501

        Average price at which the net position quantity was acquired  # noqa: E501

        :return: The average_price of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._average_price

    @average_price.setter
    def average_price(self, average_price):
        """Sets the average_price of this PositionData.

        Average price at which the net position quantity was acquired  # noqa: E501

        :param average_price: The average_price of this PositionData.  # noqa: E501
        :type: float
        """

        self._average_price = average_price

    @property
    def buy_value(self):
        """Gets the buy_value of this PositionData.  # noqa: E501

        Net value of the bought quantities  # noqa: E501

        :return: The buy_value of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._buy_value

    @buy_value.setter
    def buy_value(self, buy_value):
        """Sets the buy_value of this PositionData.

        Net value of the bought quantities  # noqa: E501

        :param buy_value: The buy_value of this PositionData.  # noqa: E501
        :type: float
        """

        self._buy_value = buy_value

    @property
    def overnight_quantity(self):
        """Gets the overnight_quantity of this PositionData.  # noqa: E501

        Quantity held previously and carried forward over night  # noqa: E501

        :return: The overnight_quantity of this PositionData.  # noqa: E501
        :rtype: int
        """
        return self._overnight_quantity

    @overnight_quantity.setter
    def overnight_quantity(self, overnight_quantity):
        """Sets the overnight_quantity of this PositionData.

        Quantity held previously and carried forward over night  # noqa: E501

        :param overnight_quantity: The overnight_quantity of this PositionData.  # noqa: E501
        :type: int
        """

        self._overnight_quantity = overnight_quantity

    @property
    def day_buy_value(self):
        """Gets the day_buy_value of this PositionData.  # noqa: E501

        Amount at which the quantity is bought during the day  # noqa: E501

        :return: The day_buy_value of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._day_buy_value

    @day_buy_value.setter
    def day_buy_value(self, day_buy_value):
        """Sets the day_buy_value of this PositionData.

        Amount at which the quantity is bought during the day  # noqa: E501

        :param day_buy_value: The day_buy_value of this PositionData.  # noqa: E501
        :type: float
        """

        self._day_buy_value = day_buy_value

    @property
    def day_buy_price(self):
        """Gets the day_buy_price of this PositionData.  # noqa: E501

        Average price at which the day qty was bought. Default is empty string  # noqa: E501

        :return: The day_buy_price of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._day_buy_price

    @day_buy_price.setter
    def day_buy_price(self, day_buy_price):
        """Sets the day_buy_price of this PositionData.

        Average price at which the day qty was bought. Default is empty string  # noqa: E501

        :param day_buy_price: The day_buy_price of this PositionData.  # noqa: E501
        :type: float
        """

        self._day_buy_price = day_buy_price

    @property
    def overnight_buy_amount(self):
        """Gets the overnight_buy_amount of this PositionData.  # noqa: E501

        Amount at which the quantity was bought in the previous session  # noqa: E501

        :return: The overnight_buy_amount of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._overnight_buy_amount

    @overnight_buy_amount.setter
    def overnight_buy_amount(self, overnight_buy_amount):
        """Sets the overnight_buy_amount of this PositionData.

        Amount at which the quantity was bought in the previous session  # noqa: E501

        :param overnight_buy_amount: The overnight_buy_amount of this PositionData.  # noqa: E501
        :type: float
        """

        self._overnight_buy_amount = overnight_buy_amount

    @property
    def overnight_buy_quantity(self):
        """Gets the overnight_buy_quantity of this PositionData.  # noqa: E501

        Quantity bought in the previous session  # noqa: E501

        :return: The overnight_buy_quantity of this PositionData.  # noqa: E501
        :rtype: int
        """
        return self._overnight_buy_quantity

    @overnight_buy_quantity.setter
    def overnight_buy_quantity(self, overnight_buy_quantity):
        """Sets the overnight_buy_quantity of this PositionData.

        Quantity bought in the previous session  # noqa: E501

        :param overnight_buy_quantity: The overnight_buy_quantity of this PositionData.  # noqa: E501
        :type: int
        """

        self._overnight_buy_quantity = overnight_buy_quantity

    @property
    def day_buy_quantity(self):
        """Gets the day_buy_quantity of this PositionData.  # noqa: E501

        Quantity bought during the day  # noqa: E501

        :return: The day_buy_quantity of this PositionData.  # noqa: E501
        :rtype: int
        """
        return self._day_buy_quantity

    @day_buy_quantity.setter
    def day_buy_quantity(self, day_buy_quantity):
        """Sets the day_buy_quantity of this PositionData.

        Quantity bought during the day  # noqa: E501

        :param day_buy_quantity: The day_buy_quantity of this PositionData.  # noqa: E501
        :type: int
        """

        self._day_buy_quantity = day_buy_quantity

    @property
    def day_sell_value(self):
        """Gets the day_sell_value of this PositionData.  # noqa: E501

        Amount at which the quantity is sold during the day  # noqa: E501

        :return: The day_sell_value of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._day_sell_value

    @day_sell_value.setter
    def day_sell_value(self, day_sell_value):
        """Sets the day_sell_value of this PositionData.

        Amount at which the quantity is sold during the day  # noqa: E501

        :param day_sell_value: The day_sell_value of this PositionData.  # noqa: E501
        :type: float
        """

        self._day_sell_value = day_sell_value

    @property
    def day_sell_price(self):
        """Gets the day_sell_price of this PositionData.  # noqa: E501

        Average price at which the day quantity was sold  # noqa: E501

        :return: The day_sell_price of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._day_sell_price

    @day_sell_price.setter
    def day_sell_price(self, day_sell_price):
        """Sets the day_sell_price of this PositionData.

        Average price at which the day quantity was sold  # noqa: E501

        :param day_sell_price: The day_sell_price of this PositionData.  # noqa: E501
        :type: float
        """

        self._day_sell_price = day_sell_price

    @property
    def overnight_sell_amount(self):
        """Gets the overnight_sell_amount of this PositionData.  # noqa: E501

        Amount at which the quantity was sold in the previous session  # noqa: E501

        :return: The overnight_sell_amount of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._overnight_sell_amount

    @overnight_sell_amount.setter
    def overnight_sell_amount(self, overnight_sell_amount):
        """Sets the overnight_sell_amount of this PositionData.

        Amount at which the quantity was sold in the previous session  # noqa: E501

        :param overnight_sell_amount: The overnight_sell_amount of this PositionData.  # noqa: E501
        :type: float
        """

        self._overnight_sell_amount = overnight_sell_amount

    @property
    def overnight_sell_quantity(self):
        """Gets the overnight_sell_quantity of this PositionData.  # noqa: E501

        Quantity sold short in the previous session  # noqa: E501

        :return: The overnight_sell_quantity of this PositionData.  # noqa: E501
        :rtype: int
        """
        return self._overnight_sell_quantity

    @overnight_sell_quantity.setter
    def overnight_sell_quantity(self, overnight_sell_quantity):
        """Sets the overnight_sell_quantity of this PositionData.

        Quantity sold short in the previous session  # noqa: E501

        :param overnight_sell_quantity: The overnight_sell_quantity of this PositionData.  # noqa: E501
        :type: int
        """

        self._overnight_sell_quantity = overnight_sell_quantity

    @property
    def day_sell_quantity(self):
        """Gets the day_sell_quantity of this PositionData.  # noqa: E501

        Quantity sold during the day  # noqa: E501

        :return: The day_sell_quantity of this PositionData.  # noqa: E501
        :rtype: int
        """
        return self._day_sell_quantity

    @day_sell_quantity.setter
    def day_sell_quantity(self, day_sell_quantity):
        """Sets the day_sell_quantity of this PositionData.

        Quantity sold during the day  # noqa: E501

        :param day_sell_quantity: The day_sell_quantity of this PositionData.  # noqa: E501
        :type: int
        """

        self._day_sell_quantity = day_sell_quantity

    @property
    def quantity(self):
        """Gets the quantity of this PositionData.  # noqa: E501

        Quantity left after nullifying Day and CF buy quantity towards Day and CF sell quantity  # noqa: E501

        :return: The quantity of this PositionData.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PositionData.

        Quantity left after nullifying Day and CF buy quantity towards Day and CF sell quantity  # noqa: E501

        :param quantity: The quantity of this PositionData.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def last_price(self):
        """Gets the last_price of this PositionData.  # noqa: E501

        Last traded market price of the instrument  # noqa: E501

        :return: The last_price of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._last_price

    @last_price.setter
    def last_price(self, last_price):
        """Sets the last_price of this PositionData.

        Last traded market price of the instrument  # noqa: E501

        :param last_price: The last_price of this PositionData.  # noqa: E501
        :type: float
        """

        self._last_price = last_price

    @property
    def unrealised(self):
        """Gets the unrealised of this PositionData.  # noqa: E501

        Day PnL generated against open positions  # noqa: E501

        :return: The unrealised of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._unrealised

    @unrealised.setter
    def unrealised(self, unrealised):
        """Sets the unrealised of this PositionData.

        Day PnL generated against open positions  # noqa: E501

        :param unrealised: The unrealised of this PositionData.  # noqa: E501
        :type: float
        """

        self._unrealised = unrealised

    @property
    def realised(self):
        """Gets the realised of this PositionData.  # noqa: E501

        Day PnL generated against closed positions  # noqa: E501

        :return: The realised of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._realised

    @realised.setter
    def realised(self, realised):
        """Sets the realised of this PositionData.

        Day PnL generated against closed positions  # noqa: E501

        :param realised: The realised of this PositionData.  # noqa: E501
        :type: float
        """

        self._realised = realised

    @property
    def sell_value(self):
        """Gets the sell_value of this PositionData.  # noqa: E501

        Net value of the sold quantities  # noqa: E501

        :return: The sell_value of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._sell_value

    @sell_value.setter
    def sell_value(self, sell_value):
        """Sets the sell_value of this PositionData.

        Net value of the sold quantities  # noqa: E501

        :param sell_value: The sell_value of this PositionData.  # noqa: E501
        :type: float
        """

        self._sell_value = sell_value

    @property
    def tradingsymbol(self):
        """Gets the tradingsymbol of this PositionData.  # noqa: E501

        Shows the trading symbol of the instrument  # noqa: E501

        :return: The tradingsymbol of this PositionData.  # noqa: E501
        :rtype: str
        """
        return self._tradingsymbol

    @tradingsymbol.setter
    def tradingsymbol(self, tradingsymbol):
        """Sets the tradingsymbol of this PositionData.

        Shows the trading symbol of the instrument  # noqa: E501

        :param tradingsymbol: The tradingsymbol of this PositionData.  # noqa: E501
        :type: str
        """

        self._tradingsymbol = tradingsymbol

    @property
    def trading_symbol(self):
        """Gets the trading_symbol of this PositionData.  # noqa: E501

        Shows the trading symbol of the instrument  # noqa: E501

        :return: The trading_symbol of this PositionData.  # noqa: E501
        :rtype: str
        """
        return self._trading_symbol

    @trading_symbol.setter
    def trading_symbol(self, trading_symbol):
        """Sets the trading_symbol of this PositionData.

        Shows the trading symbol of the instrument  # noqa: E501

        :param trading_symbol: The trading_symbol of this PositionData.  # noqa: E501
        :type: str
        """

        self._trading_symbol = trading_symbol

    @property
    def close_price(self):
        """Gets the close_price of this PositionData.  # noqa: E501

        Closing price of the instrument from the last trading day  # noqa: E501

        :return: The close_price of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._close_price

    @close_price.setter
    def close_price(self, close_price):
        """Sets the close_price of this PositionData.

        Closing price of the instrument from the last trading day  # noqa: E501

        :param close_price: The close_price of this PositionData.  # noqa: E501
        :type: float
        """

        self._close_price = close_price

    @property
    def buy_price(self):
        """Gets the buy_price of this PositionData.  # noqa: E501

        Average price at which quantities were bought  # noqa: E501

        :return: The buy_price of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._buy_price

    @buy_price.setter
    def buy_price(self, buy_price):
        """Sets the buy_price of this PositionData.

        Average price at which quantities were bought  # noqa: E501

        :param buy_price: The buy_price of this PositionData.  # noqa: E501
        :type: float
        """

        self._buy_price = buy_price

    @property
    def sell_price(self):
        """Gets the sell_price of this PositionData.  # noqa: E501

        Average price at which quantities were sold  # noqa: E501

        :return: The sell_price of this PositionData.  # noqa: E501
        :rtype: float
        """
        return self._sell_price

    @sell_price.setter
    def sell_price(self, sell_price):
        """Sets the sell_price of this PositionData.

        Average price at which quantities were sold  # noqa: E501

        :param sell_price: The sell_price of this PositionData.  # noqa: E501
        :type: float
        """

        self._sell_price = sell_price

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
        if issubclass(PositionData, dict):
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
        if not isinstance(other, PositionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
