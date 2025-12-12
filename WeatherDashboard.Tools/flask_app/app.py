from flask import Flask,jsonify
app=Flask(__name__)
@app.get('/cities')
def cities():
    return jsonify([])
if __name__=='__main__':
    app.run()
