# File drop application

## Description

The app built in Flask, which is quite popular web framework in Python

There is UI written in JS to handle Drag and Drop

## Database

All dropped files' metadata are stored in "database.db", which is already included in the project.

'database.db' was initialised in Python before building the app

```
import sqlite3
conn = sqlite3.connect('database.db')
conn.execute('CREATE TABLE filemetas (name TEXT, size TEXT)')
conn.close()
```

### Environment setup

Make sure you have Docker installed in your machine

Build the image

```
docker build -t filedrop .
```

Run the container

```
docker run -p 4000:80 filedrop
```

You should see a message that Python is serving your app at http://0.0.0.0:80

### Usage
Go to 'http://localhost:4000' in a web browser to see the app served up on a web page.

Drag and drop a file to the red square, a list of files also appears on the left blue square. The file will appear in the "uploads" folder, and file metadata (name, size) will be stored in "database.db"

'http://localhost:4000/filenames' to get a list of files

'http://localhost:4000/<a_file_from_list>' to read the file content
