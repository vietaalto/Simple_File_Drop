from flask import Flask, request, redirect, jsonify
import os, subprocess
import sqlite3 as sql
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

@app.route("/")
def index():
    return redirect("/static/index.html")

# With POST / a file is stored in the filesystem and the file's metadata (name, size etc) is stored in a DB.
@app.route("/sendfile", methods=["POST"])
def send_file():
    upfile = request.files["uploadedfile"]
    filename = secure_filename(upfile.filename)
    file_path = "{}/{}".format(app.config["UPLOAD_FOLDER"], filename)
    upfile.save(file_path)
    filesize = os.stat(file_path).st_size
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO filemetas (fname,fsize) VALUES (?,?)",(filename,filesize))
        con.commit()
    return "successful_upload"

# With GET / the list of uploaded files is retrieved from the database.
@app.route("/filenames", methods=["GET"])
def get_filenames():
    filenames = os.listdir("uploads/")
    return_dict = dict(filenames=filenames)
    return jsonify(return_dict)

# With GET /a_file_from_the_list the file's contents are read using 'cat' command line utility and then sent as a response to the client.
@app.route("/<file_from_list>", methods=["GET"])
def read_filefromlist(file_from_list):
    if file_from_list not in os.listdir("uploads/"):
        return "No such file in system"
    else:
        file_path = "uploads/{}".format(file_from_list)
        file_read = subprocess.check_output("cat {}".format(file_path), shell = True) # --> CAT command
        return file_read
        
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=80)
