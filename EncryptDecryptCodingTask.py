import sys
import os.path
import datetime
from cryptography.fernet import Fernet


class EncryptDecrypt:
    """
    Created by:
    Steve Young, 2021-06-23.
    Python 3.9

    Purpose:
    A program that allows a user to encrypt and decrypt a message (from a file, to a new file). 

    Dependencies:
    Requires the installation of cryptography. Can be done using command:  pip install cryptography

    Notes:
    The user is prompted for:
      - e or d, specifying encryption or decryption.
      - The secret key.
      - The filename to encrypt or decrypt.
    """

    # Constants:
    ACTION_ENCRYPT = "e"
    ACTION_DECRYPT = "d"
    SECRET_KEY = "3ya3VRFu9SNtETmlfAbYAhhf4fqBGA5fBbWmEyQ3QSE="
    DATE_STAMP_FORMAT = "-%Y-%m-%d-%H-%M-%S"

    


    # Functions:


    def process_input(self):
        """
        Purpose:
        Validates the user input from prompts and makes calls to encrypt or decrypt contents to a new file.
        """
      
        action = input("Please enter the letter e for encrpyting, or d for decrypting:")

        # Validate the two allowable inputs, converting to lowercase.

        if str(action.lower()) not in (self.ACTION_ENCRYPT,
                                       self.ACTION_DECRYPT):
            raise ValueError('Invalid input. Must be e or d to specify encrypt or decrypt')

        # Prompt for the secret key and validate it.

        user_key = input("Please enter the secret key (copy and paste it here):")
        self.validate_key(user_key)

        # Perform an encryption or decryption.

        if action == self.ACTION_ENCRYPT:
            message_file = input("Enter the file to encrypt:")
            file_contents = self.read_file(message_file)
            new_file_name = self.encrypt_message(file_contents)

        elif action == self.ACTION_DECRYPT:
            message_file = input("Enter the file to decrypt:")
            file_contents = self.read_file(message_file)
            new_file_name = self.decrypt_message(file_contents)

        print("New file created: %s" % new_file_name)
        


    def validate_key(self, user_key):
        """
        Purpose:
        Checks if the user-supplied secret key matches the expected one.
        Failure (the wrong key) raises an error.
        """

        if self.SECRET_KEY != user_key:
            raise ValueError('Invalid secret key.')



    def read_file(self, file_name):
        """
        Purpose:
        Reads and returns the content of the specified file.
        An invalid filename raises an error.
        """

        # First, validate that the specified file exists. 
        if os.path.isfile(file_name) == False:
            raise FileNotFoundError(file_name)

        # Read and return the file contents.
        message_file = open(file_name, "r")
        file_contents = message_file.read()
        message_file.close()
        return file_contents



    def encrypt_message(self, file_contents):
        """
        Purpose:
        Encrypt content, save to a new file with timestamp.
        """
         
        print("Encrypting file.")
        crypt_key = Fernet(self.SECRET_KEY)
        # Encode the file contents for encryption, then decode for writing to the new file.
        new_message_contents = crypt_key.encrypt(file_contents.encode()).decode()

        file_name = "encrypted%s.txt" % datetime.datetime.now().strftime(self.DATE_STAMP_FORMAT)
        new_file = open(file_name, "w+")
        new_file.write(new_message_contents)
        new_file.close()
        return file_name
        


    def decrypt_message(self, file_contents):
        """
        Purpose:
        Decrypt content, save to a new file with timestamp.
        """

        print("Decrypting file.")

        crypt_key = Fernet(self.SECRET_KEY)
        # Encode the file contents for decryption, then decode for writing to the new file.
        new_message_contents = crypt_key.decrypt(file_contents.encode()).decode()

        file_name = "decrypted%s.txt" % datetime.datetime.now().strftime(self.DATE_STAMP_FORMAT)
        new_file = open(file_name, "w+")
        new_file.write(new_message_contents)
        new_file.close()
        return file_name



# Startup command, this is the entry point for our Python application.
if (__name__ == '__main__'):
    # Run the program.
    run = EncryptDecrypt()
    run.process_input()