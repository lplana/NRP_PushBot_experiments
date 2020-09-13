#------------------------------
# PushBot wheel control
#
#NOTE: The PushBot has continuous tracks - the model has independent wheels
#NOTE: this function sends the same message to the two wheels on a side to
#NOTE: make them act as a track
#------------------------------
# PushBot brain neurons that control wheel movement
@nrp.MapSpikeSink(
    "left_wheels_neuron",
    nrp.brain.left_wheels_neuron, nrp.leaky_integrator_exp,
    weight=0.1
    )

@nrp.MapSpikeSink(
    "right_wheels_neuron",
    nrp.brain.right_wheels_neuron, nrp.leaky_integrator_exp,
    weight=0.1
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
def pushbot_wheel_control(
        t,
        left_wheels_neuron,
        right_wheels_neuron,
        back_left_wheel,
        back_right_wheel,
        front_left_wheel,
        front_right_wheel):

    # compute velocity commands
#    vel_left  = 100 * left_wheels_neuron.voltage
#    vel_right = 100 * right_wheels_neuron.voltage
    vel_left  = -5.0
    vel_right =  5.0

    # send same velocity command to both left-side wheels
    back_left_wheel.send_message(std_msgs.msg.Float64(vel_left))
    front_left_wheel.send_message(std_msgs.msg.Float64(vel_left))

    # send same velocity command to both right-side wheels
    back_right_wheel.send_message(std_msgs.msg.Float64(vel_right))
    front_right_wheel.send_message(std_msgs.msg.Float64(vel_right))
