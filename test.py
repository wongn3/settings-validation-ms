import time

def send_request(volume, brush_size):
    with open('validation_request.txt', 'w') as file:
        file.write(f'volume={volume}\n')
        file.write(f'brush_size={brush_size}')


# test 1: normal params
send_request(
    volume=70,
    brush_size=3
)

time.sleep(5)

# test 2: high vol
send_request(
    volume=170,
    brush_size=3
)

time.sleep(5)

# test 3: low vol
send_request(
    volume=-70,
    brush_size=3
)

time.sleep(5)

# test 4: high brush
send_request(
    volume=70,
    brush_size=300
)

time.sleep(5)

# test 4: low brush
send_request(
    volume=70,
    brush_size=-3
)