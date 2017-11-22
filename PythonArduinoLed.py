import serial
import time


arduino = serial.Serial('COM4', 9600)

def on_off_fun():
	option = input('Ledi yakmak icin On kapatmak icin Off seceneklerini kullan')

	if option == 'On':
		print ("Led Suan yaniyor...")
		time.sleep(1)
		arduino.write('LedOn')
		on_off_fun()

	elif option == ' Off':
		print('Led Suan yanmiyor...')
		arduino.write('LedOff')
		on_off_fun()

	else:
		print('On yada Off secmeliydiniz!')
		on_off_fun()


time.sleep(2)
on_off_fun()