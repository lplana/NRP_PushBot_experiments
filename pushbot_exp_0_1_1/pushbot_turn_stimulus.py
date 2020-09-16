@nrp.MapSpikeSource("neuron_pop", nrp.brain.neuron_pop, nrp.fixed_frequency)
@nrp.Robot2Neuron()
def pushbot_turn_stimulus(t, neuron_pop):
#    clientLogger.info("stimulus")
    neuron_pop.rate = 100.0
