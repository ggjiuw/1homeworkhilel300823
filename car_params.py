
def car_info(weight, time, speed: int | float) -> str:
    if speed <= 0 or time <= 0 or weight <= 0:
        raise ValueError('The entered auto parameters are incorrect, they cannot be equal to or less than zero')
        exit()
    result = f'Транспортний засіб вагою {weight} кг рухався {time} секунд зі швидкістю {speed}м/сек, і подолав відстань {time * speed} метрів'
    return result
