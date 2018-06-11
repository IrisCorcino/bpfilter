from BinaryReader import BinaryReader
from ExcelWriter import ExcelWriter
import collections
import sys

MeasurementContext = collections.namedtuple('MeasurementContext', ['reader', 'index', 'freq', 'inputloc', 'outputloc'])

def startMeasurement(measurement):
    if len(sys.argv) != 3:
        print 'location and measuring time not specified'

    location = sys.argv[1]
    measuringTime = int(sys.argv[2])
    titles = ['Index', 'Frequency', 'Min', 'Avg', 'Max']

    binaryReader = BinaryReader()
    filters = measurement.getFilters()
    inLoc = measurement.getOutputLocation()
    outLoc = location
    writers = getWriters(outLoc, filters)
    writeHeader(writers, titles)
    for i in xrange(0,measurement.getSize()-1):
        measurement.startMeasurement(i,measuringTime)
        freq = measurement.getFrequency(i)
        context = MeasurementContext(binaryReader, i, freq, inLoc, outLoc)
        writeDataSet(context, filters, writers)
    closeWriters(writers)

def getWriters(outputLocation, filters):
   writers = []
   for filter in filters:
       writer = ExcelWriter()
       writer.open(outputLocation + filter + '.csv')
       writers.append(writer)
   return writers

def writeHeader(writers, titles):
    for writer in writers:
        writeRow(writer, titles)

def writeDataSet(context, filters, writers):
    for i, writer in enumerate(writers):
        data = prepareData(context, filters[i])
        writeRow(writer, data)

def writeRow(writer, data):
    writer.writeRow(data)

def prepareData(context, filter, firstAndLast = 20):
    reader = context.reader
    index = context.index
    frequency = context.freq
    location = context.inputloc
    reader.readToFloat(location + filter + '_' + str(index) + '.bin')
    data = [index, frequency, reader.getMin(), reader.getAvg(), reader.getMax()]
    for number in reader.getData()[:firstAndLast]:
        data.append(number)
    for number in reader.getData()[-firstAndLast:]:
        data.append(number)
    return data

def closeWriters(writers):
    for writer in writers:
	    writer.close()
