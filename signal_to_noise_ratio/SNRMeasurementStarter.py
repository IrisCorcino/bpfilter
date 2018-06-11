import sys
sys.path.append(sys.path[0] + '/../utils/')
from BaseMeasurement import BaseMeasurement
import BaseMeasurementStarter
from top_block import top_block

class SNRMeasurement(BaseMeasurement):

    def __init__(self):
        BaseMeasurement.__init__(self)

    def getFilters(self):
        filters = []
        filters.append(self.getPattern(self.tb.get_FileNameSND()))
        return filters

def main():
    measurement = SNRMeasurement()
    measurement.setTopBlock(top_block())
    BaseMeasurementStarter.startMeasurement(measurement)

if __name__ == '__main__':
    main()
