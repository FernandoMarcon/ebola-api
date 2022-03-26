from flask import Flask, jsonify
import pandas as pd


api = Flask(__name__)

@api.route("/")
def index():
    return "Ebola API is up!"


@api.route("/raw")
def raw():

    fname="data/raw/EBOVAC/gene_expression/geneva/Pheno_Geneva.csv"
    data=pd.read_csv(fname,delimiter=";")

    return jsonify(data.to_list())


if __name__=="__main__":
    app.run()
