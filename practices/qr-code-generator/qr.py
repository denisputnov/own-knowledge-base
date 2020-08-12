import qrcode

def get_qrcode(
    data: str, 
    return_='file', 
    filename='qrcode.jpg',
    border_size=2, 
    fill_color="black", 
    back_color="white"
):
    """
        input: 
        - data = Text for QRCode,
        - return_ = What are you want to get? ['img', 'file'],
        - filename = name of your file (ONLY .jpg),
        - border_size  = Size of your border around qrcode,
        - fill_color = qrcode color
        - back_color = background color
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=30,
        border=border_size,
    )
    qr.add_data(data=data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    if return_ == 'img':
        return img
    elif return_ == 'file':
        img.save(filename) if filename.endswith('.jpg') else img.save(filename + '.jpg')
        return True

if __name__ == "__main__":
    get_qrcode('Data Here')
    