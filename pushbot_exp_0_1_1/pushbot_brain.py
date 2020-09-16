from hbp_nrp_cle.brainsim import simulator as sim
import logging

logger = logging.getLogger (__name__)


def create_brain ():
    NEURON_PARAMS = {
        'v_rest'    : -60.5,
        'cm'        :   0.025,
        'tau_m'     :  10.0,
        'tau_refrac':  10.0,
        'tau_syn_E' :   2.5,
        'tau_syn_I' :   2.5,
        'e_rev_E'   :   0.0,
        'e_rev_I'   : -75.0,
        'v_thresh'  : -60.0,
        'v_reset'   : -60.5
        }

    neuron_pop = sim.Population (
        1,
        sim.IF_cond_alpha (**NEURON_PARAMS),
        label="neuron_pop"
        )

    return {"neuron_pop" : neuron_pop}


circuit = create_brain ()
