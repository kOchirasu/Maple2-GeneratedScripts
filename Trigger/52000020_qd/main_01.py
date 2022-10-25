""" trigger/52000020_qd/main_01.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True) # 퀘스트용 리퍼트(11001262)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100090], questStates=[2]):
            return ready(self.ctx)


# 준비
class ready(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7001, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202], animationEffect=True) # 연출용 리퍼트 (11003193)
        self.create_monster(spawnIds=[301], animationEffect=True)
        self.create_monster(spawnIds=[401,402,403], animationEffect=True) # 연출용 흑성회
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_scene_skip(state=battle_ready, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return camera(self.ctx)


class camera(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=4001, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return start(self.ctx)


class start(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_01(self.ctx)


# 이벤트 씬 시작
class scene_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001,4002], returnView=False)
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Bore_C')
        self.add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_01__0$', duration=3709, align='center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_02(self.ctx)


class scene_02(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003193, msg='$52000020_QD__MAIN_01__1$', duration=3369, align='center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03(self.ctx)


class scene_03(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003193, msg='$52000020_QD__MAIN_01__2$', duration=2000, align='center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_04(self.ctx)


class scene_04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Emotion_Troubled_A')
        self.add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_01__3$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_05(self.ctx)


class scene_05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Bore_B')
        self.add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_01__4$', duration=2000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_06(self.ctx)


class scene_06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.add_balloon_talk(spawnId=401, msg='$52000020_QD__MAIN_01__5$', duration=1000, delayTick=0)
        self.add_balloon_talk(spawnId=402, msg='$52000020_QD__MAIN_01__6$', duration=1000, delayTick=0)
        self.add_balloon_talk(spawnId=403, msg='$52000020_QD__MAIN_01__7$', duration=1000, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_07(self.ctx)


class scene_07(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=301, sequenceName='Emotion_Angry_A')
        self.add_cinematic_talk(npcId=29000266, msg='$52000020_QD__MAIN_01__8$', duration=2000, align='left')
        self.add_balloon_talk(spawnId=202, msg='$52000020_QD__MAIN_01__9$', duration=2000, delayTick=1000)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return battle_ready(self.ctx)


# 전투 씬
class battle_ready(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7001, enable=False)
        self.set_sound(triggerId=7002, enable=True)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.destroy_monster(spawnIds=[301]) # 연출용 흑성회 대장(11001262)
        self.destroy_monster(spawnIds=[401,402,403]) # 연출용 흑성회

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return battle(self.ctx)


class battle(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.reset_camera(interpolationTime=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.create_monster(spawnIds=[501], animationEffect=True) # 몬스터 흑성회 대장
        self.create_monster(spawnIds=[601,602,603], animationEffect=True) # 몬스터 흑성회

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return battleMsg(self.ctx)


class battleMsg(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000020_QD__MAIN_01__10$', arg3='3000', arg4='0')
        self.add_balloon_talk(spawnId=601, msg='$52000020_QD__MAIN_01__11$', duration=3000, delayTick=2)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[501,601,602,603]):
            return delay(self.ctx)


class delay(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7002, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return winready(self.ctx)


class winready(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202]) # 연출용 리퍼트
        self.destroy_monster(spawnIds=[501]) # 흑성회 대장
        self.destroy_monster(spawnIds=[601,602,603]) # 흑성회
        self.create_monster(spawnIds=[201], animationEffect=True) # 퀘스트용 리퍼트(11001262)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return end(self.ctx)


class end(common.Trigger):
    pass


initial_state = idle
