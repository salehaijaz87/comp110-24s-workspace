"""Practice class wroting."""
# definition
class Profile:

    username: str
    private: bool

    def __init__(self, username_input) -> None:
        """Create a new Profile object."""
        self.username = username_input
        self.private = True

    def tweet(self, msg: str) -> None:
        """tweet fucntion"""
        if self.private is False:
            print(msg)
    
#Instantiation
user1: Profile = Profile("110_rulez")  #calls init
user1.private = False
user1.tweet(user1, "OOP is cool!")

        