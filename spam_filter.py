def spam_filter(file_name='input_file.txt'):

    with open(file_name, mode='r') as f:

        message = f.readline()

        while message:
            spam = False

            for word in message.split():
                if not word.isnumeric():  # если слово полностью состоит из цифр -> pass
                    # если в оставшихся словах есть хотя бы одна буква, то это спам
                    if any(ch.isnumeric() for ch in word):
                        spam = True
                        break

            if not spam:
                output_file.write(message)

            message = f.readline()

if __name__ == '__main__':
    output_file = open('output_file.txt', 'a')
    spam_filter()
    output_file.close()
