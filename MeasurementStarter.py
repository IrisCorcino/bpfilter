import Measurement

def main():
    measurement = Measurement.Measurement()
    for i in xrange(0,measurement.getSize()-1):
        measurement.startMeasurement(i,2)
    #measurement.quit()
    
if __name__ == '__main__':
	main()
