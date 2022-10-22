""" trigger/66200001_gd/03_removedropout.xml """
from common import *
import state


class Wait(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return Remove()


class Remove(state.State):
    def on_enter(self):
        move_to_portal(boxId=9002, userTagId=1, portalId=21) # Tag1=Blue
        move_to_portal(boxId=9002, userTagId=2, portalId=22) # Tag2=Red

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return Remove()


