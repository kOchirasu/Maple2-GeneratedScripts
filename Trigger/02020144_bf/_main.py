""" trigger/02020144_bf/_main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        remove_buff(boxId=1003, skillId=70002151, arg3=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1002]):
            return 보스전_시작()


class 보스전_시작(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=23501001, illust='Turned_Yuperia_normal', script='$02020101_BF__MAIN__0$', duration=5670, voice='ko/Npc/00002206')
        create_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5670):
            return 조건추가()


class 조건추가(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 보스전_성공()


class 보스전_성공(state.State):
    def on_enter(self):
        set_achievement(type='trigger', achieve='ClearGreenLapenta_Quest')
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)
        side_npc_talk(type='talk', npcId=23501001, illust='Turned_Yuperia_normal', script='$02020101_BF__MAIN__1$', duration=7940, voice='ko/Npc/00002207')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7940):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        # <action name="업적이벤트를발생시킨다" arg2="trigger" arg3="ClearGreenLapenta"/>


