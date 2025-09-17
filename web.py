from flask import Flask, render_template, request
from functions import search as searchContaining, definition as definitionContaining
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/kanji/<level>")
def kanji(level='n3'):
    return render_template('kanji.html', content=f"data/{level}_all.html", level=level)

@app.route('/search')
def searchPage():
    return render_template('search.html', result=None, totalWord=None, search=None)
@app.route("/search/<value>/page=<page>")
def search(value=None,page=1):
    res = searchContaining(value,page)

    soup = BeautifulSoup(str(res), 'html.parser')
    nextPage = soup.find('a', {'class':'more'})
    totalWord = soup.find('h4').text
    if(nextPage):
        strNextPage = nextPage['href'].split("?")[1]

        elHref = "/search/" + str(value) + "/" + strNextPage

        elA = soup.new_tag("a", href=elHref, style="padding: 8px; border: 1px solid white; border-radius: 5px;text-align: center")
        elA.string = "NEXT PAGE"

        nextPage.replace_with(elA)

    return render_template('search.html', result=str(soup), totalWord=totalWord, search=value)

@app.route("/definition")
def definition(result=None, search=None):
    if not request.args.get('query'):
        return render_template('definition.html', result='', search=search)
    query,searchType,x,y = request.args.values()
    res = definitionContaining(query,searchType,x,y)
    return render_template('definition.html', result=res, search=query)

@app.errorhandler(500)
def page_not_found(error):
    return "<p>Back To Home :)</p>" 