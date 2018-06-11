from top_block import top_block
import sys
sys.path.append('../utils/')
import BaseMeasurementStarter
from BaseMeasurement import BaseMeasurement

class PSMeasurement(BaseMeasurement):

    def getFilters(self):
        filters = []
        filters.append(self.getPattern(self.tb.get_FileNameCAS()))
        filters.append(self.getPattern(self.tb.get_FileNameCP()))
        return filters

def main():
    tb = top_block()
    BaseMeasurementStarter.startMeasurement(PSMeasurement(tb))

if __name__ == '__main__':
    main()
