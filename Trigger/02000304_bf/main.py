""" trigger/02000304_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=201, visible=False, initialSequence='Closed_A')
        self.set_actor(triggerId=202, visible=False, initialSequence='Closed_A')
        self.set_actor(triggerId=203, visible=True, initialSequence='sf_functobj_monitor_C01_On')
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_portal(portalId=98, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=99, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10000646], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            self.create_monster(spawnIds=[2001], animationEffect=False)
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 카메라이동대기(self.ctx)


class 카메라이동대기(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4500):
            return 전투시작대기(self.ctx)


class 전투시작대기(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20003041, textId=20003041, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=301, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[2001]):
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=2001, script='$02000304_BF__MAIN__1$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2001]):
            self.set_actor(triggerId=203, visible=False, initialSequence='sf_functobj_monitor_C01_On')
            self.set_interact_object(triggerIds=[10000646], state=1)
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[603], visible=True)
        self.show_guide_summary(entityId=20003003, textId=20003003)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000646], stateValue=0):
            self.hide_guide_summary(entityId=20003003)
            self.set_effect(triggerIds=[603], visible=False)
            self.set_effect(triggerIds=[602], visible=True)
            self.set_achievement(triggerId=999, type='trigger', achieve='ClearTimehole')
            return 미션성공(self.ctx)


class 미션성공(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_clear()
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=201, visible=True, initialSequence='Closed_A')
        self.set_actor(triggerId=202, visible=True, initialSequence='Closed_A')
        self.set_portal(portalId=99, visible=False, enable=True, minimapVisible=True)
        self.set_portal(portalId=98, visible=False, enable=True, minimapVisible=True)
        self.set_timer(timerId='5', seconds=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 종료2(self.ctx)


class 종료2(trigger_api.Trigger):
    pass


initial_state = 대기
