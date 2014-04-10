# Description: 
# Runs the start.py wth all the given algorithms for
# various values of n.
# Reports the final results in files that are ready to be processed 
# later.

# Author:   Vlad Burca
# Date:     November 24, 2013
# Updated:  March 13, 2014

from start import generate_expanders
import yaml

import methods
from helpers import check_configured_run, cleanup

# VALUES for the number of nodes, n
# (replace code accordingly, for an incrementation strategy, if needed)
# VALUES = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30 ]
VALUES = [2, 20, 30]


# Open results files
# angluin_result_file   = open("angluin.results", "w")
# margulis_result_file  = open("margulis.results", "w")
# random3_result_file   = open("random3.results", "w")
# random5_result_file   = open("random5.results", "w")

# Create results dictionaries for the yaml write
# angluin_results   = { ANGLUIN:  {} }
# margulis_results  = { MARGULIS: {} }
# random3_results   = { RANDOM_3: {} }
# random5_results   = { RANDOM_5: {} }

print "Starting main program ... \n\n"

# Run only if there is any algorithm configured to run
if check_configured_run(methods.ANGLUIN, methods.MARGULIS, methods.AJTAI, \
                        methods.RANDOM_3, methods.RANDOM_5):
  
  # Load configuration parameters
  config_file = open("config.yaml", "r")
  config_vars = yaml.safe_load(config_file)
  config_file.close()

  # Clean existing .results files
  if config_vars['params']['clear_results_files'] == True:
    cleanup(".results")

  for v in VALUES:

    config_vars['params']['n'] = v     # update the new n value

    # Prepare config file to write the new yaml dictionary
    config_file = open("config.yaml", "w")
    config_file.write(yaml.dump(config_vars, default_flow_style=False))   # update yaml dictionary in config file
    config_file.close()

    # Call the main method that runs the generating algorithms
    print "\n\n--------------------------------------------------"
    print "**** n = " + str(v) + " ****\n"
    generate_expanders()

  print "\n\n--------------------------------------------------"
  print "Program is done. Results are in the .results files. Exiting ... \n"

else:
  print "\n\n--------------------------------------------------"
  print "Program is done. No algorithm was configured to run. Exiting ... \n"



# Write the final results to their coresponding files

# Angluin results
# angluin_result_file.write(yaml.dump(angluin_results, default_flow_style=False))
# angluin_result_file.close()

# Margulis results
# margulis_result_file.write(yaml.dump(martulis_results, default_flow_style=False))
# margulis_result_file.close()

# Random_3 results

# Random_5 results
