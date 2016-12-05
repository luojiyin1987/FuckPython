from flask import send_file

@app.route('/file-downloads/')
def file_downloads():
    try:
        return reader_template('downloads.html')
    except Exception as e :
        return str(e)

@app.route('/return-files/')
def return_files_tut():
    try:
        rerurn send_file('/var/www/PythonProgramming/PythonProgramming/static/images/python.jpg', attachment_filename='python.jpg')
    except Exception as e:
        return str(e)
