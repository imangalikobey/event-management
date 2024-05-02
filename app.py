from flask import Flask, render_template, request, redirect, url_for, flash
import qrcode 
from pathlib import Path
app = Flask(__name__)


# Мероприятия для тестовых данных
events = [
    {"id": 1, "name": "Концерт", "date": "2024-05-10", "location": "Концертный зал", "tickets_available": 100, "description":"Концерт 50 Cent в Алматы пройдет 28 ноября 2023 года в Almaty Arena и удивит зрителей незабываемой атмосферой и яркими впечатлениями. Это событие будет исключительной возможностью для казахстанских поклонников 50 Cent увидеть его вживую и стать частью невероятного концерта, который они запомнят надолго."},
    {"id": 2, "name": "Выставка", "date": "2024-05-15", "location": "Выставочный центр", "tickets_available": 50,"description":"Эта уникальная выставка предлагает посетителям возможность окунуться в мир творчества и открыть для себя удивительные произведения искусства в различных формах: живопись, скульптура, фотография, дизайн, ремесла и многое другое. От классических мастеров до современных талантов, каждый участник выставки приносит с собой свой уникальный взгляд на мир искусства."},
    {"id": 3, "name": "Фестиваль", "date": "2024-06-01", "location": "Парк развлечений", "tickets_available": 200, "description":"На протяжении нескольких дней фестиваль предлагает посетителям уникальную возможность погрузиться в мир разнообразных искусственных выражений: музыкальных выступлений, танцев, театральных представлений, визуального искусства, ремесел, кулинарных изысков и многое другое. Каждый участник фестиваля приглашен поделиться своими традициями, талантами и идеями, чтобы создать уникальное культурное и творческое пространство, в котором каждый может найти что-то особенное и вдохновляющее."}
]


@app.route('/')
def index():
    return render_template('index.html', events=events)

@app.route('/event/<int:event_id>')
def event_details(event_id):
    event = next((event for event in events if event['id'] == event_id), None)
    return render_template('event.html', event=event)

@app.route('/registration/<int:event_id>')
def registration(event_id):
    event = next((event for event in events if event['id'] == event_id), None)
    return render_template('registration.html', event=event)

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
        user_info = f"Name: {name}, Email: {email}, ID: {id}, tickets: {tickets}"
        # QR code в качестве билета
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(user_info)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        desktop_dir = Path.home() / "Desktop"
        img_path = desktop_dir/ "ticket.png"
        img.save(img_path)
        return redirect(url_for('index'))

    else:
        return "Недостаточно доступных билетов"
    
if __name__ == '__main__':
    app.run(debug=True)
