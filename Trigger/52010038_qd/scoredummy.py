""" trigger/52010038_qd/scoredummy.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001258], arg2=0):
            return 점수()
        if object_interacted(interactIds=[10001259], arg2=0):
            return 점수()
        if object_interacted(interactIds=[10001260], arg2=0):
            return 점수()
        if object_interacted(interactIds=[10001261], arg2=0):
            return 점수()
        if object_interacted(interactIds=[10001262], arg2=0):
            return 점수()
        if object_interacted(interactIds=[10001263], arg2=0):
            return 점수()
        if object_interacted(interactIds=[10001264], arg2=0):
            return 점수()
        if object_interacted(interactIds=[10001265], arg2=0):
            return 점수()


class 점수(state.State):
    def on_enter(self):
        create_monster(spawnIds=[4030], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대기()


