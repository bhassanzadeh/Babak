import sys

if len(sys.argv) < 2:
    print('provide at least 1 file as argument')
    sys.exit()

song_files = sys.argv[1:]

result = {}
for song in song_files:
    # open the file
    with open(song, 'rw') as file:
        all_lines = file.read()

    song_title = all_lines.split('\n')[0] #first line
    lyrics_lines = all_lines.split('\n')[1:] # second line and more

    for line in lyrics_lines:
        for word in line.split(' '): # separate words by space
            if len(word) < 1: continue
            word = word.lower() # convert to lowercase
            if word not in result.keys():
                result[word] = {}
                result[word]['count'] = 1
                result[word]['songs'] = [song_title]
            else:
                result[word]['count'] = result[word]['count'] + 1
                # if the song title is not already in the list of songs, add it
                if song_title not in result[word]['songs']:
                    result[word]['songs'].append(song_title)
