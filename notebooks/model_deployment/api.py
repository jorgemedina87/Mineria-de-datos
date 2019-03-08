#!/usr/bin/python
from flask import Flask
from flask_restplus import Api, Resource, fields
from sklearn.externals import joblib
from m09_model_deployment import predict_proba



app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Prediction Price API',
    description='Prediction Price API')

ns = api.namespace('predict', 
     description='Price')
   
parser = api.parser()

parser.add_argument(
    'Data Year',
    type=int, 
    required=True, 
    help='Year', 
    location='args')
parser.add_argument(
    'Data Mileage',
    type=int, 
    required=True, 
    help='Mileage', 
    location='args')

parser.add_argument(
    'Data State',
    type=str, 
    required=True, 
    help='State', 
    location='args')


parser.add_argument(
    'Data Make',
    type=str, 
    required=True, 
    help='Make', 
    location='args')

parser.add_argument(
    'Data Model',
    type=str, 
    required=True, 
    help='Model', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.Integer,
})


@ns.route('/')
class PriceApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": predict_price(args['Data Year'],args['Data Mileage'],args['Data State'],
                                                                             args['Data Make'],args['Data Model'])
        }, 200
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8089)
