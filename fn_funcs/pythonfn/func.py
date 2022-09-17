import io
import json
import logging
import decimal

from fdk import response


def handler(ctx, data: io.BytesIO = None):
    name = "Welcome"
    weight = 0
    height = 0
    bmi = 0.0
    verdict = "Please insert values"
    try:
        body = json.loads(data.getvalue())
        name = body.get("name")
        weight = body.get("weight")
        height = body.get("height")

        if (name == None) :
            name = "Welcome"
        if (weight == None):
            weight = "Enter your weight in kilograms."
        if (height == None):
            height = "Enter your height in meters"
        
        decimal.getcontext().prec = 4
        
        bmi = decimal.Decimal(weight) / decimal.Decimal(height**2)
        
        if (bmi <= 18.4):
            verdict = "Underweight. You should gain weight."
        elif (bmi >= 18.5 and bmi <= 24.9):
            verdict = "Normal"
        elif (bmi >= 25.0 and bmi <= 39.9):
            verdict = "Overweight. You should lose weight."
        elif (bmi >= 40.0):
            verdict = "Obese. You should loose weight."
    
    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    logging.getLogger().info("Inside Python Hello World function")
    return response.Response(
        ctx, response_data=json.dumps(
            {"message": "Hello {0}".format(name) , "Your bmi is": format(bmi),"You are": format(verdict)}),
        headers={"Content-Type": "application/json"}
    )
