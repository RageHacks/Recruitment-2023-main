import string

def decrypt(text, key):
    # Convert the text and key to ASCII codes.
    text_codes = [ord(c) for c in text]
    key_codes = [ord(c) for c in key]   

    # Perform an XOR operation on the text and key codes.
    decrypted_codes = [a ^ b for a, b in zip(text_codes, key_codes)]
    
    # Convert the decrypted codes back to text.
    decrypted_text = ''.join([chr(c) for c in decrypted_codes])

    return decrypted_text


# Encrypt the text.
encrypted_text = '|OP`Z<E]|Y\$'

# Get the key.
key = 'Jai Shree Ram!Jai Shree Ram!'

# Decrypt the text.
decrypted_text = decrypt(encrypted_text, key)

# Print the decrypted text.
print(decrypted_text,"\n")

# Store the coordinates in a text file.
with open("Cyber Security Corner\Ashok Vatika-CCube-Medium\coordinates.txt", "w") as f:
    f.write(decrypted_text)



# Search the coordinates on Google Maps and take a screenshot of the location
import webbrowser
import pyautogui

# Get the coordinates from the text file
coordinates = open("Cyber Security Corner\Ashok Vatika-CCube-Medium\coordinates.txt").read()

# Open Google Maps in a web browser
webbrowser.open("https://www.google.com/maps")

# Wait for Google Maps to load
pyautogui.sleep(5)

# Search for the coordinates in Google Maps
pyautogui.typewrite(coordinates)

# Click on the search button
pyautogui.press("Enter")
pyautogui.sleep(5)

# Take a screenshot of the location
pyautogui.screenshot("Cyber Security Corner\Ashok Vatika-CCube-Medium\location.png")