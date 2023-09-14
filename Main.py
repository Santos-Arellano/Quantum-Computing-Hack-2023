from qiskit import QuantumCircuit, Aer, transpile
from qiskit.visualization import plot_bloch_multivector, plot_histogram

# Crear un circuito cuántico
qc = QuantumCircuit(1)
qc.h(0)

# Visualizar el vector de estado resultante
simulator = Aer.get_backend('statevector_simulator')
job = simulator.run(transpile(qc, simulator))
result = job.result()
statevector = result.get_statevector()
plot_bloch_multivector(statevector)

# Medir el qubit y visualizar el histograma de resultados
qc.measure_all()
simulator = Aer.get_backend('qasm_simulator')
job = simulator.run(transpile(qc, simulator))
result = job.result()
counts = result.get_counts()
plot_histogram(counts)
