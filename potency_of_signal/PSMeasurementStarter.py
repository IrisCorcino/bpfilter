import sys
sys.path.append(sys.path[0] + '/../utils/')
from BaseMeasurement import BaseMeasurement
import MeasurementStarter
from top_block import top_block

class PSMeasurement(BaseMeasurement):

    def __init__(self):
        BaseMeasurement.__init__(self)

    def getSources(self):
        sources = []
        sources.append(self.getPattern(self.tb.get_FileNameCAS()))
        sources.append(self.getPattern(self.tb.get_FileNameCP()))
        return sources

def main():
    measurement = PSMeasurement()
    measurement.setTopBlock(top_block())
    MeasurementStarter.startMeasurement(measurement)

if __name__ == '__main__':
    main()
