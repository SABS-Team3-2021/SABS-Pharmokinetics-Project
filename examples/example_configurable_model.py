import pk_model as pk

'''
Most of the configuration is given in the json file, with only the dosefunction
needing to be independantly set.
'''
doseFn = pk.create_periodic_dosing(.2, 5, 2, lowVal=0)
pk.process_config('example_configurable_directory.json', doseFn)
