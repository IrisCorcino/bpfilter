import sys
sys.path.append('../utils/')
from BaseMeasurement import BaseMeasurement

class PSMeasurement(BaseMeasurement):

    def getFilters(self):
        filters = []
        filters.append(self.getPattern(self.tb.get_FileNameCAS()))
        filters.append(self.getPattern(self.tb.get_FileNameCP()))
        return filters
