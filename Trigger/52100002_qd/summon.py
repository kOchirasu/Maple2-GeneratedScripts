""" trigger/52100002_qd/summon.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='SummonSister', value=1):
            return 룸체크()


class 룸체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 소환()
        if not is_dungeon_room():
            return 퀘스트소환()


class 소환(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=300, enable=True)
        create_monster(spawnIds=[2002], arg2=False)
        set_effect(triggerIds=[602], visible=True)
        add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$02000392_BF__SUMMON__0$', align='left', duration=2000)
        set_skip(state=죽음대기)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            reset_camera(interpolationTime=1)
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            return 죽음대기()


class 퀘스트소환(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=300, enable=True)
        create_monster(spawnIds=[2102], arg2=False)
        set_effect(triggerIds=[602], visible=True)
        add_cinematic_talk(npcId=11003889, illustId='Firis_normal', msg='$02000392_BF__SUMMON__0$', align='left', duration=2000)
        set_skip(state=퀘스트죽음대기)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            reset_camera(interpolationTime=1)
            set_cinematic_ui(type=0)
            set_cinematic_ui(type=2)
            return 퀘스트죽음대기()


class 퀘스트죽음대기(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_skip()

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2101]):
            return 퀘스트셀린사망()
        if monster_dead(boxIds=[2102]):
            return 퀘스트피리스사망()


class 퀘스트셀린사망(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2102, script='$02000392_BF__SUMMON__1$', arg4=4, arg5=0)
        add_buff(boxIds=[2102], skillId=40442003, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 퀘스트피리스사망(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True)
        set_conversation(type=1, spawnId=2101, script='$02000392_BF__SUMMON__2$', arg4=4, arg5=0)
        add_buff(boxIds=[2101], skillId=40442003, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 죽음대기(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_skip()

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 셀린사망()
        if monster_dead(boxIds=[2002]):
            return 피리스사망()


class 셀린사망(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2002, script='$02000392_BF__SUMMON__1$', arg4=4, arg5=0)
        add_buff(boxIds=[2002], skillId=40442003, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2002]):
            set_achievement(triggerId=199, type='trigger', achieve='SirenDualKill')
            return 종료()
        if wait_tick(waitTick=2000):
            return 종료()


class 피리스사망(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True)
        set_achievement(triggerId=199, type='trigger', achieve='BigSisterFirst')
        set_conversation(type=1, spawnId=2001, script='$02000392_BF__SUMMON__2$', arg4=4, arg5=0)
        add_buff(boxIds=[2001], skillId=40442003, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            set_achievement(triggerId=199, type='trigger', achieve='SirenDualKill')
            return 종료()
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    pass


