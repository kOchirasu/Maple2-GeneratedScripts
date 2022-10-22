""" trigger/02000281_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302], visible=True, arg3=0, arg4=0)
        set_interact_object(triggerIds=[10000414], state=0)
        set_ladder(triggerIds=[321], visible=False, animationEffect=False)
        set_ladder(triggerIds=[322], visible=False, animationEffect=False)
        set_ladder(triggerIds=[323], visible=False, animationEffect=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015], arg2=False)
        set_interact_object(triggerIds=[10000414], state=1)
        select_camera(triggerId=3001, enable=True)
        add_buff(boxIds=[199], skillId=70000107, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 카메라대기()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

state.DungeonStart = DungeonStart


class 카메라대기(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002810, textId=20002810, duration=5000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 카메라이동()


class 카메라이동(state.State):
    def on_enter(self):
        select_camera(triggerId=3002, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 생성()

    def on_exit(self):
        remove_buff(boxId=199, skillId=70000107)
        select_camera(triggerId=3002, enable=False)


class 생성(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302], visible=False, arg3=0, arg4=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000414], arg2=0):
            return 보스()


class 보스(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2002], arg2=False)
        show_guide_summary(entityId=20002816, textId=20002816, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2002]):
            show_guide_summary(entityId=20002812, textId=20002812, duration=5000)
            play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            set_ladder(triggerIds=[321], visible=True, animationEffect=True)
            set_ladder(triggerIds=[322], visible=True, animationEffect=True)
            set_ladder(triggerIds=[323], visible=True, animationEffect=True)
            set_portal(portalId=2, visible=False, enabled=True, minimapVisible=True)
            return 종료()


class 종료(state.State):
    pass


