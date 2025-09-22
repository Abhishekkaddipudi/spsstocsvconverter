import os
from flask import Flask, request, render_template, send_file, redirect, url_for, flash
import pyreadstat

app = Flask(__name__)
app.secret_key = "secret123"  # for flash messages

# create folders if not exist
os.makedirs("uploads", exist_ok=True)
os.makedirs("converted", exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            flash("No file selected")
            return redirect(request.url)

        if file and file.filename.endswith(".sav"):
            # save uploaded file
            filepath = os.path.join("uploads", file.filename)
            file.save(filepath)

            # convert to CSV
            df, meta = pyreadstat.read_sav(filepath)
            csv_filename = file.filename.rsplit(".", 1)[0] + ".csv"
            csv_path = os.path.join("converted", csv_filename)
            df.to_csv(csv_path, index=False)

            flash("File successfully converted!")
            return redirect(url_for("download_file", filename=csv_filename))
        else:
            flash("Please upload a .sav file")
            return redirect(request.url)

    return render_template("index.html")


@app.route("/download/<filename>")
def download_file(filename):
    path = os.path.join("converted", filename)
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
