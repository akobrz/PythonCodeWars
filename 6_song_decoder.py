def song_decoder(song):
    return ' '.join([x for x in song.split("WUB") if x])

print(song_decoder("AWUBBWUBC"), "A B C","WUB should be replaced by 1 space")
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"), "A B C","multiples WUB should be replaced by only 1 space")
print(song_decoder("WUBAWUBBWUBCWUB"), "A B C","heading or trailing spaces should be removed")