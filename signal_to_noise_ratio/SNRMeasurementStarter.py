import sys
sys.path.append(sys.path[0] + '/../src/')
from Measurement import Measurement
from MeasurementStarter import MeasurementStarter
from top_block import top_block

def main():
    starter = MeasurementStarter(Measurement(top_block))
    starter.start()

if __name__ == '__main__':
    main()