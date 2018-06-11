import sys
print sys.path[0]
sys.path.append(sys.path[0] + '/../utils/')
print sys.path
from BaseMeasurement import BaseMeasurement
from top_block import top_block

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
