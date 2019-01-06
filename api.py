import hug

@hug.post('/scan')
def scan(data):
    print(f'Got Scan Data! {data}')
    return True
