import pkmodel as pk
import json

cfg = json.load(open('config.json'))
pk.run(cfg)

def run(cfg):
    assert "modelConfig" in cfg
    outfiles = solveModelFromConfig(cfg["modelConfig"])
    if "plotConfig" in cfg:
        plotFromConfig(cfg["plotConfig"], outfiles)