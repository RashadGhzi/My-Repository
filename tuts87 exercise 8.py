import os


def soldier_file(path, text_type, format):
    os.chdir(path)
    list_dir = os.listdir(os.getcwd())
    print(list_dir)

    i = 10
    for item in list_dir:
        if os.path.splitext(item)[1] == text_type:
            os.rename(item, f"{item.split('.')[0].capitalize()}{text_type}")
            file = open(item, 'r')
            text = file.read().split('\n')
            for text_capit in text:
                print(text_capit.capitalize())
            print('\n')

        if os.path.splitext(item)[1] == format:
            os.rename(item, f'{i}{format}')
            i += 1


soldier_file(r'C:\Users\user\PycharmProjects\New folder', '.txt', '.jpg')
