class SWAPIClient():
    def __init__(self):
        # Nothing to do yet
        pass
    
    def get_data(self, character_name):
        return {}

    def get_swapi_data(self):
        """
        This is a documentation comment in Python, it is not executed but informs tooling.

        This function is a catch-all to orchestrate the SWAPI data that backs the front-end. It should
        communicate with the API and clean it up to send to the route handler that sends it to the
        front end.

        browser <-> flask-server <-> SWAPIClient <-> SWAPI
        """
        try:
            character_data = self.get_data("Luke Skywalker")
        except Exception as ex:
            return {"error": True, "message": str(ex)}

        # TODO: Merge with other data? From DB?
        # TODO: Test all of these functions, structural test for this function
        # etc...
        return character_data