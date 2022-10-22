""" trigger/02010070_bf/main2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2100,2101,2102,2103,2104,2105,2106,2107,2108])
        set_interact_object(triggerIds=[10000834], state=1)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False)
        set_effect(triggerIds=[95001], visible=False)
        destroy_monster(spawnIds=[22210,22211,22212,22213])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[999993]):
            return 대기시간안내01()


class 대기시간안내01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], arg2=False)
        create_monster(spawnIds=[22210,22211,22212,22213], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대기시간02()


class 대기시간02(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02010070_BF__MAIN__4$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[999983]):
            return 시작1()


class 시작1(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20100706, textId=20100706, duration=7000) # 바니걸을 따라 이동하세요.
        move_npc(spawnId=2108, patrolName='MS2PatrolData0')
        set_conversation(type=1, spawnId=2108, script='$02010070_BF__MAIN__1$', arg4=4)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[88123]):
            return 시작112()


class 시작112(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=2108, script='$02010070_BF__MAIN__2$', arg4=4)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20100707, textId=20100707) # 테이블 위에 있는 금화를 획득하세요.

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000834], arg2=0):
            return 시작2()


class 시작2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[95001], visible=True)
        hide_guide_summary(entityId=20100707)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20100708, textId=20100708) # 욕망이 불러낸 몬스터를 모두 처치해야 합니다.
        destroy_monster(spawnIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108])
        create_monster(spawnIds=[2000,2001,2002,2003], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 시작32()


class 시작32(state.State):
    def on_enter(self):
        create_monster(spawnIds=[2004,2005], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2000,2001,2002,2003,2004,2005]):
            return 시작3()


class 시작3(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20100708)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20100709, textId=20100709) # 로비에 등장한 몬스터를 모두 처치하세요!
        create_monster(spawnIds=[2006,2007,2008], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2006,2007,2008]):
            return 시간1()


class 시간1(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20100709)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 시작5()


class 시작5(state.State):
    def on_enter(self):
        set_effect(triggerIds=[70002], visible=True)
        set_effect(triggerIds=[70003], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_effect(triggerIds=[70001], visible=True)
            set_skill(triggerIds=[70004], isEnable=True)
            return 시작6()


class 시작6(state.State):
    def on_enter(self):
        set_cinematic_ui(type=6)
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            move_user(mapId=2010070, portalId=9)
            return 시작7()


class 시작7(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시작8()


class 시작8(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=False)


