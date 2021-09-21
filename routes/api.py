from flask import Blueprint

api_blueprint = Blueprint(
    "api",
    __name__,
)


@api_blueprint.route("/")
def index():
    return "api index route"
