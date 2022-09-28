def read_log():

    with open('log.txt', 'r') as f:
        while True:
            data = f.read()
            return data


if __name__ == '__main__':
    print(read_log())
