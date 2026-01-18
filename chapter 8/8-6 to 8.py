def describe_city(city='Reykjavik', country='Iceland'):
    describe = f"{city} is in {country}"
    return describe
#返回值使用
printf = describe_city()
print(printf)

def make_album(name, album_name, song_count=None):
    if song_count is None:
        album = {'name': name, 'album_name': album_name}
    else:
        album = {'name': name, 'album_name': album_name, 'song_count': song_count}
    return album
#是否返回具有歌曲数量的键值对
a_album = make_album('aaa', 'bad')
print('\n', a_album)
b_album = make_album('bbb', 'ccc', '23')
print('\n', b_album)

make_album_program = True
#标志flag
while make_album_program:
    print("please enter a new singer name:", "if u want to leave enter 'q'")
    new_name = input()
    if new_name == 'q':
        make_album_program = False
        continue
    #退出检测
    print("please enter a new album name:")
    new_album_name = input()
    new_album = make_album(new_name, new_album_name)
    print('\n', new_album)