import base64

def enco(photo_name):
    with open(photo_name, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_text = base64_encoded_data.decode('utf-8')

    print(f"The encoded image text is \n: {base64_text}")
    return(base64_text)