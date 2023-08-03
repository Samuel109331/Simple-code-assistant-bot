import requests
from flask import *
import github as gt
from flask_restful import Api,Resource

class GenerateCode(Resource):
    def get(self,question):
        response = gt.getCodes(question)
        return {"codes" : response}

app = Flask(__name__)
api = Api(app)

api.add_resource(GenerateCode,'/api/generate/<string:question>')

@app.route("/")
def homePage():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)