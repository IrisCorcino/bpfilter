import sys
sys.path.append(sys.path[0] + '/../utils/')
print sys.path
from BaseMeasurement import BaseMeasurement
import BaseMeasurementStarter
from top_block import top_block

class SNRMeasurement(BaseMeasurement):

    def __init__(self):
        super(BaseMeasurement, self).__init__()

    def getFilters(self):
        filters = []
        filters.append(self.getPattern(self.tb.get_FileNameSND()))
        return filters

def main():
    measurement = SNRMeasurement()
    tb = top_block()
    measurement.setTopBlock(top_block)
    BaseMeasurementStarter.startMeasurement(measurement)

if __name__ == '__main__':
    main()