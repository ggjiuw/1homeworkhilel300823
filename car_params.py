
def car_info(weight, time, speed: int | float) -> str:
    default_result = 'ValueError'
    if speed <= 0 or time <= 0 or weight <= 0:
        return default_result
        exit()
    result = f'Транспортний засіб вагою {weight} кг рухався {time} секунд зі швидкістю {speed}м/сек, і подолав відстань {time * speed} метрів'
    return result
