from flask import Flask, request, jsonify, render_template_string
from config import conectar

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

# pagina do formulário de cadastro
@app.route('/')
def index():
    return render_template_string(open('index.html').read())


#  Rota para cadastrar aluno (POST)
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():
    nome = request.form.get('nome')
    email = request.form.get('email')
    matricula = request.form.get('matricula')
    senha = request.form.get('senha')

    # Aqui fazemos o hash da senha
    senha_hash = generate_password_hash(senha)
    
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO aluno (nome, email, matricula, senha) VALUES (%s, %s, %s, %s)"
        valores = (nome, email, matricula, senha_hash)
        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        return jsonify({'mensagem': 'Aluno cadastrado com sucesso!'}), 201

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

#  Rota para listar alunos (GET)
@app.route('/alunos', methods=['GET'])
def listar_alunos():
  lista = []
  try:
      conexao = conectar()
      cursor = conexao.cursor()
      cursor.execute("SELECT * FROM aluno")
      alunos = cursor.fetchall()
    

      for aluno in alunos:
        lista.append({
            'id': aluno[0],
            'nome': aluno[1],
            'email': aluno[2],
            'matricula': aluno[3],
            'senha': aluno[4]
        })
      cursor.close()
      conexao.close()  

      return jsonify(lista), 200
  except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
