class Credential:
    """
    Class that generates new instances of credentials
    """

    Mycredentials = []  # Empty contact list

    def __init__(self, first_name, last_name, number, email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
