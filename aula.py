from flask import Flask

app = flask('Hello')

@app.route('/home')
    def home():
        return "Hello from Flask"    
