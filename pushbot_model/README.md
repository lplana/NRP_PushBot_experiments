# PushBot model

#### Initial PushBot model provided by [Oskar Weinberger](oskarwei@kth.se) from KTH.

#### Current status:

- all physical parameters are in SI units,
- model size is roughly correct,
- dvs functionality is provided by the [DVS Gazebo Plugin](https://github.com/HBPNeurorobotics/gazebo_dvs_plugin),
- masses are set very high (approximately 1000 times their actual value),
- inertias have been set to either 1 or 0, due to apparent simulation bug for smaller inertias,
- tracks have not been implemented, the model has 4 independent wheels,
- meshes for visuals have not been implemented,
- laser pointer and LED functionality has not been implemented due to lack of Gazebo 7 support for lights as robot links.

Note: light functionality is available if using the model in standalone Gazebo 9. The relevant code is included in model.sdf but commented out.