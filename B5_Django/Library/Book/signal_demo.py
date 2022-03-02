from django.dispatch import Signal, receiver

# Create a custom signal
ping_signal = Signal(providing_args=["context"])
# print(ping_signal)
class SignalDemo:
    # function to send the signal
    def ping(self):
        print('PING')
        ping_signal.send(sender=self.__class__, PING=True, val=25)


# Function to receive the signal
@receiver(ping_signal)
def pong(**kwargs):
    # print(kwargs)  # dict
    if kwargs.get('PING'):
        print('PONG')

# demo = SignalDemo()
# demo.ping()