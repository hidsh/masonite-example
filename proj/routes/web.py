from masonite.routes import Route

ROUTES = [
        Route.get("/", "WelcomeController@show"),
        Route.get("/login", "LoginController@show"),
        ]
