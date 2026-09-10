import json


HEALTHCHECK_SCHEMA = {
    "name": "sandra_plugin_healthcheck",
    "description": "Verify that the Sandra test plugin is loaded correctly.",
    "parameters": {
        "type": "object",
        "properties": {},
        "required": [],
    },
}


def healthcheck(args: dict, **kwargs) -> str:
    return json.dumps(
        {
            "status": "ok",
            "message": "Sandra Hermes plugin is loaded",
        }
    )


def register(ctx):
    ctx.register_tool(
        name="sandra_plugin_healthcheck",
        toolset="project",
        schema=HEALTHCHECK_SCHEMA,
        handler=healthcheck,
    )
