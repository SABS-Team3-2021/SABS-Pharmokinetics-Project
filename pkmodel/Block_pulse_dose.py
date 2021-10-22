
class blockPulse():

    """ A block dosing function that can add multiple block pulses of a dose,
        each dose pulse has a beginning time, end time and dose ammount
    """
    def __init__(self):
        self.pulses = {}
   
    def add_pulse(self, start_time, stop_time, dose) -> None:
        """ Method to add individual pulses
            Parameters:
            start_time: time at beginning of dosing pulse
            stop_time: time at end of dosing pulse
            dose: concentration of dose
        """
        self.pulses[start_time, stop_time] = dose
        return

    def __call__(self, x : float) -> float:
        """ Calls dosing function to be used in solution of PK models
        """
        current = 0
        for key in self.pulses:
            pulseAmmount = self.pulses[key]
            startTime = key[0]
            stopTime=key[1]
            if x >= startTime and x < stopTime:
                current += pulseAmmount
        return current