# podcast-save
Small Python script to save podcast audio files from a feed URL.

Uses episode Date (YYYY-MM-DD) and Title as the file name - with (Windows) illegal characters removed - and updates the file creation/modification time to be the episode date.

Assumes `.mp3` type/extension.

Example usage:
```shell
python ~/src/podcast-save/get-episode-files.py 'https://heritagepark.org/podcast/1e3ea995-6640-464a-96d8-7e70eecdb18a.xml'
```
