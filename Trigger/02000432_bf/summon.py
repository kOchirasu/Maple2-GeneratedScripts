""" trigger/02000432_bf/summon.xml """
from common import *
import state


class 룸체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 소환()


class 소환(state.State):
    def on_enter(self):
        set_skip(state=죽음대기)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 죽음대기()


class 죽음대기(state.State):
    def on_enter(self):
        set_skip()

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 셀린사망()
        if monster_dead(boxIds=[2002]):
            return 피리스사망()


class 셀린사망(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2002, script='$02000432_BF__SUMMON__1$', arg4=4, arg5=0)
        add_buff(boxIds=[2002], skillId=40500011, level=1, arg4=True, arg5=False)

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
        set_conversation(type=1, spawnId=2001, script='$02000432_BF__SUMMON__0$', arg4=4, arg5=0)
        add_buff(boxIds=[2001], skillId=40500011, level=1, arg4=True, arg5=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            set_achievement(triggerId=199, type='trigger', achieve='SirenDualKill')
            return 종료()
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    pass


