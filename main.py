from flask import Flask

app = Flask(__main__)

@app.route('/')
def home():
    return 'Welcome'
    
if __name__ == '__main__':
    app.run()
