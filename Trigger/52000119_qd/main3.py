""" trigger/52000119_qd/main3.xml """
import common


# 골든타워 8층 : 60100030
# 랄프:11003187 / 조디:11003169 / 코쿤:11003171
# 오프닝 연출
class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100070], questStates=[2]):
            return monsterdel(self.ctx)
        if self.quest_user_detected(boxIds=[2002], questIds=[60100075], questStates=[1]):
            return fadeout(self.ctx)


class fadeout(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4020], returnView=False)
        self.destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        self.destroy_monster(spawnIds=[921,922,923,924,925,926,927,928,929])
        self.create_monster(spawnIds=[106], animationEffect=True)
        self.create_monster(spawnIds=[201,202], animationEffect=True)
        self.create_monster(spawnIds=[301,302,303,304,305,306], animationEffect=True)
        self.move_user(mapId=52000119, portalId=6001)
        self.set_scene_skip(state=fadeout_01, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return fadein(self.ctx)


class fadein(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=6000)
        self.face_emotion(spawnId=0, emotionName='Object_React_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_01(self.ctx)


# 랄프:11003187 / 조디:11003169 / 코쿤:11003171
class scene_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4021], returnView=False)
        self.set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003169, illustId='Jordy_normal', msg='$52000119_QD__MAIN3__0$', duration=3000, align='Right')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_02(self.ctx)


class scene_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN3__1$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03(self.ctx)


class scene_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4013,4014,4015], returnView=False)
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN3__2$', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_04(self.ctx)


class scene_04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003187, msg='$52000119_QD__MAIN3__3$', duration=3000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return cheer_01(self.ctx)


# 응원 씬
class cheer_01(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7001, enable=True)
        self.select_camera_path(pathIds=[4023,4024], returnView=False)
        self.add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__4$', duration=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return cheer_02(self.ctx)


class cheer_02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=306, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__5$', duration=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return cheer_03(self.ctx)


class cheer_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4024,4025], returnView=False)
        self.add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__6$', duration=2000)
        self.add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__7$', duration=1000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return cheer_04(self.ctx)


class cheer_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__8$', duration=2000)
        self.add_balloon_talk(spawnId=303, msg='$52000119_QD__MAIN3__9$', duration=2000, delayTick=1)
        self.add_cinematic_talk(npcId=11003354, msg='$52000119_QD__MAIN3__10$', duration=1000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_05(self.ctx)


# 응원 씬 종료
class scene_05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.set_npc_emotion_sequence(spawnId=106, sequenceName='Stun_A')
        self.add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN3__11$', duration=2000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_06(self.ctx)


class scene_06(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4019], returnView=False)
        self.set_effect(triggerIds=[5002], visible=True)
        self.set_effect(triggerIds=[5003], visible=True)
        self.set_effect(triggerIds=[5004], visible=True)
        self.set_effect(triggerIds=[5005], visible=True)
        self.set_npc_emotion_sequence(spawnId=106, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003171, msg='$52000119_QD__MAIN3__12$', duration=4000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_07(self.ctx)


class scene_07(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4019,4022], returnView=False)
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_3001')
        self.set_conversation(type=2, spawnId=11003171, script='$52000119_QD__MAIN3__13$', arg4=3, arg5=0) # 코쿤
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return fadeout_01(self.ctx)


class fadeout_01(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7001, enable=False)
        self.set_sound(triggerId=7002, enable=True)
        self.destroy_monster(spawnIds=[106]) # 106: 코쿤
        self.create_monster(spawnIds=[999], animationEffect=True) # 998: 강해진 코쿤
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=100)

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
        self.set_event_ui(type=1, arg2='$52000119_QD__MAIN3__14$', arg3='3000', arg4='0')
        self.add_balloon_talk(spawnId=999, msg='$52000119_QD__MAIN3__15$', duration=2000, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[999]):
            return fadeout_02(self.ctx)


class fadeout_02(common.Trigger):
    def on_enter(self):
        self.set_sound(triggerId=7002, enable=False)
        self.add_balloon_talk(spawnId=999, msg='$52000119_QD__MAIN3__19$', duration=2000, delayTick=0)
        self.add_balloon_talk(spawnId=306, msg='$52000119_QD__MAIN3__20$', duration=2000, delayTick=1)
        self.destroy_monster(spawnIds=[201,202])
        self.destroy_monster(spawnIds=[401,402,403,404,405,406,407])
        self.set_achievement(type='trigger', achieve='jordysave3')
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


# 진입 시
class monsterdel(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920])
        self.destroy_monster(spawnIds=[921,922,923,924,925,926,927,928,929])
        self.create_monster(spawnIds=[401,402,403,404,405,406,407], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2002], questIds=[60100075], questStates=[1]):
            return ready(self.ctx)


initial_state = idle
