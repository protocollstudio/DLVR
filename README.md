# DLVR

## Back

1. Go to _back_ directory.
2. Activate virtual environment.
3. Rune `make` command to read available commands.

```
cd back
source ./env/bin/activate
make
```

```
Available commands: 
	make install: install requirements
	make migrations : make migrations & migrate
	make adminuser : create a superuser to access django admin
	make run : launch django on localhost:8000
```


Routes :
- api/tracks : liste les tracks
- api/track/1 : détails d'une track
- api/track/1/like : ajoute un like
- api/track/1/dislike : ajoute un dislike


## Front

Svelte
