import time
import random
from eventos import EventManager

class RealTimeDataManager:
    def __init__(self):
        self.event_manager = EventManager()
        self.temperatura = 0.0
        self.humedad = 0.0

    def update_data(self):
        # Simulación de actualización periódica de datos
        while True:
            # Lógica para actualizar la temperatura y la humedad con números aleatorios
            self.temperatura = round(random.uniform(20.0, 30.0), 2)
            self.humedad = round(random.uniform(50.0, 70.0), 2)

            # Notificar a los suscriptores que los datos han cambiado
            data = {'temperatura': self.temperatura, 'humedad': self.humedad}
            self.event_manager.notify(data)

            time.sleep(1)  # Simular un intervalo de actualización

if __name__ == "__main__":
    def callback(data):
        print(f'Datos en tiempo real actualizados: {data}')

    data_manager = RealTimeDataManager()
    data_manager.event_manager.subscribe(callback)

    # Iniciar la actualización periódica
    data_manager.update_data()
