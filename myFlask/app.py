from flask import Flask, render_template, request
import queryingFinal

app = Flask(__name__)

@app.route('/')
def welcomePage():
    title = 'Recipe Recommendation System!'
    return render_template('index.html', title = title)

@app.route('/queryInputForm')
def queryInputForm():
    title = 'Please Enter In Ingredients!'
    return render_template('queryInputs.html', title = title)

@app.route('/displayResults', methods = ['POST', 'GET'])
def displayResults():
    ING1 = request.form.get('ingredient1')
    ING2 = request.form.get('ingredient2')
    ING3 = request.form.get('ingredient3')
    rawQuery = [ING1, ING2, ING3]
    query = [ingredient for ingredient in rawQuery if ingredient != '']
    if (request.form.get('rankedDisplaySelection') == "true"):
        title = "You'r ranked recipe results!"
        recoR3T = queryingFinal.Search_Recipes(query, True, (0,3))
        return render_template('displayResult.html', my_dict = recoR3T, title = title)
    else:
        title = "You'r recipe results!"
        recoR3F = queryingFinal.Search_Recipes(query, False, (0,3))
        return render_template('displayResult.html', my_dict = recoR3F, title = title)
    
if __name__ == "__main__":
    app.run()
