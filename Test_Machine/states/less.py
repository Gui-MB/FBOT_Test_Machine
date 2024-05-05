import smach
import rospy

class RandomNumber(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['succeeded', 'preempted'])

    def execute(self):
        if self.preempt_requested():
            return 'preempted'

        else:
            print('O valor gerado é menor ou igual a 5')
            return 'succeeded'