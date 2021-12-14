import pickle
def input_one_song():
    song = {}
    song['group'] = input('Group: ')
    song['singers'] = input('Singers: ').split(' ')
    song['disk'] = input('Disk: ')
    song['song'] = input('Song: ')
    with open('baza_songs.txt','wb') as file:
        pickle.dump(song,file)
    return song


def input_songs():
    n = int(input('Кількість пісень: '))
    return [input_one_song() for i in range(n)]



def search_song(songs_list, song_title):
    return list(filter(lambda song: song['song'] == song_title, songs_list))


# -----------------

songs_list = input_songs()

while True:
    ans = input('Do you want to search {y/n}?')
    if ans == 'n':
        break
    song_title = input('Song for search: ')
    songs_res = search_song(songs_list, song_title)
    if len(songs_res) > 0:
        print(songs_res)
    else:
        print('No song')

