from BinaryReader import BinaryReader
from CSVWriter import CSVWriter
import collections
import sys
import os.path

MeasurementContext = collections.namedtuple('MeasurementContext', ['reader', 'index', 'freq', 'inputloc', 'outputloc'])

def startMeasurement(measurement):
    if len(sys.argv) != 3:
        print 'location and measuring time not specified'

    location = sys.argv[1]
    measuringTime = int(sys.argv[2])
    titles = ['Index', 'Frequency', 'sample count', 'Min', 'Max', 'Mean', 'Std']

    binaryReader = BinaryReader()
    sources = measurement.getSources()
    inLoc = measurement.getOutputLocation()
    outLoc = location
    writers = _getWriters(outLoc, sources)
    _writeHeader(writers, titles)
    for i in xrange(0,measurement.getSize()-1):
        measurement.startMeasurement(i,measuringTime)
        freq = measurement.getFrequency(i)
        context = MeasurementContext(binaryReader, i, freq, inLoc, outLoc)
        _writeDataSet(context, sources, writers)
    _closeWriters(writers)

def _getWriters(outputLocation, sources):
   writers = []
   for source in sources:
       writer = CSVWriter()
       writer.open(outputLocation + source + '.csv')
       writers.append(writer)
   return writers

def _writeHeader(writers, titles):
    for writer in writers:
        _writeRow(writer, titles)

def _writeDataSet(context, sources, writers):
    for i, writer in enumerate(writers):
        location = context.inputloc
        source = sources[i]
        filePath = location + source + '_' + str(index) + '.bin'
        if os.path.isfile(fname):
            data = _prepareData(context, filePath)
            _writeRow(writer, data)

def _writeRow(writer, data):
    writer.writeRow(data)

def _prepareData(context, filePath, firstAndLast = 20):
    reader = context.reader
    index = context.index
    frequency = context.freq
    reader.readToFloat(filePath)
    data = [index, frequency, reader.getSize(), reader.getMin(), reader.getMax(), reader.getMean(), reader.getStd()]
    for number in reader.getData()[:firstAndLast]:
        data.append(number)
    for number in reader.getData()[-firstAndLast:]:
        data.append(number)
    return data

def _closeWriters(writers):
    for writer in writers:
	    writer.close()
