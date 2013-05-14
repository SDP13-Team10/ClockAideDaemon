import daemon
from ClockAideGamma import clockaide_gamma_rev3

with daemon.DaemonContext():
	ClockAideGamma.main()
