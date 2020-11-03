import sys
import os

import pafy

print(
    'Хотите скачать видео или аудио с YouTube? Просто введите ссылку ниже...')
url = input('Введите URL: ')
print('Чтобы скачать видео введите: 1 | Чтобы скачать аудио введите: 2 ')
choice = int(input('Введите цифру: '))


def download(choice, url):
    try:
        v = pafy.new(url)
        if choice == 1:
            streams = v.streams
        elif choice == 2:
            streams = v.audiostreams
        else:
            sys.exit()
        if choice == 1:
            print(
                'Выберите желаемое качество видео, передав цифру. Пример: 1 ')
        else:
            print(
                'Выберите желаемое качество аудио, передав цифру. Пример: 2 ')

        available_streams = {}
        count = 1  # для удобства пользователей начинаем отсчет с единицы
        for stream in streams:
            available_streams[count] = stream
            print(f'{count}: {stream}')
            count += 1

        stream_count = int(input('Введите число: '))
        d = streams[stream_count - 1].download()

        if choice == 2:
            audio_extension = str(available_streams[stream_count])
            audio_extension = audio_extension.split('@')[0].split(':')[1]

            file_name = v.title
            audio_file = f'{file_name}.{audio_extension}'
            base = os.path.splitext(audio_file)[0]
            # TODO: на винде не работает конвертация таким образом.
            os.rename(audio_file, base + '.mp3')

        return d

    except:
        print('Упс, кажется, что ссылка неправильная...попробуйте снова')


if __name__ == '__main__':
    download(choice, url)
