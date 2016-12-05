from flask import Flask, make_response, request

app = Flask(__name__)

def transform(text_file_contents):
    return text_file_contents.replace("=",",")

@app.route('/')
def form():
    return """
        <html>
            <body>
                <h1> Transform a flle demo</h1>
                <form action="/transform" method="post"  enctype="multipart/form-data">
                    <input type="file" name="data_file">
                    <input type="submit">
                </form>
            </body>
        </html>
        """

@app.route('/transform', methods=["POST"])
def transform_view():
    file = request.files['data_files']
    if not file:
        return "No file"

    file_contents = file.stream.read().decode("utf-8")
    result = transform(file_contents)
    
    response = make_response(result)
    response.headers["Content-Disposition"] = "attachment; filename=result.csv"
    return reponse

if  __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True)
