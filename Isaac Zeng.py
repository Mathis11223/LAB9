def encode(password):
    password = list(password)
    print(password)
    encoded_list = []
    string_encoded = ''
    for i in range(len(password)):
        encoded = int(password[int(i)]) + 3
        encoded_list.append(encoded)
        if encoded_list[i] >= 10:
            encoded_list[i] -= 10
    for i in range(len(encoded_list)):
        string_encoded += str(encoded_list[i])
    print(encoded_list)
    print(string_encoded)

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")
        option = input("Please enter an option: ")
        if user == "1":
            password_to_encode = input("Please enter an your password to encode: ")
            encoded_password = encode(password_to_encode)
            print("Your password has been encoded and stored!\n")
        if user == "2":
            decoded_password = decode(password_to_decode)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")
        if user == "3":
            break


if __name__ == "__main__":
    main()

