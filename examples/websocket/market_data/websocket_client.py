import asyncio
import json
import ssl
import websockets
import requests
from google.protobuf.json_format import MessageToDict
import urllib.parse
import os
import sys
from threading import Thread
from time import sleep
import pandas as pd
os.chdir("X:/richa - Personal/Documents/AlgoTrading/Richa/upstox-python/examples/websocket/market_data/")
import MarketDataFeedV3_pb2 as pb
import upstox_access as ua


apikey = '2a3bbf7d-8bd5-49f5-9a66-6e5388308e63'
secretkey = 'alqbcayzko'
rurl = urllib.parse.quote('https://www.google.com', safe = "")
uri = f'https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={apikey}&redirect_uri={rurl}'
uri
code = 'fsYpxW'
access_token=ua.authorization(apikey,secretkey,code)['access_token']
access_token


#filename =f"X:/richa - Personal/Documents/AlgoTrading/Richa/access_token.txt"
access_token=open('access_token.txt').read().strip()
  


symbols=['NSE_INDEX|Nifty 50']  ##['NSE_EQ|INE040A01034','MCX_FO|453231','NSE_FO|98964']
marketData=ua.market_data(access_token,symbols)
ltp=marketData['close'].item()
ltp
  

def get_market_data_feed_authorize_v3(access_token):
    """Get authorization for market data feed."""
    
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer '+access_token
    }
    url = 'https://api.upstox.com/v3/feed/market-data-feed/authorize'
    api_response = requests.get(url=url, headers=headers)
    return api_response.json()




def decode_protobuf(buffer):
    """Decode protobuf message."""
    feed_response = pb.FeedResponse()
    feed_response.ParseFromString(buffer)
    return feed_response


async def fetch_market_data():
    """Fetch market data using WebSocket and print it."""

    # Create default SSL context
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Get market data feed authorization
    response = get_market_data_feed_authorize_v3(access_token)
    print(response)
    # Connect to the WebSocket with SSL context
    async with websockets.connect(response["data"]["authorized_redirect_uri"], ssl=ssl_context) as websocket:
        print('Connection established')

        await asyncio.sleep(1)  # Wait for 1 second

        # Data to be sent over the WebSocket
        data = {
            "guid": "someguid",
            "method": "sub",
            "data": {
                "mode": "full",
                "instrumentKeys": [ "NSE_INDEX|Nifty 50"]
            }
        }

        # Convert data to binary and send over WebSocket
        binary_data = json.dumps(data).encode('utf-8')
        print(binary_data)
        await websocket.send(binary_data)

        # Continuously receive and decode data from WebSocket
        while True:
            message = await websocket.recv()
            decoded_data = decode_protobuf(message)
            print(decoded_data)

            # Convert the decoded data to a dictionary
            data_dict = MessageToDict(decoded_data)

            # Print the dictionary representation
            print(json.dumps(data_dict))
            
# Execute the function to fetch market data
asyncio.run(fetch_market_data())
