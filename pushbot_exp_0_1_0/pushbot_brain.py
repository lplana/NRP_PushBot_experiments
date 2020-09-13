# -*- coding: utf-8 -*-

"""
#------------------------------
# PushBot brain
#
# basic brain with 2 neurons, each one controlling the velocity of
# of the weheels on one side of the PushBot.
#
#NOTE: The PushBot has continuous tracks while the model has independent wheels
#
#NOTE: this brain assumes that the two wheels on each side will be
#NOTE: controlled together to make them act as a track
#------------------------------
"""
# pragma: no cover

__author__ = 'lap'

from hbp_nrp_cle.brainsim import simulator as sim
import numpy as np
import logging

logger = logging.getLogger(__name__)

def create_brain():
    # neuron parameters that provide smooth and symmetric
    # wheel movement
    WHEEL_NEURON_PARAMS = {
        'v_rest'    : -60.5,
        'cm'        : 0.025,
        'tau_m'     : 10.,
        'tau_refrac': 10.0,
        'tau_syn_E' : 2.5,
        'tau_syn_I' : 2.5,
        'e_rev_E'   : 0.0,
        'e_rev_I'   : -75.0,
        'v_thresh'  : -60.0,
        'v_reset'   : -60.5
        }

    # stimulus-to-wheels synaptic parameters
    WEIGHT_STIMULUS_TO_WHEELS = 1.5e-4
    DELAY = 0.1

    # PushBot wheel velocity is controlled by neuron membrane potentials
    # both left-side wheels are controlled by the same neuron
    left_wheels_neuron = sim.Population(
        1,
        sim.IF_cond_exp(**WHEEL_NEURON_PARAMS),
        label="left_wheels_neuron"
        )

    # both right-side wheels are controlled by the same neuron
    right_wheels_neuron = sim.Population(
        1,
        sim.IF_cond_exp(**WHEEL_NEURON_PARAMS),
        label="right_wheels_neuron"
        )

    # setup a source of spikes that will make the PushBot turn
    stimulus = sim.Population(
        1,
        sim.SpikeSourceArray(
            spike_times = [i * 100 for i in range(100)]
            ),
        label = "stimulus"
        )

    # setup a synaptic connection from the stimulus to the neurons
    stim_to_wheels = sim.StaticSynapse(
        weight=abs(WEIGHT_STIMULUS_TO_WHEELS),
        delay=DELAY
        )

    # on left side use inhibitory receptor type to make the PushBot turn CCW
    sim.Projection(
        stimulus,
        left_wheels_neuron,
        connector     = sim.AllToAllConnector(),
        synapse_type  = stim_to_wheels,
        receptor_type = 'inhibitory'
        )

    # on right side use excitatory receptor type to make the PushBot turn CCW
    sim.Projection(
        stimulus,
        right_wheels_neuron,
        connector     = sim.AllToAllConnector(),
        synapse_type  = stim_to_wheels,
        receptor_type = 'excitatory'
        )

    return {"left_wheels_neuron" : left_wheels_neuron,
            "right_wheels_neuron" : right_wheels_neuron,
            "stimulus" : stimulus}


circuit = create_brain()
