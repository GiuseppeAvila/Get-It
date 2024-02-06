def extract_route(request):
    return request.split(' ')[1][1:]

read_file = lambda filepath: open(filepath, 'rb').read()