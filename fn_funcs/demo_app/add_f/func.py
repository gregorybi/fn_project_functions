import io
import json
import logging
import statistics

from fdk import response


def handler(ctx, data: io.BytesIO = None):
    ls = []
    try:
        body = json.loads(data.getvalue())
        ls = body.get("nums")
    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    logging.getLogger().info("Inside Python array_sum function")
    result = sum(ls)
    max_elem = max(ls)
    num_of_elems = len(ls)
    median_of_elems = statistics.median(ls)

    return response.Response(
        ctx, response_data=json.dumps(
            {"sum": result, 
            "max": max_elem, 
            "number of elements": num_of_elems,
            "median of elements": median_of_elems}),
        headers={"Content-Type": "application/json"}
    )
