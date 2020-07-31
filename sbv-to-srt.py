import webvtt

decision = 'y'

if decision == 'y':
    file = input('Insert path to file: ')

    webvtt = webvtt.from_sbv(file).save_as_srt()

    decision = input('Do you have another file to convert? y or n?')
