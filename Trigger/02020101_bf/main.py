""" trigger/02020101_bf/main.xml """
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
        dungeon_reset_time(seconds=420)
        create_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5670):
            return 조건추가()


class 조건추가(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 보스전_성공()
        if dungeon_check_play_time(playSeconds=420, operator='Equal'):
            return 보스전_타임어택실패()
        if user_value(key='SkillBreakFail', value=1):
            return 보스전_스킬브레이크실패()


class 보스전_스킬브레이크실패(state.State):
    def on_enter(self):
        dungeon_stop_timer()
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 보스전_리셋세팅()


class 보스전_타임어택실패(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 보스전_타임어택실패세팅()


class 보스전_리셋세팅(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        move_user(mapId=2020101, portalId=1, boxId=1002)
        remove_buff(boxId=1003, skillId=70002122, arg3=True)
        remove_buff(boxId=1003, skillId=70002151, arg3=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기()


class 보스전_타임어택실패세팅(state.State):
    def on_enter(self):
        dungeon_set_end_time()
        dungeon_close_timer()
        remove_buff(boxId=1003, skillId=70002151, arg3=True)


class 보스전_성공(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23038005)
        dungeon_set_end_time()
        # <action name="DungeonCloseTimer" />
        side_npc_talk(type='talk', npcId=23501001, illust='Turned_Yuperia_normal', script='$02020101_BF__MAIN__1$', duration=7940, voice='ko/Npc/00002207')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7940):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        dungeon_clear()
        set_achievement(type='trigger', achieve='ClearGreenLapenta')
        remove_buff(boxId=1003, skillId=70002151, arg3=True)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)


