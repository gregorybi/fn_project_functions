import io
import json
import logging
import requests

from fdk import response


def handler(ctx, data: io.BytesIO = None):
    result = 0
    phi = (1 + 5**0.5)/2.0
    #url = "http://localhost:8080/t/demo_app/fibo_f"
    try:
        body = json.loads(data.getvalue())
        n = body.get("N")
    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    logging.getLogger().info("Inside Python fibo function")

    if n == 1 or n == 2:
        result = 1
    else:
        try:
            result = int(round((phi**n - (1-phi)**n) / 5**0.5)) 
            #r_1 = requests.get(url, json={"N": n-1})
            #data_1 = r_1.json()
            #n_1 = data_1.get("result")
            #r_2 = requests.get(url, json={"N": n-2})
            #data_2 = r_2.json()
            #n_2 = data_2.get("result")
            #result = n_1 #+ n_2
        except (Exception)as ex:
            logging.getLogger().info('I F-ED UP' + str(ex))


    return response.Response(
        ctx, response_data=json.dumps(
            {"result": result}),
        headers={"Content-Type": "application/json"}
    )
