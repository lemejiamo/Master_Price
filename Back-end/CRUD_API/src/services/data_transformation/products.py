class Product:
    def __init__(
        self,
        id_user: str,
        json_data: dict,
    ):

        self.new_dict = json_data[id_user]
