from top_block import top_block
import sys
sys.path.append('../utils/')
import BaseMeasurementStarter
from BaseMeasurement import BaseMeasurement

class SNRMeasurement(BaseMeasurement):

    def getFilters(self):
        filters = []
        filters.append(self.getPattern(self.tb.get_FileNameSND()))
        return filters

def main():
    tb = top_block()
    BaseMeasurementStarter.startMeasurement(SNRMeasurement(tb))

if __name__ == '__main__':
    main()