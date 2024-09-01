from flask import Flask
import random 
random_number=random.randint(0,9)
app=Flask(__name__)
@app.route("/")
def write_guess_a_number():
    return f'<h1>Guess a number between 0 and 9:</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.g" width=300>'
@app.route("/<int:number>")
def guess_a_number(number):
    if number>random_number:
        return f'<h1 style="color:purple">Too high, try again!</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.g" width=300>'
    elif number<random_number:
        return f'<h1 style="color:red">Too low, try again!</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=300>'
    else:
        return f'<h1 style="color:green">You found me!</h1>' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=300>'
    
    
if __name__=="__main__":
    app.run(debug=True)