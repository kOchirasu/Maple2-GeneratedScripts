""" trigger/02000194_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10001054], state=2)
        set_interact_object(triggerIds=[10001055], state=2)
        set_interact_object(triggerIds=[10001056], state=2)
        set_interact_object(triggerIds=[10001057], state=2)
        set_interact_object(triggerIds=[11000004], state=2)
        set_mesh(triggerIds=[3005,3006,3007], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3001,3002,3003,3004], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3101,3102,3103,3104], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3201,3202,3203], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3301,3302,3303,3304], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 던전시작()

state.DungeonStart = DungeonStart


class 던전시작(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20001941, textId=20001941, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_interact_object(triggerIds=[10001054], state=1)
        set_interact_object(triggerIds=[10001055], state=1)
        set_interact_object(triggerIds=[10001056], state=1)
        set_interact_object(triggerIds=[10001057], state=1)
        create_monster(spawnIds=[1001,1002,1003,1004,2000], arg2=False)
        select_camera(triggerId=301, enable=True)
        add_buff(boxIds=[101], skillId=70000107, level=1, arg4=False, arg5=False)
        set_skip(state=시작)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 시작()

    def on_exit(self):
        select_camera(triggerId=301, enable=False)
        set_mesh(triggerIds=[3005,3006,3007], visible=False, arg3=0, arg4=0, arg5=0)
        remove_buff(boxId=101, skillId=70000107)


class 시작(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20001942, textId=20001942, duration=5000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 시작2()


class 시작2(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001054], arg2=0):
            set_mesh(triggerIds=[3101,3102,3103,3104], visible=False, arg3=0, arg4=0, arg5=0)
            return 오브젝트2()


class 오브젝트2(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001055], arg2=0):
            set_mesh(triggerIds=[3201,3202,3203], visible=False, arg3=0, arg4=0, arg5=0)
            return 오브젝트3()


class 오브젝트3(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001056], arg2=0):
            set_mesh(triggerIds=[3301,3302,3303,3304], visible=False, arg3=0, arg4=0, arg5=0)
            return 오브젝트4()


class 오브젝트4(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001057], arg2=0):
            show_guide_summary(entityId=20001944, textId=20001944, duration=5000)
            play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            set_mesh(triggerIds=[3001,3002,3003,3004], visible=False, arg3=0, arg4=0, arg5=0)
            return 종료()


class 종료(state.State):
    pass


