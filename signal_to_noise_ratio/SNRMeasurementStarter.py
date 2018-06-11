import sys
sys.path.append(sys.path[0] + '/../utils/')
print sys.path
from BaseMeasurement import BaseMeasurement
from top_block import top_block

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