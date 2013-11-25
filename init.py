# Description: 
# Runs the init_generators.py wth all the given algorithms for
# various values of n.
# Reports the final results in files that are ready to be processed 
# later.

# Author:   Vlad Burca
# Date:     November 24, 2013
# Updated:  November 24, 2013

import start
import yaml

# Methods
ANGLUIN   = 'angluin'
MARGULIS  = 'margulis'
RANDOM_3  = 'random_3'
RANDOM_5  = 'random_5'

# VALUES for the number of nodes, n
# (replace code accordingly, for an incrementation strategy, if needed)
VALUES = [ 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000 ]

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


for v in VALUES:
  # Update config file with the new value for n
  config_file = open("config.yaml", "r")
  config_vals = yaml.safe_load(config_file)
  config_file.close()

  config_vals['params']['n'] = v     # update the new value

  # Prepare config file to write the new yaml dictionary
  config_file = open("config.yaml", "w")
  config_file.write(yaml.dump(config_vals, default_flow_style=False))   # update yaml dictionary in config file
  config_file.close()

  # Call the main method that runs the generating algorithms
  print "\n\n--------------------------------------------------"
  print "**** n = " + str(v) + " ****\n"
  start.generate_expanders()


# Write the final results to their coresponding files

# Angluin results
# angluin_result_file.write(yaml.dump(angluin_results, default_flow_style=False))
# angluin_result_file.close()

# Margulis results
# margulis_result_file.write(yaml.dump(martulis_results, default_flow_style=False))
# margulis_result_file.close()

# Random_3 results

# Random_5 results

print "Program is done. Results are in the .results files. Exiting ... "

