import hashlib
import hmac

class FileHMAC:
    @staticmethod
    def generate_hmac(file_path: str, secret_key: str) -> bytes:
        try:
            with open(file_path, 'rb') as file:
                file_content = file.read()

            key_bytes = secret_key.encode('utf-8')

            mac = hmac.new(key_bytes, file_content, hashlib.sha3_256)
            return mac.digest()

        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
            raise
        except IOError as e:
            print(f"Error reading file: {e}")
            raise

    @staticmethod
    def save_hmac(hmac_value: bytes, output_path: str) -> None:

        try:
            with open(output_path, 'wb') as hmac_file:
                hmac_file.write(hmac_value)
            print(f"HMAC successfully saved to {output_path}")
        except IOError as e:
            print(f"Error saving HMAC: {e}")

    @staticmethod
    def verify_hmac(file_path: str, secret_key: str, hmac_path: str) -> bool:
        try:
            current_hmac = FileHMAC.generate_hmac(file_path, secret_key)

            with open(hmac_path, 'rb') as hmac_file:
                stored_hmac = hmac_file.read()

            is_verified = hmac.compare_digest(current_hmac, stored_hmac)

            print("File Integrity: " +
                  ("VERIFIED" if is_verified else "NOT VERIFIED"))

            return is_verified

        except FileNotFoundError as e:
            print(f"Error: {e}")
            return False
        except IOError as e:
            print(f"Error verifying HMAC: {e}")
            return False
