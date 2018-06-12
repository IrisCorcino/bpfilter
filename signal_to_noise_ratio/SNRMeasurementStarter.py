import sys
sys.path.append(sys.path[0] + '/../utils/')
from BaseMeasurement import BaseMeasurement
import MeasurementStarter
from top_block import top_block

class SNRMeasurement(BaseMeasurement):

    def __init__(self):
        BaseMeasurement.__init__(self)

    def getSources(self):
        sources = []
        sources.append(self.getPattern(self.tb.get_FileNameSND()))
        return sources

def main():
    measurement = SNRMeasurement()
    measurement.setTopBlock(top_block())
    MeasurementStarter.startMeasurement(measurement)

if __name__ == '__main__':
    main()
