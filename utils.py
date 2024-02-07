import json

def extract_route(request):
    return request.split(' ')[1][1:]

read_file = lambda filepath: open(filepath, 'rb').read()

load_data = lambda filename: json.load(open('data/' + filename))

load_template = lambda filename: open('templates/' + filename).read()