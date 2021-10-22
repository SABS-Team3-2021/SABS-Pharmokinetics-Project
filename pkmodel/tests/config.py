modelConfigsSuccess = [
    {"model": "IV","protocols": [{"Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 1.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol1Output.csv"},{"Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 2.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol2Output.csv"}],"numIterations": 100,"numCompartments": 2,"tspan": 10},
    {"model": "IV","protocol": {"Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 1.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol1Output.csv"},"numIterations": 100,"numCompartments": 2,"tspan": 10},
    {"model": "IV","protocols": [{"Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 1.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol1Output.csv"},{"Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 2.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0}],"numIterations": 100,"numCompartments": 2,"tspan": 10},
    {"model": "Subcut","protocols": [{"k_a": 1, "q_e0": 0, "Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 1.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol1Output.csv"},{"k_a": 1, "q_e0": 0, "Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 2.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol2Output.csv"}],"numIterations": 100,"numCompartments": 2,"tspan": 10},
    {"model": "subcut","protocol": {"k_a": 1, "q_e0": 0, "Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 1.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol1Output.csv"},"numIterations": 100,"numCompartments": 2,"tspan": 10},
]

modelConfigsFail = [
    {"protocols": [{"Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 1.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol1Output.csv"},{"Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 2.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol2Output.csv"}],"numIterations": 100,"numCompartments": 2,"tspan": 10},
    {"model": "a","protocols": [{"k_a": 1, "q_e0": 0, "Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 1.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol1Output.csv"},{"k_a": 1, "q_e0": 0, "Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 2.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol2Output.csv"}],"numIterations": 100,"numCompartments": 2,"tspan": 10},
    {"model": "Subcut","numIterations": 100,"numCompartments": 2,"tspan": 10},
    {"model": "IV","protocol": {"Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 1.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol1Output.csv"},"numCompartments": 2,"tspan": 10},
    {"model": "IV","protocol": {"Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 1.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol1Output.csv"},"numIterations": 100,"tspan": 10},
    {"model": "IV","protocol": {"Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 1.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol1Output.csv"},"numIterations": 100,"numCompartments": 2,},
]

fullConfigSuccess = [
    {"modelConfig":{"model": "IV","protocol": {"Q_p1": 1,"Q_p2": 1,"V_c": 1.0,"V_p1": 1.0,"V_p2": 1,"CL": 1.0,"q_c0": 0.0,"q_p1_0": 0.0,"q_p2_0": 0,"outfile": "protocol1Output.csv"},"numIterations": 100,"numCompartments": 2,"tspan": 10},"plotConfig": {"plotVars": ["q_c"],"DoseLine": True,"DoseLineColour": ["r"],"ParameterLineColour": ["k", "b", "g"],"ParameterLabels": [],"ImageFileFormat": "png"}},
]