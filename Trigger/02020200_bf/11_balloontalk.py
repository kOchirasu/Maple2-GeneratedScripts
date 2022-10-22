""" trigger/02020200_bf/11_balloontalk.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[905]):
            return 대사1()


class 대사1(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020200_BF__11_BALLOONTALK__0$')
        add_balloon_talk(spawnId=0, msg='$02020200_BF__11_BALLOONTALK__1$', duration=5000, delayTick=1000)

    def on_tick(self) -> state.State:
        if all_of():
            return 대사2()
        if all_of():
            return 대사2()
        if all_of():
            return 대사2()
        if monster_dead(boxIds=[205]):
            return 종료()


class 대사2(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='$02020200_BF__11_BALLOONTALK__2$', duration=5000, delayTick=0)

    def on_tick(self) -> state.State:
        if check_npc_additional_effect(spawnId=205, additionalEffectId=42030261, level=1):
            return 대사3()


class 대사3(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11001813, illust='Turka_normal', duration=5000, script='$02020200_BF__11_BALLOONTALK__3$')
        add_balloon_talk(spawnId=0, msg='$02020200_BF__11_BALLOONTALK__4$', duration=5000, delayTick=0)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


