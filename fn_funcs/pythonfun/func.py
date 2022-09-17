import io
import logging

from fdk import response

def handler(ctx, data: io.BytesIO = None):
    logging.getLogger().info("Got incoming request for URL %s with headers %s", ctx.RequestURL(), ctx.HTTPHeaders())
    ctx.SetResponseHeaders({"Location": "http://www.example.com"}, 302)
    return response.Response(ctx, response_data="Page moved from %s")
    

