""" trigger/02000299_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1010,1011,1012,1013], animationEffect=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        self.set_interact_object(triggerIds=[10000494,10000495,10000496,10000497,10000498,10000499], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[104]):
            return 클리어체크(self.ctx)


class 클리어체크(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False) # Eff_dungeon_allert_01
        self.set_effect(triggerIds=[602], visible=False) # Eff_Sound_Dungeon_Object_Scifi_Door_Open
        self.set_effect(triggerIds=[603], visible=False) # Eff_Sound_Dungeon_Object_Scifi_Door_Open
        self.set_effect(triggerIds=[604], visible=False) # Eff_UI_Sound_notice_01
        self.set_effect(triggerIds=[605], visible=False) # Eff_sf_fi_prop_incubator_B02_wfx_Big
        self.set_effect(triggerIds=[606], visible=False) # Eff_electricity
        self.set_effect(triggerIds=[607], visible=False) # Eff_electricity
        self.set_effect(triggerIds=[610], visible=False) # Eff_Sound_RedAllert

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 클리어체크2(self.ctx)


class 클리어체크2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=False, arg3=0, delay=0, scale=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1010]):
            return 타임머신중지(self.ctx)
        if self.monster_dead(boxIds=[1011]):
            return 타임머신중지(self.ctx)
        if self.monster_dead(boxIds=[1012]):
            return 타임머신중지(self.ctx)
        if self.monster_dead(boxIds=[1013]):
            return 타임머신중지(self.ctx)
        if self.wait_tick(waitTick=100):
            return 정황설명(self.ctx)


class 정황설명(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20002990, textId=20002990, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 시간반응대기(self.ctx)


class 시간반응대기(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20002992, textId=20002992, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(triggerIds=[10000494,10000495], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000494], stateValue=0):
            return 미래시간(self.ctx)
        if self.object_interacted(interactIds=[10000495], stateValue=0):
            return 과거시간(self.ctx)


class 미래시간(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[606], visible=True)
        self.set_effect(triggerIds=[604], visible=True)
        self.show_guide_summary(entityId=20002987, textId=20002987)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(triggerIds=[10000495], state=0)
        self.set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000496], stateValue=0):
            return 그런거없음(self.ctx)
        if self.object_interacted(interactIds=[10000497], stateValue=0):
            return 미래엘리니아(self.ctx)
        if self.object_interacted(interactIds=[10000498], stateValue=0):
            return 그런거없음(self.ctx)
        if self.object_interacted(interactIds=[10000499], stateValue=0):
            return 미래커닝시티(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20002987)
        self.set_effect(triggerIds=[607], visible=True)
        self.set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=0)


class 과거시간(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[606], visible=True)
        self.set_effect(triggerIds=[604], visible=True)
        self.show_guide_summary(entityId=20002988, textId=20002988)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_interact_object(triggerIds=[10000494], state=0)
        self.set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000496], stateValue=0):
            return 과거헤네니스(self.ctx)
        if self.object_interacted(interactIds=[10000497], stateValue=0):
            return 그런거없음(self.ctx)
        if self.object_interacted(interactIds=[10000498], stateValue=0):
            return 과거페리온(self.ctx)
        if self.object_interacted(interactIds=[10000499], stateValue=0):
            return 그런거없음(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=20002988)
        self.set_effect(triggerIds=[607], visible=True)
        self.set_interact_object(triggerIds=[10000496,10000497,10000498,10000499], state=0)


class 미래엘리니아(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[604], visible=True)
        self.show_guide_summary(entityId=20002989, textId=20002989)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.hide_guide_summary(entityId=20002989)
            return 미래엘리니아2(self.ctx)


class 미래엘리니아2(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000299, portalId=2, boxId=104)
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_effect(triggerIds=[604], visible=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='Opened_A')
        self.show_count_ui(text='$02000299_BF__MAIN__3$', stage=1, count=3)
        self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 미래엘리니아이동(self.ctx)


class 미래엘리니아이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_effect(triggerIds=[603], visible=True)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        self.set_effect(triggerIds=[605], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.move_user(mapId=2000302, portalId=1, boxId=104)
            self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 클리어체크(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[1010])
        self.set_effect(triggerIds=[603], visible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=True, arg3=0, delay=0, scale=5)


class 미래커닝시티(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[604], visible=True)
        self.show_guide_summary(entityId=20002989, textId=20002989)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.hide_guide_summary(entityId=20002989)
            return 미래커닝시티2(self.ctx)


class 미래커닝시티2(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000299, portalId=2, boxId=104)
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='Opened_A')
        self.set_effect(triggerIds=[604], visible=True)
        self.show_count_ui(text='$02000299_BF__MAIN__5$', stage=1, count=3)
        self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 미래커닝시티이동(self.ctx)


class 미래커닝시티이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_effect(triggerIds=[603], visible=True)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        self.set_effect(triggerIds=[605], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.move_user(mapId=2000301, portalId=1, boxId=104)
            self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 클리어체크(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[1011])
        self.set_effect(triggerIds=[603], visible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=True, arg3=0, delay=0, scale=5)


class 과거헤네니스(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[604], visible=True)
        self.show_guide_summary(entityId=20002989, textId=20002989)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.hide_guide_summary(entityId=20002989)
            return 과거헤네니스2(self.ctx)


class 과거헤네니스2(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000299, portalId=2, boxId=104)
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='Opened_A')
        self.set_effect(triggerIds=[604], visible=True)
        self.show_count_ui(text='$02000299_BF__MAIN__7$', stage=1, count=3)
        self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 과거헤네니스이동(self.ctx)


class 과거헤네니스이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_effect(triggerIds=[603], visible=True)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        self.set_effect(triggerIds=[605], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.move_user(mapId=2000303, portalId=1, boxId=104)
            self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 클리어체크(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[1012])
        self.set_effect(triggerIds=[603], visible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=True, arg3=0, delay=0, scale=5)


class 과거페리온(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[604], visible=True)
        self.show_guide_summary(entityId=20002989, textId=20002989)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.hide_guide_summary(entityId=20002989)
            return 과거페리온2(self.ctx)


class 과거페리온2(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000299, portalId=2, boxId=104)
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='Opened_A')
        self.set_effect(triggerIds=[604], visible=True)
        self.show_count_ui(text='$02000299_BF__MAIN__9$', stage=1, count=3)
        self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 과거페리온이동(self.ctx)


class 과거페리온이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=2)
        self.set_effect(triggerIds=[603], visible=True)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        self.set_effect(triggerIds=[605], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.move_user(mapId=2000300, portalId=1, boxId=104)
            self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 클리어체크(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[1013])
        self.set_effect(triggerIds=[603], visible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=True, arg3=0, delay=0, scale=5)


class 그런거없음(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=3)
        self.set_effect(triggerIds=[604], visible=True)
        self.show_guide_summary(entityId=20002989, textId=20002989)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            self.hide_guide_summary(entityId=20002989)
            return 그런거없음2(self.ctx)


class 그런거없음2(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[606], visible=False)
        self.set_effect(triggerIds=[607], visible=False)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_timer(timerId='4', seconds=4)
        self.show_guide_summary(entityId=20002994, textId=20002994)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            self.hide_guide_summary(entityId=20002994)
            return 방어모드(self.ctx)


class 방어모드(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=True)
        self.set_effect(triggerIds=[610], visible=True)
        self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')
        self.show_guide_summary(entityId=20002995, textId=20002995)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.create_monster(spawnIds=[1001,1002,1003,1004], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[1001,1002,1003,1004]):
            self.hide_guide_summary(entityId=20002995)
            self.set_effect(triggerIds=[610], visible=False)
            self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_Off')
            self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_Off')
            return 방어모드종료(self.ctx)


class 방어모드종료(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20002996, textId=20002996)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            self.hide_guide_summary(entityId=20002996)
            return 시간반응대기(self.ctx)


class 타임머신중지(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[104]):
            return 보스방이동준비(self.ctx)


class 보스방이동준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_effect(triggerIds=[603], visible=True)
        self.set_effect(triggerIds=[610], visible=True)
        self.show_guide_summary(entityId=20002997, textId=20002997)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_effect(triggerIds=[603], visible=True)
        self.set_effect(triggerIds=[605], visible=True)
        self.set_effect(triggerIds=[606], visible=True)
        self.set_effect(triggerIds=[607], visible=True)
        self.set_actor(triggerId=290, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=291, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=292, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=293, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=294, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=295, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=296, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=297, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=298, visible=True, initialSequence='sf_quest_light_A01_On')
        self.set_actor(triggerId=299, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.hide_guide_summary(entityId=20002997)
            return 보스방이동(self.ctx)


class 보스방이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='4', seconds=4)
        self.set_effect(triggerIds=[603], visible=True)
        self.show_count_ui(text='$02000299_BF__MAIN__15$', stage=1, count=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            self.move_user(mapId=2000304, portalId=1)
            return 반복체크(self.ctx)


class 반복체크(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='5', seconds=5)
        self.set_effect(triggerIds=[603], visible=True)
        self.show_guide_summary(entityId=20002997, textId=20002997)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            self.hide_guide_summary(entityId=20002997)
            return 보스방이동(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
