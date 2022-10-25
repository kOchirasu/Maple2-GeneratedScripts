""" trigger/52010027_qd/main_quest10003101.xml """
import common


# 바람의 골짜기 : 52010027
# 중간 보스 빌런과 전투 벌이는 씬
class idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5005], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003101], questStates=[1]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52010027, portalId=6005)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 집에서나옴(self.ctx)


class 집에서나옴(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4011], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3006')
        self.create_monster(spawnIds=[801], animationEffect=True)
        self.add_balloon_talk(spawnId=0, msg='$52010027_QD__MAIN_QUEST10003101__0$', duration=3000, delayTick=500)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 집에서나와서대사침(self.ctx)


class 집에서나와서대사침(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Suprise_A'])
        self.add_balloon_talk(spawnId=0, msg='$52010027_QD__MAIN_QUEST10003101__1$', duration=2000, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 집에나와서대사침01(self.ctx)


class 집에나와서대사침01(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=10000)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003101__2$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 집에나와서대사침02(self.ctx)


class 집에나와서대사침02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4012], returnView=False)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__3$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 집에나와서대사침03(self.ctx)


class 집에나와서대사침03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4011], returnView=False)
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=10000)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003101__4$', duration=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 집에나와서대사침04(self.ctx)


class 집에나와서대사침04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4012], returnView=False)
        self.move_npc(spawnId=801, patrolName='MS2PatrolData_3005')
        self.set_effect(triggerIds=[5005], visible=True)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__5$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003101__6$', duration=3000)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__7$', duration=3000)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__8$', duration=4000)
        self.add_cinematic_talk(npcId=0, msg='$52010027_QD__MAIN_QUEST10003101__9$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=16000):
            return 집에나와서대사침05(self.ctx)


class 집에나와서대사침05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=801, sequenceName='Attack_01_G')
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__10$', duration=3000)
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__11$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return 전투시작01(self.ctx)


class 전투시작01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52010027, portalId=6006)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투시작01_1(self.ctx)


class 전투시작01_1(common.Trigger):
    def on_enter(self):
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투시작02(self.ctx)


class Skip_1(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52010027, portalId=6006)
        self.create_monster(spawnIds=[801], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투시작02(self.ctx)


class 전투시작02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[801])
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 전투시작03(self.ctx)


class 전투시작03(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[802], animationEffect=True)
        self.set_event_ui(type=1, arg2='$52010027_QD__MAIN_QUEST10003101__12$', arg3='3000', arg4='0')
        self.add_balloon_talk(spawnId=802, msg='$52010027_QD__MAIN_QUEST10003101__13$', duration=3000, delayTick=5000)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[802]):
            return 전투종료01(self.ctx)


class 전투종료01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52010027, portalId=6007)
        self.destroy_monster(spawnIds=[802])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 전투종료02(self.ctx)


class 전투종료02(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003431, msg='$52010027_QD__MAIN_QUEST10003101__14$', duration=3000)
        self.set_npc_emotion_loop(spawnId=803, sequenceName='Stun_A', duration=160000000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 전투종료03(self.ctx)


class 전투종료03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: 


initial_state = idle
