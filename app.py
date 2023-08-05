from flask import Flask, request, jsonify

app = Flask(__name__)

class EncryptorDecryptor:
    def process(self, message):
        return message  # Replace this with your encryption and decryption logic

class XORCipher(EncryptorDecryptor):
    def __init__(self, secret_key):
        self.key = secret_key

    def process(self, message):
        processed_message = ''
        for i in range(len(message)):
            processed_message += chr(ord(message[i]) ^ ord(self.key[i % len(self.key)]))
        return processed_message

class CommonAlgorithm(EncryptorDecryptor):
    def process(self, message):
        processed_message = ''
        for i in range(len(message)):
            processed_message += chr(ord(message[i]) + 1)
        return processed_message

def main():
    ch = 1

    while ch != 0:
        try:
            print("Enter 'E' to encrypt or 'D' to decrypt a message: ")
            choice = input().strip().lower()

            if choice not in ['e', 'd']:
                raise ValueError("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")

            processor = None

            if choice == 'e':
                print("Enter the message to encrypt: ")
                message = input()

                print("Enter the secret key (leave empty for common encryption): ")
                key = input().strip()

                if key:
                    processor = XORCipher(key)
                else:
                    processor = CommonAlgorithm()

                encrypted = processor.process(message)
                print("Encrypted message:", encrypted)
            else:
                print("Enter the message to decrypt: ")
                message = input()

                print("Enter the secret key (leave empty for common encryption): ")
                key = input().strip()

                if key:
                    processor = XORCipher(key)
                else:
                    processor = CommonAlgorithm()

                decrypted = processor.process(message)
                print("Decrypted message:", decrypted)

        except Exception as e:
            print("Error:", e)

        print("\nPress 1 to Continue; Press 0 to Exit\n")
        ch = int(input())

if __name__ == "__main__":
    main()

def index():
    return jsonify('index.html')

@app.route('/', methods=['POST'])
def process_data():
    data = request.get_json()
    choice = data.get('choice')
    message = data.get('message')
    key = data.get('key')

    try:
        processor = EncryptorDecryptor()
        result = ""

        if choice == "encrypt":
            result = processor.process(message)
        elif choice == "decrypt":
            result = processor.process(message)
        else:
            raise ValueError("Invalid choice. Please choose 'encrypt' or 'decrypt'.")

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)