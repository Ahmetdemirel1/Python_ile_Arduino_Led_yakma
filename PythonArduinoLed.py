import serial
import time


arduino = serial.Serial('COM3', 9600)

def on_off_fun():
	option = input('Ledi yakmak icin on kapatmak icin Off seceneklerini kullan')

	if option == 'on':
		print ("Led Suan yaniyor...")
		time.sleep(1)
		arduino.write('1'.encode('utf-8'))
		on_off_fun()

	if option == 'off':
		print('Led Suan yanmiyor...')
		time.sleep(1)
		arduino.write('0'.encode('ascii'))

		on_off_fun()


	else:
		print('On yada Off secmeliydiniz!')
		on_off_fun()


time.sleep(2)
on_off_fun()