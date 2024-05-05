import smach
import rospy
import random

class RandomNumber(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['succeeded', 'aborted', 'preempted'])
        
    def execute(self):
        self.value = random.randint(1, 10)

        print('O valor gerado foi: ' + self.value)

        if self.preempt_requested():
            return 'preempted'
        
        if self.value > 5:
            return 'succeeded'
        
        else:
            return 'aborted'