def lou_bega(lyrics_list: list):

    for prefix in range(len(lyrics_list)):
        lyrics_list[prefix] = "A little bit of " + lyrics_list[prefix]
    return lyrics_list

lyrics_list = [
    "Monica in my life", 
    "Erica by my side", 
    "Rita's all I need"
]

print(lou_bega(lyrics_list))
