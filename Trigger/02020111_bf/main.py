""" trigger/02020111_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=900012, key='SkillBreakMissionReset', value=0)
        set_ambient_light(primary=[183,189,201])
        set_directional_light(diffuseColor=[192,210,211], specularColor=[170,170,170])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1007]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        remove_buff(boxId=1006, skillId=70002151, arg3=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 보스전_시작()


class 보스전_시작(state.State):
    def on_enter(self):
        set_user_value(triggerId=900012, key='SkillBreakMissionReset', value=1) # <스킬브레이크 던전 미션 체크시작>
        side_npc_talk(type='talk', npcId=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__MAIN__0$', duration=5684, voice='ko/Npc/00002201')
        dungeon_reset_time(seconds=420)
        create_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5684):
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
        set_user_value(triggerId=900012, key='SkillBreakMissionReset', value=0) # <스킬브레이크 던전 미션 리셋>
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=7, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=8, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=9, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        destroy_monster(spawnIds=[-1])
        move_user(mapId=2020111, portalId=1, boxId=1001)
        remove_buff(boxId=1006, skillId=70002151, arg3=True)

    def on_tick(self) -> state.State:
        if true():
            return 대기()


class 보스전_타임어택실패세팅(state.State):
    def on_enter(self):
        dungeon_set_end_time()
        dungeon_close_timer()
        remove_buff(boxId=1006, skillId=70002151, arg3=True)


class 보스전_성공(state.State):
    def on_enter(self):
        dungeon_mission_complete(missionId=23039005)
        dungeon_set_end_time()
        # <action name="DungeonCloseTimer" />
        side_npc_talk(type='talk', npcId=23501011, illust='Turned_Renduebian_normal', script='$02020111_BF__MAIN__1$', duration=3176, voice='ko/Npc/00002202')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3176):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        dungeon_clear()
        set_achievement(type='trigger', achieve='ClearBlueLapenta')
        remove_buff(boxId=1006, skillId=70002151, arg3=True)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=7, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=9, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)
        set_portal(portalId=12, visible=True, enabled=True, minimapVisible=True)


