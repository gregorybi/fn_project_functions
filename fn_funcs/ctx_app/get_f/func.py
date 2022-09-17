import io
import json
import logging

from fdk import response


def handler(ctx, data: io.BytesIO = None):
    #new_foo = str(random.randint(0,100))

    logging.getLogger().info("Inside Python random list function")
    #foo = ctx.get("foo")
    old_foo = ctx.Config()["foo"]
    logging.getLogger().info("OLD FOO WAS: "+str(old_foo))
    #ctx.Config()["foo"] = new_foo

    return response.Response(
        ctx, json.dumps({"old_foo": old_foo}),
        headers={"Content-Type": "application/json"}
    )
