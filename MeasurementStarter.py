import Measurement
import BinaryReader
import ExcelWriter

def main():
    titles = ['Index', 'Frequency', 'Min', 'Avg', 'Max']
    location = '/home/iris/Desktop/medidas/'
    measurement = Measurement.Measurement()
    binaryReader = BinaryReader.BinaryReader()
    filters = measurement.getFilters()
    writers = getWriters(filters)
    writeHeader(writers, titles)
    for i in xrange(0,measurement.getSize()-1):
        measurement.startMeasurement(i,2)
	freq = measurement.getFrequency(i)
        writeDataSet(binaryReader, writers, i, freq, location, filters)
    closeWriters(writers)

def getWriters(strings):
   writers = []
   for string in strings:
       writer = ExcelWriter.ExcelWriter()
       writer.open(string + '.csv')
       writers.append(writer)
   return writers

def writeHeader(writers, titles):
    for writer in writers:
        writeRow(writer, titles)

def writeDataSet(reader, writers, index, freq, location, strings, firstAndLast = 20):
    for i, writer in enumerate(writers):
        data = prepareData(reader, index, location, strings[i], freq, firstAndLast)
        writeRow(writer, data)

def writeRow(writer, data):
    writer.writeRow(data)
    
def prepareData(reader, index, location, type, frequency, firstAndLast):
    reader.readToFloat(location + type + '_' + str(index) + '.bin')
    data = [index, frequency, reader.getMin(), reader.getAvg(), reader.getMax()]
    for number in reader.getData()[:firstAndLast]:
        data.append(number)
    for number in reader.getData()[-firstAndLast:]:
        data.append(number)
    return data

def closeWriters(writers):
    for writer in writers:
	    writer.close()
 
if __name__ == '__main__':
	main()
