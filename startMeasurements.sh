print_info_and_exit() {
  echo "Usage:"
  echo "$0 -m MEASUREMENT OUTPUT MEASUREMENT_IN_SEC (CHANNEL | CHANNEL_FROM CHALLEN_TO)" >&2
  echo "   MEASUREMENT" >&2
  echo "      0 - ALL" >&2
  echo "      1 - SNR" >&2
  echo "      2 - PS" >&2
  echo "or" >&2
  echo "$0 -p PLOTTER OUTPUT INPUT FILE_PATTERN (FILE_PATTERN | FILE_PATTERN FILE_PATTERN)" >&2
  echo "   PLOTTER" >&2
  echo "      0 - CSV" >&2
  echo "      1 - DIAGRAM" >&2
  echo "      2 - DIFF DIAGRAM" >&2
  echo "      3 - DIFF_SAMPLE" >&2
  echo "   FILE_PATTERN" >&2
  echo "      for <name>_<id>_<freq>.bin the FILE_PATTERN is <name>" >&2
  exit 1
}

check_if_number() {
  if [[ $(($1)) != $1 ]]; then
    echo "argument is not a number" >&2
    print_info_and_exit
  fi
}

check_if_existing_directory() {
  if ! [ -d "$1" ]; then
    echo "directory does not exist" >&2
    print_info_and_exit
  fi
}

SETUP_DIR1=~/pybombs/prefix/default/setup_env.sh
SETUP_DIR2=~/pybombs/prefix/setup_env.sh
if [ -f $SETUP_DIR1 ]; then
		source $SETUP_DIR1
else
		source $SETUP_DIR2
fi

case "$1" in
"-m")
  # -m MEASUREMENT OUTPUT MEASUREMENT_IN_SEC (CHANNEL | CHANNEL_FROM CHANNEL_TO)
  if [ $# -lt 4 ] || [ $# -gt 6 ]; then
    echo "incorrect number of arguments" >&2
    print_info_and_exit
  fi
  check_if_number "$2"
  check_if_existing_directory "$3"
  check_if_number "$4"

	if [ $# -eq 5 ]; then
		check_if_number "$5"
	fi

  if [ $# -eq 6 ]; then
		check_if_number "$6"
	fi

  MEASUREMENT=$2
  OUTPUT_DIR=$3
  MEASUREMENT_IN_SEC=$4
	CHANNEL_FROM=$5
	CHANNEL_TO=$6

  case "$MEASUREMENT" in
  "0")
    python2 ./signal_to_noise_ratio/SNRMeasurementStarter.py $OUTPUT_DIR $MEASUREMENT_IN_SEC $CHANNEL_FROM $CHANNEL_TO
    python2 ./potency_of_signal/PSMeasurementStarter.py $OUTPUT_DIR $MEASUREMENT_IN_SEC $CHANNEL_FROM $CHANNEL_TO
    ;;
  "1")
    python2 ./signal_to_noise_ratio/SNRMeasurementStarter.py $OUTPUT_DIR $MEASUREMENT_IN_SEC $CHANNEL_FROM $CHANNEL_TO
    ;;
  "2")
    python2 ./potency_of_signal/PSMeasurementStarter.py $OUTPUT_DIR $MEASUREMENT_IN_SEC $CHANNEL_FROM $CHANNEL_TO
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
    python2 ./src/MeasurementPlotter.py $PLOTTER $OUTPUT_DIR $INPUT_DIR $FILE_PATTERN1
  elif [ $# -eq 5  ]; then
    FILE_PATTERN2=$6
    python2 ./src/MeasurementPlotter.py $PLOTTER $OUTPUT_DIR $INPUT_DIR $FILE_PATTERN1 $FILE_PATTERN2
  else
    FILE_PATTERN2=$6
    FILE_PATTERN3=$7
    python2 ./src/MeasurementPlotter.py $PLOTTER $OUTPUT_DIR $INPUT_DIR $FILE_PATTERN1 $FILE_PATTERN2 $FILE_PATTERN3
  fi
  exit 0
  ;;
 *)
  echo "incorrect option" >&2
  print_info_and_exit
 esac
