""" trigger/02000022_bf/ia_110.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_actor(triggerId=110, visible=False, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000099], arg2=0):
            return 개구리보이기()


class 개구리보이기(state.State):
    def on_enter(self):
        set_actor(triggerId=110, visible=True, initialSequence='Idle_A')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000099], arg2=1):
            return 시작대기중()

    def on_exit(self):
        set_actor(triggerId=110, visible=False, initialSequence='Idle_A')


