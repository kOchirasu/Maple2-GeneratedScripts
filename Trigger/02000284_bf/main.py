""" trigger/02000284_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000428], state=2)
        set_interact_object(triggerIds=[10000430], state=2)
        set_interact_object(triggerIds=[10000431], state=2)
        set_interact_object(triggerIds=[10000432], state=2)
        set_interact_object(triggerIds=[10000433], state=2)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 보스연출()


class 보스연출(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[2001], arg2=False)
        select_camera(triggerId=3001, enable=True)
        set_skip(state=준비)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 준비()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=3001, enable=False)


class 준비(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002815, textId=20002815, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 반응대기()


class 반응대기(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            set_interact_object(triggerIds=[10000428], state=1)
            show_guide_summary(entityId=20002814, textId=20002814)
            play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            return 반응체크()


class 반응체크(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000428], arg2=0):
            hide_guide_summary(entityId=20002814)
            dungeon_clear()
            set_mesh(triggerIds=[301,302,303,304,305,306,307,308], visible=True, arg3=0, arg4=100, arg5=0)
            set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
            return 소멸대기()


class 소멸대기(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 소멸()


class 소멸(state.State):
    pass


