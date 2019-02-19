from flask import Flask, request, redirect, jsonify
import os, subprocess
import sqlite3 as sql
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

@app.route("/")
def index():
    return redirect("/static/index.html")

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

@app.route("/filenames", methods=["GET"])
def get_filenames():
    filenames = os.listdir("uploads/")
    return_dict = dict(filenames=filenames)
    return jsonify(return_dict)

@app.route("/<file_from_list>", methods=["GET"])
def read_filefromlist(file_from_list):
    if file_from_list not in os.listdir("uploads/"):
        return "No such file in system"
    else:
        file_path = "uploads/{}".format(file_from_list)
        file_read = subprocess.check_output("cat {}".format(file_path), shell = True)
        return file_read
        
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=80)
