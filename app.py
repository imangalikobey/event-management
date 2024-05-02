from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


# Мероприятия для тестовых данных
events = [
    {"id": 1, "name": "Концерт", "date": "2024-05-10", "location": "Концертный зал", "tickets_available": 100},
    {"id": 2, "name": "Выставка", "date": "2024-05-15", "location": "Выставочный центр", "tickets_available": 50},
    {"id": 3, "name": "Фестиваль", "date": "2024-06-01", "location": "Парк развлечений", "tickets_available": 200}
]

users = []


@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/event/<int:event_id>')
def event_details(event_id):
    event = next((event for event in events if event['id'] == event_id), None)
    return render_template('event.html', event=event)

@app.route('/register', methods=['POST'])
def register():
    event_id = int(request.form['event_id'])
    name = request.form['name']
    email = request.form['email']
    tickets = int(request.form['tickets'])
    
    event = next((event for event in events if event['id'] == event_id), None)
    if event and event['tickets_available'] >= tickets:
        # Обновляем количество доступных билетов
        event['tickets_available'] -= tickets
        
        # Добавляем пользователя в список зарегистрированных
        users.append({"name": name, "email": email, "tickets": tickets, "event_id": event_id})
        
        return redirect(url_for('index'))
    else:
        return "Недостаточно доступных билетов"
    
if __name__ == '__main__':
    app.run(debug=True)
