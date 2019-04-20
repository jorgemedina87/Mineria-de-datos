#!/usr/bin/python
from flask import Flask
from flask_restplus import Api, Resource, fields
from sklearn.externals import joblib
from model_deployment.m29_model_deployment import predict_movie_genre

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Prediction Movie Genre',
    description='Developed By Andres Martinez, Nicolas Gil, Ana Maria and Jorge Medina')

ns = api.namespace('predict', 
     description='Movie Genre')
   
parser = api.parser()


parser.add_argument(
    'Data Year',
    type=int, 
    required=True, 
    help='Year', 
    location='args')
parser.add_argument(
    'Data title',
    type=str, 
    required=True, 
    help='title the movie', 
    location='args')

parser.add_argument(
    'Data plot',
    type=str, 
    required=True, 
    help='Description about the movie', 
    location='args')


resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PriceApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {  
         "result": predict_movie_genre(args['Data Year'],args['Data title'],args['Data plot'])
        }, 200
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8088)
