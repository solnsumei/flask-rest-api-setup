from src.api.resources.auth import Register


def routes(api):
    api.add_resource(Register, '/signup')


def admin_routes(admin_api):
    pass
