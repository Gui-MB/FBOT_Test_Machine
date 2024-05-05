import rospy
import smach

from states import gen_number, less, more

if __name__ == '__main__':
    rospy.init_node('draw')
    sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])

    with sm:
        smach.StateMachine.add("GEN_NUMBER", gen_number(),
        transitions={
        "succeeded": "MORE",
        "aborted": "LESS",
        "preempted": "preempted"
        }),
        smach.StateMachine.add("MORE", more(),
        transitions={
        "succeeded": "succeeded",
        "preempted": "preempted"
        })
        smach.StateMachine.add("LESS", less(),
        transitions={
        "succeeded": "succeeded",
        "preempted": "preempted"
        }),