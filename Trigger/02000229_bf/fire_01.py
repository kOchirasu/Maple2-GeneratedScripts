""" trigger/02000229_bf/fire_01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000051], state=1)
        set_effect(triggerIds=[501], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000051], arg2=0):
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 딜레이()

    def on_exit(self):
        set_effect(triggerIds=[501], visible=True)
        create_monster(spawnIds=[101])


class 딜레이(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=101, script='$02000229_BF__FIRE_01__0$', arg4=2)
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 딜레이2()

    def on_exit(self):
        set_effect(triggerIds=[501], visible=False)
        destroy_monster(spawnIds=[101])


class 딜레이2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


