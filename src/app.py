from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessário para usar sessões

@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializa o número aleatório se não estiver na sessão
    if 'secret_number' not in session:
        session['secret_number'] = random.randint(1, 10)
    
    result = None
    
    if request.method == 'POST':
        try:
            guess = int(request.form.get('guess'))
            secret_number = session['secret_number']
            
            if guess == secret_number:
                result = 'Você acertou!'
                session.pop('secret_number', None)  # Remove o número após acertar
            elif guess < secret_number:
                result = 'Tente um número maior.'
            else:
                result = 'Tente um número menor.'
        except ValueError:
            result = 'Por favor, insira um número válido.'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

