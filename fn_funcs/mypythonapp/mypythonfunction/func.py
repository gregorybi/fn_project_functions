import io
import json
import logging
import pandas as pd
import requests

from fdk import response


def handler(ctx, data: io.BytesIO = None):
    url = ""
    desc = ""
    try:
        body = json.loads(data.getvalue())
        url = body.get("url")
        r = requests.get(url, allow_redirects=True)
        open('/tmp/file4describe.csv', 'wb').write(r.content)
        data = pd.read_csv("/tmp/file4describe.csv")
        desc = str(data.describe)
        logging.getLogger().info('* Describe:'+desc)
    except (Exception, ValueError) as ex:
        logging.getLogger().error('Error processing: ' + str(ex))

    logging.getLogger().info("Inside Python Describe Function")
    return response.Response(
        ctx, response_data=json.dumps(
            {"DataFrame.describe": format(desc)}),
        headers={"Content-Type": "application/json"}
    )
