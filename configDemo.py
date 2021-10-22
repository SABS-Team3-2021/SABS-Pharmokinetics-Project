import pkmodel as pk
import json

config_file = json.load(open('config.json'))
pk.run(config_file)


def run(config_file):
    assert "modelConfig" in config_file
    outfiles = pk.solveModelFromConfig(config_file["modelConfig"])
    if "plotConfig" in config_file:
        pk.plotFromConfig(config_file, outfiles)

