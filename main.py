from os import path, listdir, makedirs, remove

bad_words = ['Free', 'Deezer Free', 'Gratuit']

if not path.exists("Removed"):
        makedirs("Removed")
with open('hits.txt') as oldfile, open('Removed/Napster.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
print(f"""
______                                  _   _ 
| ___ \                                | | | |
| |_/ /___ _ __ ___   _____   _____  __| | | |
|    // _ \ '_ ` _ \ / _ \ \ / / _ \/ _` | | |
| |\ \  __/ | | | | | (_) \ V /  __/ (_| | |_|
\_| \_\___|_| |_| |_|\___/ \_/ \___|\__,_| (_)
                                              
                                         
              by Celwo
             flip-gen.fr  
""")
