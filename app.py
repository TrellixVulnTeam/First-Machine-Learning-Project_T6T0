from flask import Flask, request
from housing.logger import logging
from housing.exception import HousingException
import sys





app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        housing= HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logging module")

    logging.info("we are testing logging module")
    return "Starting Machine Learning Project"
    
   
    


if __name__=="__main__":
    app.run(debug=True)




