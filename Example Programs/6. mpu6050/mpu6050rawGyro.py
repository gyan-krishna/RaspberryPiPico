from machine import I2C
from machine import Pin

gyro = I2C(1, scl=Pin(27), sda=Pin(26), freq=100000)
addr = gyro.scan()[0]

#resetting gyro by writing 0x00 in reg 0x6B
gyro.writeto(addr, 0x6B) #reg
gyro.writeto(addr, 0x00) #data

#writing to GYRO_CONFIG register
gyro.writeto(addr, 0x1B)
gyro.writeto(addr, 0x10) #1000dps full scale

#configuring accleration with ACCEL_CONFIG reg
gyro.writeto(addr, 0x1C)
gyro.writeto(addr, 0x10) # 8g full scale range

gyro.writeto(addr, 0x3B)
print(gyro.readfrom(addr, 6))
print("end")