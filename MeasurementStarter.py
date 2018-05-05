import Measurement
import BinaryReader
import ExcelWriter

def main():
    titles = ['Index', 'Frequency', 'Min', 'Avg', 'Max']
    measurement = Measurement.Measurement()
    binaryReader = BinaryReader.BinaryReader()
    filters = measurement.getFilters()
    writers = getWriters(filters)
    writeHeader(writers, titles)
    for i in xrange(0,measurement.getSize()-1):
        measurement.startMeasurement(i,2)
        writeDataSet(binaryReader, writers, i, filters)
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

def writeDataSet(reader, writers, index, strings, firstAndLast = 20):
    for i, writer in enumerate(writers):
        data = prepareData(reader, index, strings[i], 0, firstAndLast)
        writeRow(writer, data)

def writeRow(writer, data):
    writer.writeRow(data)
    
def prepareData(reader, index, type, frequency, firstAndLast):
    reader.readToFloat(type + '_' + str(index) + '.bin')
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
