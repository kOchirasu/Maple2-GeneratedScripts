""" trigger/02000304_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_actor(triggerId=201, visible=False, initialSequence='Closed_A')
        set_actor(triggerId=202, visible=False, initialSequence='Closed_A')
        set_actor(triggerId=203, visible=True, initialSequence='sf_functobj_monitor_C01_On')
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_portal(portalId=98, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=99, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10000646], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            create_monster(spawnIds=[2001], arg2=False)
            return 연출시작()


class 연출시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 카메라이동대기()


class 카메라이동대기(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4500):
            return 전투시작대기()


class 전투시작대기(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20003041, textId=20003041, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=301, enable=False)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[2001]):
            return 전투시작()


class 전투시작(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2001, script='$02000304_BF__MAIN__1$', arg4=3)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            set_actor(triggerId=203, visible=False, initialSequence='sf_functobj_monitor_C01_On')
            set_interact_object(triggerIds=[10000646], state=1)
            return 반응대기()


class 반응대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[603], visible=True)
        show_guide_summary(entityId=20003003, textId=20003003)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000646], arg2=0):
            hide_guide_summary(entityId=20003003)
            set_effect(triggerIds=[603], visible=False)
            set_effect(triggerIds=[602], visible=True)
            set_achievement(triggerId=999, type='trigger', achieve='ClearTimehole')
            return 미션성공()


class 미션성공(state.State):
    def on_enter(self):
        dungeon_clear()
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        set_actor(triggerId=202, visible=True, initialSequence='Closed_A')
        set_portal(portalId=99, visible=False, enabled=True, minimapVisible=True)
        set_portal(portalId=98, visible=False, enabled=True, minimapVisible=True)
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 종료2()


class 종료2(state.State):
    pass


