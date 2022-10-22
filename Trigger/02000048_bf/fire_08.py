""" trigger/02000048_bf/fire_08.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000313], state=1)
        set_mesh(triggerIds=[208], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[308], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000313], arg2=0):
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if true():
            return NPC이동()

    def on_exit(self):
        set_mesh(triggerIds=[208], visible=True, arg3=0, arg4=0, arg5=1)
        set_effect(triggerIds=[308], visible=True)
        create_monster(spawnIds=[408], arg2=False)


class NPC이동(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=408, script='$02000048_BF__FIRE_08__0$', arg4=2)
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 몬스터와전투()


class 몬스터와전투(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[408]):
            return 딜레이()
        if not monster_in_combat(boxIds=[408]):
            return 몬스터소멸()


class 몬스터소멸(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[408]):
            reset_timer(timerId='1')
            return None
        if monster_dead(boxIds=[408]):
            return 소멸대기()
        if time_expired(timerId='1'):
            return 소멸대기()


class 소멸대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 딜레이()
        if monster_in_combat(boxIds=[408]):
            return 몬스터소멸()


class 딜레이(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[408])
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


