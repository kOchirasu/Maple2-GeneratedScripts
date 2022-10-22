""" trigger/02000299_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=False, arg3=0, arg4=0, arg5=0)
        create_monster(spawnIds=[1010,1011,1012,1013], arg2=True)
        set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        set_interact_object(triggerIds=[10000494,10000495,10000496,10000497,10000498,10000499], state=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 클리어체크()


class 클리어체크(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False) # Eff_dungeon_allert_01
        set_effect(triggerIds=[602], visible=False) # Eff_Sound_Dungeon_Object_Scifi_Door_Open
        set_effect(triggerIds=[603], visible=False) # Eff_Sound_Dungeon_Object_Scifi_Door_Open
        set_effect(triggerIds=[604], visible=False) # Eff_UI_Sound_notice_01
        set_effect(triggerIds=[605], visible=False) # Eff_sf_fi_prop_incubator_B02_wfx_Big
        set_effect(triggerIds=[606], visible=False) # Eff_electricity
        set_effect(triggerIds=[607], visible=False) # Eff_electricity
        set_effect(triggerIds=[610], visible=False) # Eff_Sound_RedAllert

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 클리어체크2()


class 클리어체크2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=False, arg3=0, arg4=0, arg5=5)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1010]):
            return 타임머신중지()
        if monster_dead(boxIds=[1011]):
            return 타임머신중지()
        if monster_dead(boxIds=[1012]):
            return 타임머신중지()
        if monster_dead(boxIds=[1013]):
            return 타임머신중지()
        if wait_tick(waitTick=100):
            return 정황설명()


class 정황설명(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002990, textId=20002990, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 시간반응대기()


class 시간반응대기(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002992, textId=20002992, duration=4000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_interact_object(triggerIds=[10000494,10000495], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000494], arg2=0):
            return 미래시간()
        if object_interacted(interactIds=[10000495], arg2=0):
            return 과거시간()


class 미래시간(state.State):
    def on_enter(self):
        set_effect(triggerIds=[606], visible=True)
        set_effect(triggerIds=[604], visible=True)
        show_guide_summary(entityId=20002987, textId=20002987)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_interact_object(triggerIds=[10000495], state=0)
        set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000496], arg2=0):
            return 그런거없음()
        if object_interacted(interactIds=[10000497], arg2=0):
            return 미래엘리니아()
        if object_interacted(interactIds=[10000498], arg2=0):
            return 그런거없음()
        if object_interacted(interactIds=[10000499], arg2=0):
            return 미래커닝시티()

    def on_exit(self):
        hide_guide_summary(entityId=20002987)
        set_effect(triggerIds=[607], visible=True)
        set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=0)


class 과거시간(state.State):
    def on_enter(self):
        set_effect(triggerIds=[606], visible=True)
        set_effect(triggerIds=[604], visible=True)
        show_guide_summary(entityId=20002988, textId=20002988)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_interact_object(triggerIds=[10000494], state=0)
        set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000496], arg2=0):
            return 과거헤네니스()
        if object_interacted(interactIds=[10000497], arg2=0):
            return 그런거없음()
        if object_interacted(interactIds=[10000498], arg2=0):
            return 과거페리온()
        if object_interacted(interactIds=[10000499], arg2=0):
            return 그런거없음()

    def on_exit(self):
        hide_guide_summary(entityId=20002988)
        set_effect(triggerIds=[607], visible=True)
        set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=0)


class 미래엘리니아(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[604], visible=True)
        show_guide_summary(entityId=20002989, textId=20002989)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            hide_guide_summary(entityId=20002989)
            return 미래엘리니아2()


class 미래엘리니아2(state.State):
    def on_enter(self):
        move_user(mapId=2000299, portalId=2, boxId=104)
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[602], visible=True)
        set_effect(triggerIds=[604], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='Opened_A')
        show_count_ui(text='$02000299_BF__MAIN__3$', stage=1, count=3)
        set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 미래엘리니아이동()


class 미래엘리니아이동(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_effect(triggerIds=[603], visible=True)
        set_effect(triggerIds=[601], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        set_effect(triggerIds=[605], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            move_user(mapId=2000302, portalId=1, boxId=104)
            set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 클리어체크()

    def on_exit(self):
        destroy_monster(spawnIds=[1010])
        set_effect(triggerIds=[603], visible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=True, arg3=0, arg4=0, arg5=5)


class 미래커닝시티(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[604], visible=True)
        show_guide_summary(entityId=20002989, textId=20002989)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            hide_guide_summary(entityId=20002989)
            return 미래커닝시티2()


class 미래커닝시티2(state.State):
    def on_enter(self):
        move_user(mapId=2000299, portalId=2, boxId=104)
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[602], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='Opened_A')
        set_effect(triggerIds=[604], visible=True)
        show_count_ui(text='$02000299_BF__MAIN__5$', stage=1, count=3)
        set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 미래커닝시티이동()


class 미래커닝시티이동(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_effect(triggerIds=[603], visible=True)
        set_effect(triggerIds=[601], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        set_effect(triggerIds=[605], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            move_user(mapId=2000301, portalId=1, boxId=104)
            set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 클리어체크()

    def on_exit(self):
        destroy_monster(spawnIds=[1011])
        set_effect(triggerIds=[603], visible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=True, arg3=0, arg4=0, arg5=5)


class 과거헤네니스(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[604], visible=True)
        show_guide_summary(entityId=20002989, textId=20002989)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            hide_guide_summary(entityId=20002989)
            return 과거헤네니스2()


class 과거헤네니스2(state.State):
    def on_enter(self):
        move_user(mapId=2000299, portalId=2, boxId=104)
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[602], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='Opened_A')
        set_effect(triggerIds=[604], visible=True)
        show_count_ui(text='$02000299_BF__MAIN__7$', stage=1, count=3)
        set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 과거헤네니스이동()


class 과거헤네니스이동(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_effect(triggerIds=[603], visible=True)
        set_effect(triggerIds=[601], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        set_effect(triggerIds=[605], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            move_user(mapId=2000303, portalId=1, boxId=104)
            set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 클리어체크()

    def on_exit(self):
        destroy_monster(spawnIds=[1012])
        set_effect(triggerIds=[603], visible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=True, arg3=0, arg4=0, arg5=5)


class 과거페리온(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[604], visible=True)
        show_guide_summary(entityId=20002989, textId=20002989)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            hide_guide_summary(entityId=20002989)
            return 과거페리온2()


class 과거페리온2(state.State):
    def on_enter(self):
        move_user(mapId=2000299, portalId=2, boxId=104)
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[602], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='Opened_A')
        set_effect(triggerIds=[604], visible=True)
        show_count_ui(text='$02000299_BF__MAIN__9$', stage=1, count=3)
        set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 과거페리온이동()


class 과거페리온이동(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2)
        set_effect(triggerIds=[603], visible=True)
        set_effect(triggerIds=[601], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        set_effect(triggerIds=[605], visible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            move_user(mapId=2000300, portalId=1, boxId=104)
            set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 클리어체크()

    def on_exit(self):
        destroy_monster(spawnIds=[1013])
        set_effect(triggerIds=[603], visible=False)
        set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=True, arg3=0, arg4=0, arg5=5)


class 그런거없음(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        set_effect(triggerIds=[604], visible=True)
        show_guide_summary(entityId=20002989, textId=20002989)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            hide_guide_summary(entityId=20002989)
            return 그런거없음2()


class 그런거없음2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[606], visible=False)
        set_effect(triggerIds=[607], visible=False)
        set_effect(triggerIds=[601], visible=True)
        set_timer(timerId='4', seconds=4)
        show_guide_summary(entityId=20002994, textId=20002994)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            hide_guide_summary(entityId=20002994)
            return 방어모드()


class 방어모드(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_effect(triggerIds=[610], visible=True)
        set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')
        show_guide_summary(entityId=20002995, textId=20002995)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        create_monster(spawnIds=[1001,1002,1003,1004], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1001,1002,1003,1004]):
            hide_guide_summary(entityId=20002995)
            set_effect(triggerIds=[610], visible=False)
            set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 방어모드종료()


class 방어모드종료(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002996, textId=20002996)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            hide_guide_summary(entityId=20002996)
            return 시간반응대기()


class 타임머신중지(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 보스방이동준비()


class 보스방이동준비(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_effect(triggerIds=[603], visible=True)
        set_effect(triggerIds=[610], visible=True)
        show_guide_summary(entityId=20002997, textId=20002997)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_effect(triggerIds=[603], visible=True)
        set_effect(triggerIds=[605], visible=True)
        set_effect(triggerIds=[606], visible=True)
        set_effect(triggerIds=[607], visible=True)
        set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            hide_guide_summary(entityId=20002997)
            return 보스방이동()


class 보스방이동(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=4)
        set_effect(triggerIds=[603], visible=True)
        show_count_ui(text='$02000299_BF__MAIN__15$', stage=1, count=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            move_user(mapId=2000304, portalId=1)
            return 반복체크()


class 반복체크(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)
        set_effect(triggerIds=[603], visible=True)
        show_guide_summary(entityId=20002997, textId=20002997)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            hide_guide_summary(entityId=20002997)
            return 보스방이동()


class 종료(state.State):
    pass


