""" trigger/02000356_bf/bossspawn.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 시작대기중(state.State):
    def on_enter(self):
        set_portal(portalId=11, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030], arg2=False)
        set_interact_object(triggerIds=[10000259,10000260,10000261], state=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라이동01()

state.DungeonStart = DungeonStart


class 카메라이동01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013], visible=False, arg3=0, arg4=0, arg5=0)
        add_buff(boxIds=[102], skillId=70000107, level=1, arg4=False, arg5=False)
        show_guide_summary(entityId=20003563, textId=20003563, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        select_camera(triggerId=303, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라이동02()


class 카메라이동02(state.State):
    def on_enter(self):
        select_camera(triggerId=304, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 카메라이동03()


class 카메라이동03(state.State):
    def on_enter(self):
        select_camera(triggerId=305, enable=True)
        show_guide_summary(entityId=20003562, textId=20003562, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 오브젝트반응대기()


class 오브젝트반응대기(state.State):
    def on_enter(self):
        select_camera(triggerId=305, enable=False)
        remove_buff(boxId=102, skillId=70000107)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000259,10000260,10000261], arg2=2):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1099])
        select_camera(triggerId=306, enable=True)
        add_buff(boxIds=[102], skillId=70000107, level=1, arg4=False, arg5=False)
        show_guide_summary(entityId=20003561, textId=20003561, duration=6000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            select_camera(triggerId=306, enable=False)
            remove_buff(boxId=102, skillId=70000107)
            return 종료체크()


class 종료체크(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1099]):
            return 종료딜레이()


class 종료딜레이(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            dungeon_clear()
            set_portal(portalId=11, visible=True, enabled=True, minimapVisible=True)
            return 종료()


class 종료(state.State):
    pass


