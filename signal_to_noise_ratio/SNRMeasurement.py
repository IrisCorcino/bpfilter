import sys
sys.path.append('../utils/')
print sys.path
from BaseMeasurement import BaseMeasurement

class SNRMeasurement(BaseMeasurement):

    def getFilters(self):
        filters = []
        filters.append(self.getPattern(self.tb.get_FileNameSND()))
        return filters