""" trigger/02000282_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000424], state=0)
        set_interact_object(triggerIds=[10000425], state=0)
        set_interact_object(triggerIds=[10000426], state=0)
        set_interact_object(triggerIds=[10000433], state=2)
        set_interact_object(triggerIds=[10000434], state=2)
        set_interact_object(triggerIds=[10000435], state=2)
        set_ladder(triggerIds=[341], visible=False, animationEffect=False)
        set_ladder(triggerIds=[342], visible=False, animationEffect=False)
        set_ladder(triggerIds=[343], visible=False, animationEffect=False)
        set_ladder(triggerIds=[351], visible=False, animationEffect=False)
        set_ladder(triggerIds=[352], visible=False, animationEffect=False)
        set_ladder(triggerIds=[353], visible=False, animationEffect=False)
        set_ladder(triggerIds=[361], visible=False, animationEffect=False)
        set_ladder(triggerIds=[362], visible=False, animationEffect=False)
        set_ladder(triggerIds=[363], visible=False, animationEffect=False)
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=5, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 준비()


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)
        create_monster(spawnIds=[1009], arg2=False)
        create_monster(spawnIds=[1010], arg2=False)
        create_monster(spawnIds=[1011], arg2=False)
        create_monster(spawnIds=[1012], arg2=False)
        create_monster(spawnIds=[1014], arg2=False)
        create_monster(spawnIds=[1015], arg2=False)
        create_monster(spawnIds=[1016], arg2=False)
        create_monster(spawnIds=[1017], arg2=False)
        create_monster(spawnIds=[1018], arg2=False)
        create_monster(spawnIds=[1019], arg2=False)
        create_monster(spawnIds=[1020], arg2=False)
        create_monster(spawnIds=[1021], arg2=False)

    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return 번생성4()
        if random_condition(rate=33):
            return 번생성5()
        if random_condition(rate=34):
            return 번생성6()


class 번생성4(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000424], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000424], arg2=0):
            return 번몬스터4()


class 번몬스터4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2004], arg2=False)
        show_guide_summary(entityId=20002817, textId=20002817, duration=5000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2004]):
            show_guide_summary(entityId=20002812, textId=20002812, duration=5000)
            play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            set_ladder(triggerIds=[341], visible=True, animationEffect=True)
            set_ladder(triggerIds=[342], visible=True, animationEffect=True)
            set_ladder(triggerIds=[343], visible=True, animationEffect=True)
            set_portal(portalId=4, visible=False, enabled=True, minimapVisible=True)
            return 소멸대기()


class 번생성5(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000425], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000425], arg2=0):
            return 번몬스터5()


class 번몬스터5(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2005], arg2=False)
        show_guide_summary(entityId=20002817, textId=20002817, duration=5000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2005]):
            play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            show_guide_summary(entityId=20002812, textId=20002812, duration=5000)
            set_ladder(triggerIds=[351], visible=True, animationEffect=True)
            set_ladder(triggerIds=[352], visible=True, animationEffect=True)
            set_ladder(triggerIds=[353], visible=True, animationEffect=True)
            set_portal(portalId=5, visible=False, enabled=True, minimapVisible=True)
            return 소멸대기()


class 번생성6(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000426], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000426], arg2=0):
            return 번몬스터6()


class 번몬스터6(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2006], arg2=False)
        show_guide_summary(entityId=20002817, textId=20002817, duration=5000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2006]):
            show_guide_summary(entityId=20002812, textId=20002812, duration=5000)
            play_system_sound_in_box(sound='System_ShowGuideSummary_01')
            set_ladder(triggerIds=[361], visible=True, animationEffect=True)
            set_ladder(triggerIds=[362], visible=True, animationEffect=True)
            set_ladder(triggerIds=[363], visible=True, animationEffect=True)
            set_portal(portalId=6, visible=False, enabled=True, minimapVisible=True)
            return 소멸대기()


class 소멸대기(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 소멸()


class 소멸(state.State):
    pass


