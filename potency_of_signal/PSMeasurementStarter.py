import sys
sys.path.append(sys.path[0] + '/../utils/')
print sys.path
from BaseMeasurement import BaseMeasurement
from top_block import top_block

class PSMeasurement(BaseMeasurement):

    def __init__(self, top_block):
        self(BaseMeasurement, self).__init__(top_block)

    def getFilters(self):
        filters = []
        filters.append(self.getPattern(self.tb.get_FileNameCAS()))
        filters.append(self.getPattern(self.tb.get_FileNameCP()))
        return filters

def main():
    tb = top_block
    BaseMeasurementStarter.startMeasurement(PSMeasurement(tb))

if __name__ == '__main__':
    main()
