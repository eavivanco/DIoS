import base64

def deco(base64_text):
    base64_img_bytes = base64_text.encode('utf-8')
    with open('decoded_image.png', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)
    print("The photo was succesfully decoded, check the files!")