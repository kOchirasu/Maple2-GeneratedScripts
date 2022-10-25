""" trigger/52000119_qd/main2.xml """
import common


# 골든타워 8층 : 60100030
# 랄프:11003187 / 조디:11003169 / 코쿤:11003171
# 오프닝 연출
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[60100060], questStates=[1]):
            return fadeout(self.ctx)


class fadeout(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[105,106])
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4006], returnView=False)
        self.destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        self.destroy_monster(spawnIds=[921,922,923,924,925,926,927,928,929])
        self.create_monster(spawnIds=[105,106], animationEffect=True) # 105:조디 / 106: 브로커 랄프의 수하
        self.move_user(mapId=52000119, portalId=6002)
        self.set_scene_skip(state=fadeout_01, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return fadein(self.ctx)


class fadein(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4006,4007], returnView=False)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user_path(patrolName='MS2PatrolData_3002')
        self.face_emotion(spawnId=0, emotionName='Object_React_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_01(self.ctx)


# 랄프:11003187 / 조디:11003169 / 코쿤:11003171
class scene_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4007,4008], returnView=False)
        self.set_npc_emotion_loop(spawnId=105, sequenceName='Sit_Down_A', duration=6000)
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN2__0$', duration=3000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_02(self.ctx)


class scene_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4008,4013,4014,4015], returnView=False)
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN2__1$', duration=3000, align='Left')
        self.set_conversation(type=1, spawnId=105, script='$52000119_QD__MAIN2__2$', arg4=3, arg5=0) # 조디

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_03(self.ctx)


class scene_03(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Attack_01_B')
        self.add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN2__3$', duration=3000, align='Left')
        self.set_conversation(type=1, spawnId=105, script='$52000119_QD__MAIN2__4$', arg4=3, arg5=0) # 조디

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return scene_04(self.ctx)


class scene_04(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN2__5$', duration=4989, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_05(self.ctx)


class scene_05(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN2__6$', duration=8254, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_06(self.ctx)


class scene_06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.set_npc_emotion_sequence(spawnId=106, sequenceName='Damg_B')
        self.add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__7$', duration=3000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_07(self.ctx)


class scene_07(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7001, enable=True)
        self.set_npc_emotion_sequence(spawnId=106, sequenceName='Attack_02_A')
        self.add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__8$', duration=3000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_08(self.ctx)


class scene_08(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4016], returnView=False)
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_npc_emotion_loop(spawnId=106, sequenceName='Attack_Idle_A', duration=8000)
        self.add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__9$', duration=3000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_09(self.ctx)


class scene_09(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4016,4017,4018], returnView=False)
        self.face_emotion(spawnId=0, emotionName='Object_React_A')
        self.add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__10$', duration=3000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_10(self.ctx)


class scene_10(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4018], returnView=False)
        self.set_npc_emotion_sequence(spawnId=106, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__11$', duration=3000, align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_11(self.ctx)


class scene_11(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4019], returnView=False)
        self.set_npc_emotion_sequence(spawnId=106, sequenceName='Attack_02_C')
        self.add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN2__12$', duration=3000, align='Left')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return fadeout_01(self.ctx)


class fadeout_01(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_sound(triggerId=7001, enable=False)
        self.set_sound(triggerId=7002, enable=True)
        self.set_effect(triggerIds=[5002], visible=False)
        self.destroy_monster(spawnIds=[106]) # 106: 코쿤
        self.create_monster(spawnIds=[998], animationEffect=True) # 998: 강해진 코쿤
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return fadein_01(self.ctx)


class fadein_01(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return msg(self.ctx)


class msg(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000119_QD__MAIN2__13$', arg3='3000', arg4='0')
        self.add_balloon_talk(spawnId=997, msg='$52000119_QD__MAIN2__14$', duration=2000, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[998]):
            return fadeout_02(self.ctx)


class fadeout_02(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7002, enable=False)
        self.destroy_monster(spawnIds=[998]) # 106: 코쿤
        self.set_achievement(type='trigger', achieve='jordysave2')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
