""" trigger/02000299_bf/menual.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=False)
        set_interact_object(triggerIds=[10000490], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000490], arg2=0):
            return 안내시작()


class 안내시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)
        select_camera(triggerId=301, enable=True)
        add_buff(boxIds=[104], skillId=70000107, level=1, arg4=False, arg5=False)
        show_guide_summary(entityId=20003011, textId=20003011, duration=2500)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 안내01()


class 안내01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)
        show_guide_summary(entityId=20003012, textId=20003012, duration=3000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 안내02()


class 안내02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)
        select_camera(triggerId=302, enable=True)
        show_guide_summary(entityId=20003013, textId=20003013, duration=3000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 안내03()


class 안내03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)
        select_camera(triggerId=303, enable=True)
        set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=1)
        show_guide_summary(entityId=20003014, textId=20003014, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 안내04()


class 안내04(state.State):
    def on_enter(self):
        add_buff(boxIds=[104], skillId=70000107, level=1, arg4=False, arg5=False)
        set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=0)
        set_effect(triggerIds=[604], visible=True)
        select_camera(triggerId=301, enable=True)
        show_guide_summary(entityId=20003015, textId=20003015, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 안내05()


class 안내05(state.State):
    def on_enter(self):
        remove_buff(boxId=104, skillId=70000107)
        set_effect(triggerIds=[604], visible=True)
        select_camera(triggerId=303, enable=False)
        show_guide_summary(entityId=20003016, textId=20003016, duration=2000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 대기()


