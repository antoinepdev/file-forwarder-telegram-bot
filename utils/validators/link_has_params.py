def link_has_params(url_string):
    url_splited = url_string.split(" ")
    if len(url_splited) == 1:
        return False
    return True
