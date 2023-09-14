from flask import Flask, request, render_template
from googlesearch import search

app = Flask(__name__)


def search_pdfs(query, num_results=5):
    search_results = []
    try:
        for j in search(query + " filetype:pdf", num_results=num_results):
            search_results.append(j)
        return search_results
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

@app.route("/", methods=["GET", "POST"])
def index():
    search_results = []
    if request.method == "POST":
        search_query = request.form.get("query")
        search_results = search_pdfs(search_query, num_results=5)
    return render_template("index.html", search_results=search_results)

if __name__ == "__main__":
    app.run(debug=True)

