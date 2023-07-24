import anitopy

title = "[Moozzi2] Watashi ni Tenshi ga Maiorita! Precious Friends [ x265-10Bit Ver. ] - Movie + SP"
aniparse_options = {'allowed_delimiters': ' .-+[]'}
lol = anitopy.parse(title, options=aniparse_options)
lll = lol["anime_title"]
print(lol)
print(lll)