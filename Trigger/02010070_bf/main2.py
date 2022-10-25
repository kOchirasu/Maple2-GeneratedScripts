""" trigger/02010070_bf/main2.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2000,2001,2002,2003,2004,2005,2006,2007,2008,2100,2101,2102,2103,2104,2105,2106,2107,2108])
        self.set_interact_object(triggerIds=[10000834], state=1)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=4, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[95001], visible=False)
        self.destroy_monster(spawnIds=[22210,22211,22212,22213])

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[999993]):
            return 대기시간안내01(self.ctx)


class 대기시간안내01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], animationEffect=False)
        self.create_monster(spawnIds=[22210,22211,22212,22213], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대기시간02(self.ctx)


class 대기시간02(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02010070_BF__MAIN__4$', arg3='5000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[999983]):
            return 시작1(self.ctx)


class 시작1(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20100706, textId=20100706, duration=7000) # 바니걸을 따라 이동하세요.
        self.move_npc(spawnId=2108, patrolName='MS2PatrolData0')
        self.set_conversation(type=1, spawnId=2108, script='$02010070_BF__MAIN__1$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[88123]):
            return 시작112(self.ctx)


class 시작112(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=2108, script='$02010070_BF__MAIN__2$', arg4=4)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20100707, textId=20100707) # 테이블 위에 있는 금화를 획득하세요.

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000834], stateValue=0):
            return 시작2(self.ctx)


class 시작2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[95001], visible=True)
        self.hide_guide_summary(entityId=20100707)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20100708, textId=20100708) # 욕망이 불러낸 몬스터를 모두 처치해야 합니다.
        self.destroy_monster(spawnIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108])
        self.create_monster(spawnIds=[2000,2001,2002,2003], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=10000):
            return 시작32(self.ctx)


class 시작32(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2004,2005], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2000,2001,2002,2003,2004,2005]):
            return 시작3(self.ctx)


class 시작3(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20100708)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20100709, textId=20100709) # 로비에 등장한 몬스터를 모두 처치하세요!
        self.create_monster(spawnIds=[2006,2007,2008], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2006,2007,2008]):
            return 시간1(self.ctx)


class 시간1(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20100709)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 시작5(self.ctx)


class 시작5(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[70002], visible=True)
        self.set_effect(triggerIds=[70003], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_effect(triggerIds=[70001], visible=True)
            self.set_skill(triggerIds=[70004], enable=True)
            return 시작6(self.ctx)


class 시작6(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=6)
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.move_user(mapId=2010070, portalId=9)
            return 시작7(self.ctx)


class 시작7(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 시작8(self.ctx)


class 시작8(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=False)


initial_state = 대기
