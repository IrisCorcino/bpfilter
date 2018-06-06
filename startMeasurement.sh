print_info_and_exit() {
  echo "Usage: $0 OUTPUT_DIRECTORY SECONDS_PER_CHANNEL" >&2
  exit 1
}

# Check if the number of parameters is correct
if [[ $# != 2 ]]; then
  echo "Wrong number of parameters"
  print_info_and_exit
fi

# Check if first parameter is an existing directory
if ! [ -d "$1" ]; then
  echo "first parameter is not a valid output directory"
  print_info_and_exit
fi

# Check if variable evaluation in an arithmetic context is equal to itself
if [[ $(($2)) != $2 ]]; then
  echo "second parameter is not a number"
  print_info_and_exit
fi

TARGET_DIR = $1
MEASUREMENT_IN_SEC = $2
source ~/pybombs/prefix/default/setup_env.sh
python2 ./MeasurementStarter.py $TARGET_DIR $MEASUREMENT_IN_SEC
