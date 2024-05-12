""" trigger/52010027_qd/main_quest10003102.xml """
import trigger_api


# 바람의 골짜기 : 52010027
# 중간 보스 사라짐
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003102], questStates=[1]):
            return Del(self.ctx)


class Del(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return Ready(self.ctx)


class Ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52010027, portalId=6007)
        self.create_monster(spawnIds=[803], animationEffect=True)
        self.set_npc_emotion_loop(spawnId=803, sequenceName='Stun_A', duration=160000000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 엔피씨와말을걸면(self.ctx)


class 엔피씨와말을걸면(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4013], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 보스몬스터는소멸준비(self.ctx)


class 보스몬스터는소멸준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=완료조건, action='exit')
        self.add_cinematic_talk(npcId=11003469, msg='$52010027_QD__MAIN_QUEST10003102__0$', duration=4000)
        self.add_cinematic_talk(npcId=11003469, msg='$52010027_QD__MAIN_QUEST10003102__1$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 보스몬스터는소멸준비01(self.ctx)


class 보스몬스터는소멸준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4014], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003102__2$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003102__3$', duration=3000)
        self.set_pc_emotion_loop(sequenceName='Talk_A', duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 보스몬스터는소멸준비02(self.ctx)


class 보스몬스터는소멸준비02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4013], returnView=False)
        self.add_cinematic_talk(npcId=11003469, msg='$52010027_QD__MAIN_QUEST10003102__4$', duration=4000)
        self.add_cinematic_talk(npcId=11003469, msg='$52010027_QD__MAIN_QUEST10003102__5$', duration=3000)
        self.add_cinematic_talk(npcId=11003469, msg='$52010027_QD__MAIN_QUEST10003102__6$', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=11000):
            return 보스몬스터는소멸(self.ctx)


class 보스몬스터는소멸(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 보스몬스터는소멸_01(self.ctx)


class 보스몬스터는소멸_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[803])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투종료(self.ctx)


class 전투종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4014], returnView=False)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003102__7$', duration=2000)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003102__8$', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003102__9$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 전투종료01(self.ctx)


class 전투종료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투종료02(self.ctx)


class 전투종료02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 완료조건(self.ctx)


class 완료조건(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(triggerId=2001, type='trigger', achieve='WindValleyBattle')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=2000051, portalId=3)


initial_state = idle
