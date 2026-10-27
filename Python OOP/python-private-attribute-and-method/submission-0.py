class PasswordManager:
    def __init__(self, password: str):
        self.__password = password
        pass  
    

    def __priv_pass(self):
        return self.__password

    def verify_password(self, password:str):

        if self.__priv_pass() == password:
            return True
        else: return False
    # TODO: Implement the verify_password method




# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
