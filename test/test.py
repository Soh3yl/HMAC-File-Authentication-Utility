import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from HMAC_File_Authenticator.HMACFileAuthenticator import FileHMAC

def main():

    # Example file path
    file_name = 'secert.txt'
    file_path = f'test/text_file/{file_name}'
    secret_key = 'MySecurePassword123!'
    hmac_path = f'test/generated_HMAC_file/{file_name}.hmac'

    # Create a sample file
    with open(file_path, 'w') as f:
        f.write("This is a document written by Soheyl and should be secure!")

    try:
        # Generate HMAC
        hmac_value = FileHMAC.generate_hmac(file_path, secret_key)
        
        # Save HMAC
        FileHMAC.save_hmac(hmac_value, hmac_path)
        
        # Verify HMAC
        #is_authentic = FileHMAC.verify_hmac(file_path, secret_key, hmac_path)
        
        # Modify the file
        #with open(file_path, 'a') as f:
            #f.write(" Additional content.")
        
        # Verify with modified file (should fail)
        #FileHMAC.verify_hmac(file_path, secret_key, hmac_path)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
