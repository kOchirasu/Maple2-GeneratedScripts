""" trigger/52000126_qd/main.xml """
import trigger_api


# 이름 없는 부랑자 (11000213) 퀘스트 / 이름 없는 부랑자(11003209) 연출
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이름 없는 부랑자 퀘스트 (11000213)
        self.create_monster(spawnIds=[101], animationEffect=True)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100210], questStates=[1]):
            return ready(self.ctx)


# 준비
class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.destroy_monster(spawnIds=[101]) # 이름 없는 부랑자 퀘스트
        self.create_monster(spawnIds=[102], animationEffect=True) # 이름 없는 부랑자 연출
        self.move_user(mapId=52000126, portalId=6002)
        self.set_scene_skip(state=battle_ready, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return talk_01(self.ctx)


# 이름 없는 부랑자 대사
class talk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003209, msg='$52000126_QD__MAIN__0$', duration=2000, align='Left')
        self.create_monster(spawnIds=[301], animationEffect=True) # 11003214
        self.create_monster(spawnIds=[302], animationEffect=True) # 11003213
        self.create_monster(spawnIds=[303], animationEffect=True) # 11003212

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_02(self.ctx)


class talk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=7001, enable=True)
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003209, msg='$52000126_QD__MAIN__1$', duration=2000, align='Left')
        self.move_npc(spawnId=301, patrolName='MS2PatrolData_3002')
        self.move_npc(spawnId=302, patrolName='MS2PatrolData_3003')
        self.move_npc(spawnId=303, patrolName='MS2PatrolData_3004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_01(self.ctx)


# 마스크단 등장씬
class scene_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.add_cinematic_talk(npcId=11003214, msg='$52000126_QD__MAIN__2$', duration=3000, align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003214, msg='$52000126_QD__MAIN__3$', duration=3000, align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.add_cinematic_talk(npcId=11003214, msg='$52000126_QD__MAIN__4$', duration=4000, align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4005,4006,4007], returnView=False)
        self.add_cinematic_talk(npcId=11003214, msg='$52000126_QD__MAIN__5$', duration=3000, align='Left')
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_effect(triggerIds=[5003], visible=True)
        self.set_effect(triggerIds=[5004], visible=True)
        self.set_onetime_effect(id=20, enable=True, path='BG/Common/Sound/Eff_Object_Explosion_Debris_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_3005')
        self.set_npc_emotion_loop(spawnId=302, sequenceName='Attack_Idle_A', duration=7000)
        self.set_npc_emotion_loop(spawnId=303, sequenceName='Attack_Idle_A', duration=7000)
        self.add_cinematic_talk(npcId=11003213, msg='$52000126_QD__MAIN__6$', duration=2000, align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Attack_01_A')
        self.add_cinematic_talk(npcId=11003214, msg='$52000126_QD__MAIN__7$', duration=3000, align='Left')
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return battle_ready(self.ctx)


# 전투 씬
class battle_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return battle(self.ctx)


class battle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[301,302,303]) # 디쓰리 엔피씨
        self.create_monster(spawnIds=[601,602,603], animationEffect=True) # 디쓰리 몬스터

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return battleMsg(self.ctx)


class battleMsg(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000126_QD__MAIN__8$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[601,602,603]):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=7001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=1)
        self.set_achievement(triggerId=2001, type='trigger', achieve='maskbattle')
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)


initial_state = idle
