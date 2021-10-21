import pkmodel as pk

params = pk.IV_Parameters(
        Q_pc= 1.0,
        V_c= 1.0,
        V_p= 1.0,
        CL= 1.0,
        q_c0= 0.0,
        q_p0= 0.0,
)
soln = pk.NumpyDataCollector()

def doseFn(x: float) -> float: return x*x

model = pk.IvModelScipy(params, soln, doseFn, 10, 1000)
model.solve()

soln.writeToFile('Test.csv')