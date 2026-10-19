from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='src/templates')

#Proveedores Externos
clients_db = [
    {
        "name": "Servitécnica de Refrigeración S.A.S.",
        "idType": "NIT",
        "idNumber": "900123456-1",
        "address": "Zona Industrial, Cúcuta",
        "email": "contacto@servitecnica.com.co"
    },
    {
        "name": "Mantenimiento Térmico del Norte",
        "idType": "NIT",
        "idNumber": "890500123-4",
        "address": "Av. Sevilla # 8-15, Cúcuta",
        "email": "servicios@mantenimientotermico.com"
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form_clients', methods=['GET', 'POST'])
def form_clients():
    if request.method == 'POST':
        new_client = {
            "name": request.form.get('name'),
            "idType": request.form.get('idType'),
            "idNumber": request.form.get('idNumber'),
            "address": request.form.get('address'),
            "email": request.form.get('email')
        }
        clients_db.append(new_client)
        return redirect(url_for('list_clients'))
    return render_template('form_clients.html')

@app.route('/list_clients')
def list_clients():
    return render_template('list_clients.html', clients=clients_db)

if __name__ == '__main__':
    app.run(debug=True)
