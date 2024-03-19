from flask import render_template, request, redirect, url_for, Blueprint
from datetime import datetime
from services.reservation_service import ReservationService
from services.restaurant_service import RestaurantService
from util.dto import ReservationFormDto

reservation_blueprint = Blueprint('reservation', __name__)
restaurant_service = RestaurantService()
reservation_service = ReservationService()

@reservation_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        reservation_dto = ReservationFormDto(
                                        restaurant_id=int(request.form['restaurant_id']),
                                        name=request.form['name'],
                                        email=request.form['email'],
                                        phone=request.form['phone'],
                                        num_guests=int(request.form['num_guests']),
                                        date_time=datetime.strptime(request.form['date'], '%Y-%m-%d')
        )
        print(reservation_dto._date_time)
        reservation_service.add(reservation_dto)
        # 원래 쌤 코드
        # return redirect(url_for('reservation.index'))
        # 26번, 27번 줄 삽입
        reservations = reservation_service.get_all()
        return render_template('manage_reservations.html', reservations = reservations)
    restaurants = restaurant_service.get_all()
    print(restaurants)
    return render_template('index.html', restaurants = restaurants)

@reservation_blueprint.route('/cancel_reservation/<int:id>')
def deletes(id):
    reservation_service.delete(id)

    reservations = reservation_service.get_all()
    return render_template('manage_reservations.html', reservations = reservations)