import pyzipper
import string

def brute_force(string, characters):
  for character in characters:
    new_string = string.replace("{*}", character)
    if new_string.isalnum():
      return character
  return None


if __name__ == "__main__":
  str = "n_^{*}`W{*}5"
  characters = list(string.ascii_letters + string.digits)
  missing_character = brute_force(str, characters)
  if missing_character is not None:
    print(f"The missing character is '{missing_character}'")
  else:
    print("The missing character cannot be found.")


    '''
    with pyzipper.AESZipFile("The_secret.zip") as f:
                f.pwd = 

    '''