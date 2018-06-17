import numpy

class MeasurementStatistics():

    @staticmethod
    def getSize(data):
        return len(data)

    @staticmethod
    def getFirstAndLast(data, count):
        d = []
        for number in data[:count]:
            d.append(number)
        for number in data[-count:]:
            d.append(number)
        return d

    @staticmethod
    def getMin(data):
        return numpy.min(data)

    @staticmethod
    def getMax(data):
        return numpy.max(data)

    @staticmethod
    def getMean(data):
        return numpy.mean(data)

    @staticmethod
    def getStd(data):
        return numpy.std(data)