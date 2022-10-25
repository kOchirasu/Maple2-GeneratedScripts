""" trigger/52000125_qd/main.xml """
import common


# 노란 머리의 행방: 60100185 / 거짓말의 이유: 60100190 / 유력한 목격자: 60100195
class idle(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True) # 연출용 마크(11003205)
        self.set_sound(triggerId=7001, enable=True)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100185], questStates=[1]):
            return fadein(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60100185,60100186,60100187,60100188,60100189,60100190,60100191,60100192,60100193,60100194,60100195], questStates=[2]):
            return end(self.ctx)


# 준비
class fadein(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip(state=battle_ready, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return ready(self.ctx)


class ready(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.create_monster(spawnIds=[301], animationEffect=True) # 연출용 디나(11003214)
        self.create_monster(spawnIds=[302], animationEffect=True)
        self.create_monster(spawnIds=[303], animationEffect=True) # 연출용 디오(11003212)
        self.move_user(mapId=52000125, portalId=6002)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return start(self.ctx)


class start(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_01(self.ctx)


# 이벤트 씬 시작
class scene_01(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001,4002], returnView=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_02(self.ctx)


class scene_02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN__0$', duration=3000, align='center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_03(self.ctx)


class scene_03(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.add_cinematic_talk(npcId=11003214, msg='$52000125_QD__MAIN__1$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_04(self.ctx)


class scene_04(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003214, msg='$52000125_QD__MAIN__2$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_05(self.ctx)


class scene_05(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4008], returnView=False)
        self.add_cinematic_talk(npcId=11003213, msg='$52000125_QD__MAIN__3$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_06(self.ctx)


class scene_06(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN__4$', duration=3000, align='center')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_07(self.ctx)


class scene_07(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4010], returnView=False)
        self.add_cinematic_talk(npcId=11003212, msg='$52000125_QD__MAIN__5$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return scene_08(self.ctx)


class scene_08(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4009], returnView=False)
        self.add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN__6$', duration=3000, align='center')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return battle_ready(self.ctx)


# 전투 씬
class battle_ready(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return wait(self.ctx)


class wait(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[301,302,303]) # 연출용 마스크단
        self.create_monster(spawnIds=[601,602,603], animationEffect=False) # 몬스터 불량배
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return battle(self.ctx)


class battle(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_balloon_talk(spawnId=601, msg='$52000125_QD__MAIN__7$', duration=3000, delayTick=1000)
        self.add_balloon_talk(spawnId=602, msg='$52000125_QD__MAIN__8$', duration=3000, delayTick=3000)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return battleMsg(self.ctx)


class battleMsg(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000125_QD__MAIN__9$', arg3='3000', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[601,602,603]):
            return delay(self.ctx)


class delay(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_achievement(triggerId=2001, type='trigger', achieve='markguard')
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return winready(self.ctx)


class winready(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[601,602,603]) # 불량배
        self.create_monster(spawnIds=[304,305,306], animationEffect=True)
        self.move_user(mapId=52000125, portalId=6001)
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_scene_skip(state=end, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return endcamera(self.ctx)


class endcamera(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return bye(self.ctx)


class bye(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003214, msg='$52000125_QD__MAIN__10$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return run(self.ctx)


class run(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=304, patrolName='MS2PatrolData_3002')
        self.move_npc(spawnId=305, patrolName='MS2PatrolData_3002')
        self.move_npc(spawnId=306, patrolName='MS2PatrolData_3002')
        self.add_cinematic_talk(npcId=11003214, msg='$52000125_QD__MAIN__11$', duration=3000, align='left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return thanks(self.ctx)


class thanks(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4007], returnView=False)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Clap_A')
        self.add_cinematic_talk(npcId=11003205, msg='$52000125_QD__MAIN__12$', duration=2000, align='center')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_sound(triggerId=7001, enable=False)
        self.destroy_monster(spawnIds=[304,305,306])
        self.destroy_monster(spawnIds=[101]) # 연출용 마크(11003205)
        self.create_monster(spawnIds=[102], animationEffect=True) # 퀘스트용 마크(11003206)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)


initial_state = idle
