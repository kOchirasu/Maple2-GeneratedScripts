""" trigger/52100053_qd/04_hallwaybattle.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # InvisibleBarrier_AlwaysOn
        self.set_mesh(triggerIds=[3800,3900], visible=True, arg3=0, delay=0, scale=0)
        self.set_portal(portalId=20, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10002098], state=0) # Key
        self.destroy_monster(spawnIds=[901,902,903]) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9300]):
            # 복도 진입
            return LoadingDelay(self.ctx)


class LoadingDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[901,902,903], animationEffect=False) # Mob

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MobTrapOn01(self.ctx)


class MobTrapOn01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=901, script='$52100053_QD__04_HALLWAYBATTLE__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=902, script='$52100053_QD__04_HALLWAYBATTLE__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=903, script='$52100053_QD__04_HALLWAYBATTLE__0$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MobTrapOn02(self.ctx)


class MobTrapOn02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=5, key='MobWave', value=1)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039704, textId=20039704, duration=2000) # 가이드 : 적군이 몰려옵니다!

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MobTrapOn03(self.ctx)


class MobTrapOn03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=6, key='BlockEnable', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return GuideUseKey(self.ctx)


class GuideUseKey(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        # 가이드 : 다른 방으로 이동할 단서를 찾으세요
        self.show_guide_summary(entityId=20039705, textId=20039705)
        self.set_interact_object(triggerIds=[10002098], state=1) # Key

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002098], stateValue=0):
            return PortalOn(self.ctx)


class PortalOn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=20039705)
        self.set_portal(portalId=20, visible=True, enable=True, minimapVisible=False)


initial_state = Wait
