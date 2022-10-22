""" trigger/02000483_bf/04_hallwaybattle.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3800,3900], visible=True, arg3=0, arg4=0, arg5=0) # InvisibleBarrier_AlwaysOn
        set_portal(portalId=20, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10002045], state=0) # Key
        destroy_monster(spawnIds=[901,902,903]) # Mob

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9300]):
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[901,902,903], arg2=False) # Mob

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MobTrapOn01()


class MobTrapOn01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=901, script='$02000483_BF__04_HALLWAYBATTLE__0$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=902, script='$02000483_BF__04_HALLWAYBATTLE__1$', arg4=2, arg5=0)
        set_conversation(type=1, spawnId=903, script='$02000483_BF__04_HALLWAYBATTLE__2$', arg4=2, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MobTrapOn02()


class MobTrapOn02(state.State):
    def on_enter(self):
        set_user_value(triggerId=5, key='MobWave', value=1)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039704, textId=20039704, duration=2000) # 가이드 : 적군이 몰려옵니다!

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MobTrapOn03()


class MobTrapOn03(state.State):
    def on_enter(self):
        set_user_value(triggerId=6, key='BlockEnable', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GuideUseKey()


class GuideUseKey(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039705, textId=20039705) # 가이드 : 다른 방으로 이동할 단서를 찾으세요
        set_interact_object(triggerIds=[10002045], state=1) # Key

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002045], arg2=0):
            return PortalOn()


class PortalOn(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20039705)
        set_portal(portalId=20, visible=True, enabled=True, minimapVisible=False)


