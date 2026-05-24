def analyze_exif(image):
    try:
        exif = image._getexif()
        if exif:
            return "EXIF data present"
        return "No EXIF data (suspicious)"
    except:
        return "EXIF not accessible"

