# Imported Python Transfer Function
#

@nrp.MapRobotPublisher("back_left", Topic('/pushbot/back_left_joint/cmd_vel', std_msgs.msg.Float64))
@nrp.MapRobotPublisher("back_right", Topic('/pushbot/back_right_joint/cmd_vel', std_msgs.msg.Float64))
@nrp.MapRobotPublisher("front_left", Topic('/pushbot/front_left_joint/cmd_vel', std_msgs.msg.Float64))
@nrp.MapRobotPublisher("front_right", Topic('/pushbot/front_right_joint/cmd_vel', std_msgs.msg.Float64))
@nrp.Neuron2Robot()
def turn_around(t, back_left, back_right, front_left, front_right):
    vel_left = -5
    vel_right = 5
    back_left.send_message(std_msgs.msg.Float64(vel_left))
    front_left.send_message(std_msgs.msg.Float64(vel_left))
    back_right.send_message(std_msgs.msg.Float64(vel_right))
    front_right.send_message(std_msgs.msg.Float64(vel_right))
