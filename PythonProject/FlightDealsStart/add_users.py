import requests


user_add_url = "https://api.sheety.co/714305910239e5787bf0d55849d16ac1/flightDealsSb/users"
BEARER_TOKEN = "Bearer askldjaskldj1201234908asdnklasd091njkxzn90012094u1912e"

keep_add_user = True
while keep_add_user:
    print("Seunghoon's flight")

    firstname = input("First name? ")
    lastname = input("Last name? ")
    email = input("Email? ")



    header = {
        "Authorization": BEARER_TOKEN
    }

    user_body = {
      "user": {
        "firstName": firstname,
        "lastName": lastname,
        "email": email
      }
    }

    response = requests.post(url=user_add_url, json=user_body, headers=header)
    response.raise_for_status()
    print(response.text)

    if input("Continue? Y/N ").lower() == "n":
        keep_add_user = False