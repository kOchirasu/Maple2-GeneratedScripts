""" trigger/66200001_gd/03_removedropout.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9002]):
            return Remove(self.ctx)


class Remove(common.Trigger):
    def on_enter(self):
        self.move_to_portal(boxId=9002, userTagId=1, portalId=21) # Tag1=Blue
        self.move_to_portal(boxId=9002, userTagId=2, portalId=22) # Tag2=Red

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9002]):
            return Remove(self.ctx)


initial_state = Wait
