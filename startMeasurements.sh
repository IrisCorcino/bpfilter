print_info_and_exit() {
  echo "Usage:"
  echo "$0 -m MEASUREMENT OUTPUT MEASUREMENT_IN_SEC" >&2
  echo "   MEASUREMENT" >&2
  echo "      0 - ALL" >&2
  echo "      1 - SNR" >&2
  echo "      2 - PS" >&2
  echo "or" >&2
  echo "$0 -p PLOTTER OUTPUT INPUT FILE_PATTERN" >&2
  echo "   PLOTTER" >&2
  echo "      0 - CSV" >&2
  echo "      1 - DIAGRAM" >&2
  echo "      1 - DIFF DIAGRAM" >&2
  exit 1
}

check_if_number() {
  if [[ $(($1)) != $1 ]]; then
    echo "argument is not a number" >&s
    print_info_and_exit
  fi
}

check_if_existing_directory() {
  if ! [ -d "$1" ]; then
    echo "directory does not exist" >&2
    print_info_and_exit
  fi
}

source ~/pybombs/prefix/default/setup_env.sh

case "$1" in
"-m")
  # -m MEASUREMENT OUTPUT MEASUREMENT_IN_SEC
  if [ $# != 4 ]; then
    echo "incorrect number of arguments" >&2
    print_info_and_exit
  fi
  check_if_number "$2"
  check_if_existing_directory "$3"
  check_if_number "$4"

  MEASUREMENT=$2
  OUTPUT_DIR=$3
  MEASUREMENT_IN_SEC=$4

  case "$MEASUREMENT" in
  "0")
    python2 ./signal_to_noise_ratio/SNRMeasurementStarter.py $OUTPUT_DIR $MEASUREMENT_IN_SEC 
    python2 ./potency_of_signal/PSMeasurementStarter.py $OUTPUT_DIR $MEASUREMENT_IN_SEC 
    ;;
  "1")
    python2 ./signal_to_noise_ratio/SNRMeasurementStarter.py $OUTPUT_DIR $MEASUREMENT_IN_SEC  
    ;;
  "2")
    python2 ./potency_of_signal/SNRMeasurementStarter.py $OUTPUT_DIR $MEASUREMENT_IN_SEC 
    ;;
  *)
    print_info_and_exit
    ;;
  esac
  exit 1
  ;;
"-p")
  # -p PLOTTER OUTPUT INPUT FILE_PATTERN"
  if [ $# -lt 5 ] || [ $# -gt 7 ]; then
    echo "incorrect number of arguments" >&2
    print_info_and_exit
  fi
  check_if_number "$2"
  check_if_existing_directory "$3"
  check_if_existing_directory "$4"

  PLOTTER=$2
  OUTPUT_DIR=$3
  INPUT_DIR=$4
  FILE_PATTERN1=$5
  if [ $# -eq 5 ]; then
    python2 ./utils/MeasurementPlotter.py $PLOTTER $OUTPUT_DIR $INPUT_DIR $FILE_PATTERN1
  elif [ $# -eq 5  ]; then
    FILE_PATTERN2=$6
    python2 ./utils/MeasurementPlotter.py $PLOTTER $OUTPUT_DIR $INPUT_DIR $FILE_PATTERN1 $FILE_PATTERN2
  else
    FILE_PATTERN2=$6
    FILE_PATTERN3=$7
    python2 ./utils/MeasurementPlotter.py $PLOTTER $OUTPUT_DIR $INPUT_DIR $FILE_PATTERN1 $FILE_PATTERN2 $FILE_PATTERN3
  fi
  exit 0
  ;;
 *)
  echo "incorrect option"
  print_info_and_exit
 esac