import sys
sys.path.append(sys.path[0] + '/../utils/')
from Measurement import Measurement
import MeasurementStarter
from top_block import top_block

def main():
    starter = MeasurementStarter(Measurement(top_block))
    starter.startMeasurement()

if __name__ == '__main__':
    main()