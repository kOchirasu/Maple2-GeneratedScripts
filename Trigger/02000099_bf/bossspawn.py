""" trigger/02000099_bf/bossspawn.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 시작대기중(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20000991, textId=20000991, duration=5000)
        select_camera(triggerId=301, enable=True)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,2000], arg2=False)
        add_buff(boxIds=[199], skillId=70000107, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 시작()

    def on_exit(self):
        select_camera(triggerId=301, enable=False)
        remove_buff(boxId=199, skillId=70000107)

state.DungeonStart = DungeonStart


class 시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20000992, textId=20000992, duration=3000)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 시작가이드2()


class 시작가이드2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 차등장1()


class 차등장1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2001], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='SetSkillA', value=1):
            set_mesh(triggerIds=[3101,3102,3103,3104,3105,3106], visible=False, arg3=0, arg4=0, arg5=0)
            return 차등장대기2()


class 차등장대기2(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 차등장2()


class 차등장2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2002], arg2=False)

    def on_tick(self) -> state.State:
        if user_value(key='SetSkillB', value=1):
            set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208], visible=False, arg3=0, arg4=0, arg5=0)
            return 엘리트등장()


class 엘리트등장(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2000]):
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            show_guide_summary(entityId=20000993, textId=20000993, duration=5000)
            set_mesh(triggerIds=[3301,3302,3303,3304,3305,3306,3307,3308,3309,3310,3311], visible=False, arg3=0, arg4=0, arg5=0)
            return 엘리트처치()


class 엘리트처치(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            show_guide_summary(entityId=20000994, textId=20000994, duration=3000)
            return 종료()


class 종료(state.State):
    pass


