playlist = [{
    "name": "turn it off",
    "artist": "culture",
    "album": "Peach",
    "duration": "3:37"
}, {
    "name": "turn it off",
    "artist": "culture",
    "album": "Peach",
    "duration": "3:37"
}, {
    "name": "turn it off",
    "artist": "culture",
    "album": "Peach",
    "duration": "3:37"
}, {
    "name": "turn it off",
    "artist": "culture",
    "album": "Peach",
    "duration": "3:37"}
]
print(playlist[0])
print(playlist[0]["name"])
print(playlist[0]["duration"])

# But the problem with above approach is that we can't store the name of the playlist
# the date it was created the owner of the playlist so we will have to use a Dictionary for playlist
# the better approach below

playlist1 = {
    "name": "BEST PLAYLIST EVER",
    "creator": "tempatron",
    "Date": "31-08-1998",
    "songs": [{
        "name": "turn it off 1",
        "artist": "culture1",
        "album": "Peach1",
        "duration": 3.37
    }, {
        "name": "turn it off2",
        "artist": "culture2",
        "album": "Peach2",
        "duration": 3.37
    }, {
        "name": "turn it off3",
        "artist": "culture3",
        "album": "Peach3",
        "duration": 3.37
    }, {
        "name": "turn it off4",
        "artist": "culture4",
        "album": "Peach4",
        "duration": 3.37
        }
    ]
}
t = 0

for length in playlist1['songs']:
    t += length['duration']

print(f'Total duration = {t}')

print(playlist1["songs"][3]["name"])

