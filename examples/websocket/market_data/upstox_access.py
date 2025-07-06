# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 00:22:09 2025

@author: richa
"""
import requests
import json
import pandas as pd
def authorization(x,y,z):
    url_auth = 'https://api.upstox.com/v2/login/authorization/token' 
    headers_auth = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'}
    
    data_auth = {'code' : z,
        'client_id' : x,
        'client_secret' : y,
        'redirect_uri' : 'https://www.google.com' ,
        'grant_type' : 'authorization_code'}
    
    response = requests.post(url_auth, headers = headers_auth, data = data_auth)
    return response.json()


def make_request(method, url, headers = None, params = None, data = None):
    response = None
    try:
        if method == 'GET':
            response = requests.get(url, headers = headers, params = params)
        elif method == 'POST':
            response = requests.post(url, headers = headers, params = params, json = data)
        elif method == 'PUT':
            response = requests.put(url, headers = headers, params = params, json = data)
        else:
            raise ValueError('Invalid HTTP method.')

        if response.status_code == 200:
            return response
        else:
            return response

    except request.exceptions.RequestException as e:
        print(f'An error occuredL {e}')
        return None
    
def market_data(access_token,symbols):
    url = 'https://api.upstox.com/v2/market-quote/quotes' 
    headers = {'accept' : 'application/json',
               'Authorization' : f'Bearer {access_token}'}
    params = {'symbol':symbols}
    response = make_request('GET', url, headers = headers, params = params)
    resp=json.loads(response.text)
    data=pd.DataFrame(resp)
    df=pd.DataFrame()
    df['Symbol']=data.index
    for j in range(len(pd.DataFrame(resp))):
        df.loc[j,'open']=data['data'].iloc[j]['ohlc']['open']
        df.loc[j,'high']=data['data'].iloc[j]['ohlc']['high']
        df.loc[j,'low']=data['data'].iloc[j]['ohlc']['low']
        df.loc[j,'close']=data['data'].iloc[j]['ohlc']['close']
        df.loc[j,'instrument_token']=data['data'].iloc[j]['instrument_token']
        df.loc[j,'symbol']=data['data'].iloc[j]['symbol']
        df.loc[j,'last_price']=data['data'].iloc[j]['last_price']
        df.loc[j,'average_price']=data['data'].iloc[j]['average_price']
        df.loc[j,'oi']=data['data'].iloc[j]['oi']
        df.loc[j,'net_change']=data['data'].iloc[j]['net_change']
        df.loc[j,'oi_day_high']=data['data'].iloc[j]['oi_day_high']
        df.loc[j,'oi_day_low']=data['data'].iloc[j]['oi_day_low']
    return df       