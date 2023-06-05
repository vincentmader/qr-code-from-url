from pathlib import Path
import sys

import qrcode
import qrcode.image.svg


def get_url_from_cli_args():
    cli_args = sys.argv
    try:
        url = cli_args[1]
        return url
    except IndexError:
        raise Exception("You have to specify a url!")


def main():
    # Get URL from command line arguments.
    url = get_url_from_cli_args()
    # Generate QR code image.
    img = qrcode.make(url)
    # Define path to QR code image file. 
    filename = url.replace('/', '_')
    filename = f"{filename}.png"
    path_to_file = Path("..", "out", filename)
    # Save QR code image to disk.
    with open(path_to_file, "wb") as qr:
        img.save(qr)


if __name__ == "__main__":
    main()
