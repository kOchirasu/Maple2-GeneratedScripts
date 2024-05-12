""" trigger/52010026_qd/main.xml """
import trigger_api


# 치유의 숲 : 52010026
# 들어오자마자 앉아있는 상태 연출
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=False)
        self.set_effect(triggerIds=[201], visible=False)
        self.set_effect(triggerIds=[221], visible=False)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)
        self.set_effect(triggerIds=[5101], visible=False)
        self.set_effect(triggerIds=[5201], visible=False)
        self.set_sound(triggerId=7001, enable=True)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=7, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=8, enable=False, path='BG\\Common\\ScreenMask\\Eff_FlickEye.nif')
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=201, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=202, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=301, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=997, enable=False, path='BG/sound/Eff_BossRegen_01.xml')
        self.set_onetime_effect(id=998, enable=False, path='BG/sound/Eff_DevilPortal_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2001]):
            return black(self.ctx)


class black(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52010026, portalId=6001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=True)
        self.select_camera_path(pathIds=[4001], returnView=False) # PC 정면 샷
        self.create_monster(spawnIds=[1001], animationEffect=False, animationDelay=0) # 조디
        self.create_monster(spawnIds=[601,602,603], animationEffect=False, animationDelay=0) # 연출용 엔피씨 (상인)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출시작_깨어난PC(self.ctx)


class 연출시작_깨어난PC(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=29000)
        self.face_emotion(spawnId=0, emotionName='Trigger_disappoint')
        self.set_scene_skip(state=두번째연출_ready, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출시작_PC대사01(self.ctx)


class 연출시작_PC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawnId=0, emotionName='Trigger_disappoint')
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__0$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__1$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 연출시작_조디대사01(self.ctx)


class 연출시작_조디대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4002], returnView=False)
        self.face_emotion(spawnId=1001, emotionName='Trigger_Talk_A')
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__2$', duration=3000)
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__3$', duration=3000)
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__4$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=9000):
            return 첫번째연출_PC대사02(self.ctx)


class 첫번째연출_PC대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.face_emotion(spawnId=0, emotionName='Trigger_panic')
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__5$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 첫번째연출_조디대사02(self.ctx)


class 첫번째연출_조디대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawnId=1001, emotionName='Trigger_Talk03_A')
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__7$', duration=3000)
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__8$', duration=3000)
        self.face_emotion(spawnId=1001, emotionName='Trigger_Talk02_A')
        self.add_cinematic_talk(npcId=11003344, illustId='Peach_normal', msg='$52010026_QD__MAIN__9$', duration=3000, align='Right')
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__10$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=12000):
            return 첫번째연출_PC대사03(self.ctx)


class 첫번째연출_PC대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawnId=0, emotionName='Trigger_serious')
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__11$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 첫번째연출_조디대사03(self.ctx)


class 첫번째연출_조디대사03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.face_emotion(spawnId=1001, emotionName='Trigger_Talk01_A')
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__12$', duration=3000)
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__13$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 첫번째연출_PC대사04(self.ctx)


class 첫번째연출_PC대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.face_emotion(spawnId=0, emotionName='Trigger_serious')
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__14$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 조디_카메라01(self.ctx)


class 조디_카메라01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 첫번째연출_조디대사04(self.ctx)


class 첫번째연출_조디대사04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=False)
        self.face_emotion(spawnId=1001, emotionName='Trigger_Idle02_A')
        self.set_npc_emotion_loop(spawnId=1001, sequenceName='Trigger_Idle_A', duration=10000)
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__15$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 첫번째연출_조디대사05(self.ctx)


class 첫번째연출_조디대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4003], returnView=False)
        self.set_onetime_effect(id=301, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__16$', duration=3000)
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__17$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 첫번째연출_PC대사05(self.ctx)

    def on_exit(self) -> None:
        self.visible_my_pc(isVisible=True)


class 첫번째연출_PC대사05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.face_emotion(spawnId=0, emotionName='Trigger_serious')
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__18$', duration=3000)
        self.set_npc_emotion_loop(spawnId=1001, sequenceName='Trigger_Idle_A', duration=10000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 조디_카메라02(self.ctx)


class 조디_카메라02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 첫번째연출_조디대사06(self.ctx)


class 첫번째연출_조디대사06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=True)
        self.face_emotion(spawnId=1001, emotionName='Idle_A')
        self.set_pc_emotion_loop(sequenceName='Idle_A', duration=1000)
        self.add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__19$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__20$', duration=3000)
        self.set_event_ui(type=1, arg2='$52010026_QD__MAIN__21$', arg3='8000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 두번째연출_ready(self.ctx)

    def on_exit(self) -> None:
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_sound(triggerId=7001, enable=False)
        # Missing State: State
        self.set_scene_skip()


class 두번째연출_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.visible_my_pc(isVisible=True)
        self.set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=100)
        self.reset_camera(interpolationTime=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[2101]):
            return 두번째연출_black(self.ctx)


class 두번째연출_black(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4501], returnView=False)
        self.create_monster(spawnIds=[1000], animationEffect=False, animationDelay=30000)
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_effect(triggerIds=[5002], visible=True)
        self.create_monster(spawnIds=[101], animationEffect=False, animationDelay=0)
        self.create_monster(spawnIds=[102], animationEffect=False, animationDelay=0)
        self.set_npc_emotion_loop(spawnId=1000, sequenceName='Down_Idle_A', duration=70000)
        self.set_scene_skip(state=두번째연출_피치전투01, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 두번째연출_피치발견01(self.ctx)


class 두번째연출_피치발견01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=201, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003343, msg='$52010026_QD__MAIN__22$', duration=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 두번째연출_피치발견02(self.ctx)


class 두번째연출_피치발견02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=201, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_balloon_talk(spawnId=0, msg='$52010026_QD__MAIN__47$', duration=1000, delayTick=0)
        self.select_camera_path(pathIds=[4501,4502], returnView=False)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 두번째연출_피치전투01(self.ctx)


class 두번째연출_피치전투01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_balloon_talk(spawnId=1000, msg='$52010026_QD__MAIN__24$', duration=1000, delayTick=0)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010026_QD__MAIN__25$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 두번째연출_피치전투02(self.ctx)


class 두번째연출_피치전투02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102]):
            return 두번째연출_딜레이01(self.ctx)


class 두번째연출_딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=False)
        self.add_balloon_talk(spawnId=1000, msg='$52010026_QD__MAIN__26$', duration=2000, delayTick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 두번째연출_피치전투03(self.ctx)


class 두번째연출_피치전투03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=1000, msg='$52010026_QD__MAIN__27$', duration=2000, delayTick=0)
        self.set_onetime_effect(id=202, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(triggerIds=[5003], visible=True)
        self.set_effect(triggerIds=[5004], visible=True)
        self.set_effect(triggerIds=[5005], visible=True)
        self.create_monster(spawnIds=[103], animationEffect=False, animationDelay=0)
        self.create_monster(spawnIds=[104], animationEffect=False, animationDelay=0)
        self.create_monster(spawnIds=[105], animationEffect=False, animationDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103,104,105]):
            return 두번째연출_딜레이02(self.ctx)


class 두번째연출_딜레이02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=202, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(triggerIds=[5003], visible=False)
        self.set_effect(triggerIds=[5004], visible=False)
        self.set_effect(triggerIds=[5005], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째연출_PC대사01(self.ctx)


class 두번째연출_PC대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__28$', duration=3000)
        self.set_scene_skip(state=Skip, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 두번째연출_잠시쉬기(self.ctx)


class Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=4)
        self.create_monster(spawnIds=[111], animationEffect=False, animationDelay=6000)
        self.create_monster(spawnIds=[112], animationEffect=False, animationDelay=6000)
        self.create_monster(spawnIds=[113], animationEffect=False, animationDelay=6000)
        self.create_monster(spawnIds=[114], animationEffect=False, animationDelay=6000)
        self.create_monster(spawnIds=[115], animationEffect=False, animationDelay=6000)
        self.create_monster(spawnIds=[121], animationEffect=False, animationDelay=5000)
        self.create_monster(spawnIds=[122], animationEffect=False, animationDelay=5000)
        self.create_monster(spawnIds=[123], animationEffect=False, animationDelay=5000)
        self.create_monster(spawnIds=[124], animationEffect=False, animationDelay=5000)
        self.create_monster(spawnIds=[125], animationEffect=False, animationDelay=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 세번째연출_대사01(self.ctx)


class 두번째연출_잠시쉬기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.add_cinematic_talk(npcId=11003343, illustId='Peach_normal', align='Left', msg='$52010026_QD__MAIN__29$', duration=2000)
        self.add_cinematic_talk(npcId=11003343, msg='$52010026_QD__MAIN__30$', duration=2000)
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__48$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return 세번째연출_포털개방(self.ctx)


class 세번째연출_포털개방(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4201], returnView=False)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_ambient_light(primary=[128,128,128])
        self.set_effect(triggerIds=[201], visible=True)
        self.set_onetime_effect(id=998, enable=True, path='BG/sound/Eff_DevilPortal_01.xml')
        self.create_monster(spawnIds=[111], animationEffect=False, animationDelay=6000)
        self.create_monster(spawnIds=[112], animationEffect=False, animationDelay=6000)
        self.create_monster(spawnIds=[113], animationEffect=False, animationDelay=6000)
        self.create_monster(spawnIds=[114], animationEffect=False, animationDelay=6000)
        self.create_monster(spawnIds=[115], animationEffect=False, animationDelay=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세번째연출_포털개방02(self.ctx)


class 세번째연출_포털개방02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4301], returnView=False)
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_effect(triggerIds=[211], visible=True)
        self.create_monster(spawnIds=[121], animationEffect=False, animationDelay=5000)
        self.create_monster(spawnIds=[122], animationEffect=False, animationDelay=5000)
        self.create_monster(spawnIds=[123], animationEffect=False, animationDelay=5000)
        self.create_monster(spawnIds=[124], animationEffect=False, animationDelay=5000)
        self.create_monster(spawnIds=[125], animationEffect=False, animationDelay=5000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 세번째연출_대사01(self.ctx)


class 세번째연출_대사01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_balloon_talk(spawnId=0, msg='$52010026_QD__MAIN__32$', duration=2000, delayTick=0)
        self.set_npc_emotion_sequence(spawnId=1000, sequenceName='ChatUP_A')
        self.add_balloon_talk(spawnId=1000, msg='$52010026_QD__MAIN__33$', duration=2000, delayTick=2000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010026_QD__MAIN__34$', arg3='2000', arg4='4000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 피치탈출(self.ctx)


class 피치탈출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=1000, patrolName='MS2PatrolData_3002')
        self.add_balloon_talk(spawnId=1000, msg='$52010026_QD__MAIN__42$', duration=2000, delayTick=0)
        self.add_buff(boxIds=[2101], skillId=70000123, level=1, isPlayer=False, isSkillSet=False)
        self.set_effect(triggerIds=[5101], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[111,112,113,114,115,121,122,123,124,125]):
            return 세번째연출_대사02(self.ctx)


class 세번째연출_대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[201], visible=False)
        self.set_effect(triggerIds=[221], visible=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=998, enable=False, path='BG/sound/Eff_DevilPortal_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 세번째연출_대사02_1(self.ctx)


class 세번째연출_대사02_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=skip_a, action='nextState')
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__35$', duration=2000)
        self.add_cinematic_talk(npcId=11003343, msg='$52010026_QD__MAIN__36$', duration=2000)
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__49$', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 다섯번째연출_ready(self.ctx)


class 다섯번째연출_ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[4402], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 다섯번째연출_엘리트몬스터(self.ctx)


class skip_a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_scene_skip()
        self.create_monster(spawnIds=[131], animationEffect=True, animationDelay=0)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 다섯번째연출_엘리트몬스터대사(self.ctx)


class 다섯번째연출_엘리트몬스터(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=1000, sequenceName='Trigger_Hurt_A', duration=28000)
        self.select_camera_path(pathIds=[4401], returnView=False)
        self.set_onetime_effect(id=7, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.move_user(mapId=52010026, portalId=6002)
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=997, enable=True, path='BG/sound/Eff_BossRegen_01.xml')
        self.create_monster(spawnIds=[131], animationEffect=True, animationDelay=0)
        self.show_caption(scale=2.3, type='NameCaption', title='$52010026_QD__MAIN__50$', desc='$52010026_QD__MAIN__51$', align='centerLeft', offsetRateX=-0.15, duration=4000)
        self.set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 다섯번째연출_엘리트몬스터대사(self.ctx)


class 다섯번째연출_엘리트몬스터대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=7, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52010026_QD__MAIN__38$', arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 다섯번째연출_전투(self.ctx)


class 다섯번째연출_전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_onetime_effect(id=997, enable=False, path='BG/sound/Eff_BossRegen_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[131]):
            return 다섯번째연출_마지막(self.ctx)


class 다섯번째연출_마지막(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip(state=Warp, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 다섯번째연출_대화02(self.ctx)


class 다섯번째연출_대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.face_emotion(spawnId=0, emotionName='Trigger_disappoint')
        self.set_pc_emotion_loop(sequenceName='Down_B', duration=18000)
        self.set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_effect(triggerIds=[5201], visible=True)
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__43$', duration=3000)
        self.add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__44$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return 다섯번째연출_암전(self.ctx)


class 다섯번째연출_암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 다섯번째연출_의문의목소리암전(self.ctx)


class 다섯번째연출_의문의목소리암전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npcId=11003145, msg='$52010026_QD__MAIN__45$', duration=3000)
        self.add_cinematic_talk(npcId=11003145, msg='$52010026_QD__MAIN__46$', duration=3000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=8000):
            return Warp(self.ctx)


class Warp(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=63000042, portalId=10)


initial_state = idle
