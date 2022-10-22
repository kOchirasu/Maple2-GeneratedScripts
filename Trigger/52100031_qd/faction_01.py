""" trigger/52100031_qd/faction_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=99910150)
        set_interact_object(triggerIds=[10002058], state=2)
        set_interact_object(triggerIds=[10002059], state=2)
        set_interact_object(triggerIds=[10002067], state=2)

    def on_tick(self) -> state.State:
        if user_value(key='faction01', value=1):
            return 석궁준비()


class 석궁준비(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=1001, script='$52100031_QD__FACTION_01__0$', arg4=5, arg5=0)
        set_conversation(type=1, spawnId=1001, script='$52100031_QD__FACTION_01__1$', arg4=5, arg5=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 퀘스트()


class 퀘스트(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20040101, textId=20040101, duration=3500)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_interact_object(triggerIds=[10002067], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 종료체크()


class 종료체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2901]):
            set_interact_object(triggerIds=[10002058], state=0)
            set_interact_object(triggerIds=[10002059], state=0)
            set_interact_object(triggerIds=[10002067], state=0)
            set_conversation(type=1, spawnId=1001, script='$52100031_QD__FACTION_01__2$', arg4=5, arg5=0)
            remove_buff(boxId=199, skillId=99910150)
            return NPC삭제대기()


class NPC삭제대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='DungeonClear', value=1):
            destroy_monster(spawnIds=[1001,1002,1003,1004,1005], arg2=False)
            return 종료()


class 종료(state.State):
    pass


