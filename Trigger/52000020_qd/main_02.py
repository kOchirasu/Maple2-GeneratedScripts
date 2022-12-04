""" trigger/52000020_qd/main_02.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[60100095], questStates=[1]):
            return ready(self.ctx)


# 준비
class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7001, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202], animationEffect=True) # 연출용 리퍼트 (11003193)
        self.create_monster(spawnIds=[302], animationEffect=True) # 연출용 흑성회 행동대장
        self.create_monster(spawnIds=[404,405,406,407,408,409,410,411], animationEffect=True) # 연출용 흑성회
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_scene_skip(state=battle_ready, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return camera(self.ctx)


class camera(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=4001, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_01(self.ctx)


# 이벤트 씬 시작
class scene_01(trigger_api.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7001, enable=False)
        self.set_sound(triggerId=7002, enable=True)
        self.add_cinematic_talk(npcId=11003193, msg='$52000020_QD__MAIN_02__0$', duration=2000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4003,4004], returnView=False)
        self.move_user(mapId=52000020, portalId=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=302, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_02__1$', duration=2000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=302, sequenceName='Emotion_Angry_A')
        self.add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_02__2$', duration=2000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=302, sequenceName='ChatUp_A')
        self.add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_02__3$', duration=2000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4006], returnView=False)
        self.set_npc_emotion_sequence(spawnId=404, sequenceName='ChatUp_A')
        self.set_npc_emotion_sequence(spawnId=405, sequenceName='ChatUp_A')
        self.set_npc_emotion_sequence(spawnId=406, sequenceName='ChatUp_A')
        self.set_npc_emotion_sequence(spawnId=407, sequenceName='ChatUp_A')
        self.set_npc_emotion_sequence(spawnId=408, sequenceName='ChatUp_A')
        self.set_npc_emotion_sequence(spawnId=409, sequenceName='ChatUp_A')
        self.set_npc_emotion_sequence(spawnId=410, sequenceName='ChatUp_A')
        self.set_npc_emotion_sequence(spawnId=411, sequenceName='ChatUp_A')
        self.add_balloon_talk(spawnId=404, msg='$52000020_QD__MAIN_02__4$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=405, msg='$52000020_QD__MAIN_02__5$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=406, msg='$52000020_QD__MAIN_02__6$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=407, msg='$52000020_QD__MAIN_02__7$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=408, msg='$52000020_QD__MAIN_02__8$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=409, msg='$52000020_QD__MAIN_02__9$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=410, msg='$52000020_QD__MAIN_02__10$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=411, msg='$52000020_QD__MAIN_02__11$', duration=2000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_07(self.ctx)


class scene_07(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=502, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_02__12$', duration=2000, align='center')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return battle_ready(self.ctx)


# Round_1 전투 씬
class battle_ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[404,405]) # 연출용 흑성회
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return battle(self.ctx)


class battle(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.create_monster(spawnIds=[604,605], animationEffect=True) # 몬스터 흑성회

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return battleMsg(self.ctx)


class battleMsg(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000020_QD__MAIN_02__13$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[604,605]):
            return delay(self.ctx)


class delay(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return round_2(self.ctx)


class round_2(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[406,407,408,409]) # 연출용 흑성회
        self.create_monster(spawnIds=[606,607,608,609], animationEffect=True) # 몬스터 흑성회

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[604,605]):
            return delay_a(self.ctx)


class delay_a(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return round_3(self.ctx)


class round_3(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[410,411,302]) # 연출용 흑성회
        self.create_monster(spawnIds=[610,611,502], animationEffect=True) # 몬스터 흑성회

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[610,611,502]):
            return delay_b(self.ctx)


class delay_b(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=2002, type='trigger', achieve='mafiabattle')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return winready(self.ctx)


class winready(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202]) # 연출용 리퍼트
        self.create_monster(spawnIds=[201], animationEffect=True) # 퀘스트용 리퍼트(11001262)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_sound(triggerId=7002, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    pass


initial_state = idle
