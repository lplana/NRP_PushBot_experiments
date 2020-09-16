#------------------------------
# PushBot wheel control
#
#NOTE: The PushBot has continuous tracks - the model has independent wheels
#NOTE: this function sends the same message to the two wheels on a side to
#NOTE: make them act as a track
#------------------------------
# PushBot brain neurons that control wheel movement
@nrp.MapSpikeSink(
    "neuron_pop",
    nrp.brain.neuron_pop, nrp.nrp.leaky_integrator_alpha
    )
#------------------------------
# ROS topics to control PushBot wheels
@nrp.MapRobotPublisher(
    "back_left_wheel",
    Topic('/pushbot/back_left_joint/cmd_vel', std_msgs.msg.Float64)
    )

@nrp.MapRobotPublisher(
    "back_right_wheel",
    Topic('/pushbot/back_right_joint/cmd_vel', std_msgs.msg.Float64)
    )

@nrp.MapRobotPublisher(
    "front_left_wheel",
    Topic('/pushbot/front_left_joint/cmd_vel', std_msgs.msg.Float64)
    )

@nrp.MapRobotPublisher(
    "front_right_wheel",
    Topic('/pushbot/front_right_joint/cmd_vel', std_msgs.msg.Float64)
    )
#------------------------------
# brain to PushBot transfer function
@nrp.Neuron2Robot()
#------------------------------
#
def pushbot_wheel_control (
        t,
        neuron_pop,
        back_left_wheel,
        back_right_wheel,
        front_left_wheel,
        front_right_wheel
        ):

    # compute velocity commands
    pushbot_vel = 100 * neuron_pop.voltage
    vel_left  = -pushbot_vel
    vel_right =  pushbot_vel

    # send same velocity command to both left-side wheels
    back_left_wheel.send_message (std_msgs.msg.Float64(vel_left))
    front_left_wheel.send_message (std_msgs.msg.Float64(vel_left))

    # send same velocity command to both right-side wheels
    back_right_wheel.send_message (std_msgs.msg.Float64(vel_right))
    front_right_wheel.send_message (std_msgs.msg.Float64(vel_right))
