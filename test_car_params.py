from car_params import car_info


def test_car_info():
    expected_result = 'Транспортний засіб вагою 2000 кг рухався 60 секунд зі швидкістю 2.5м/сек, і подолав відстань 150.0 метрів'
    weight = 2000
    time = 60
    speed = 2.5
    actual_result = car_info(weight=weight, time=time, speed=speed)
    assert expected_result == actual_result
