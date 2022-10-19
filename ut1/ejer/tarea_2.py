#Given the following letter, obtain the same letter but replace the word "voices" with "sounds":

song = '''You look so beautiful in this light
Your silhouette over me
The way it brings out the blue in your eyes
Is the Tenerife sea
And all of the voices surrounding us here
They just fade out when you take a breath
Just say the word and I will disappear
Into the wilderness'''
keyword = 'voices'
replaced_word = 'sounds'
start_index = song.find(keyword) #Posición incial o índice de la palabra a sustituir.
end_index = start_index + len(keyword) #Posición final que ocupa la palabra a sustituir.
song_part1 = song[:start_index] #Separamos desde el principio de la canción hasta el principio de la palabra.
song_part2 = song[end_index:] #Separamos desde el final de la palabra hasta el final de la canción.
sounds_song = song_part1 + replaced_word + song_part2
print(sounds_song)