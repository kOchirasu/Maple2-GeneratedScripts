""" trigger/52010026_qd/main.xml """
from common import *
import state


#  치유의 숲 : 52010026  
#  들어오자마자 앉아있는 상태 연출 
class idle(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False)
        set_effect(triggerIds=[201], visible=False)
        set_effect(triggerIds=[221], visible=False)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)
        set_effect(triggerIds=[5101], visible=False)
        set_effect(triggerIds=[5201], visible=False)
        set_sound(triggerId=7001, arg2=True)
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=7, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=8, enable=False, path='BG\Common\ScreenMask\Eff_FlickEye.nif')
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=201, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=202, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=301, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=997, enable=False, path='BG/sound/Eff_BossRegen_01.xml')
        set_onetime_effect(id=998, enable=False, path='BG/sound/Eff_DevilPortal_01.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001]):
            return black()


class black(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52010026, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ready()


class ready(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        select_camera_path(pathIds=[4001], returnView=False) # PC 정면 샷
        create_monster(spawnIds=[1001], arg2=False, arg3=0) # 조디
        create_monster(spawnIds=[601,602,603], arg2=False, arg3=0) # 연출용 엔피씨 (상인)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작_깨어난PC()


class 연출시작_깨어난PC(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=29000)
        face_emotion(spawnId=0, emotionName='Trigger_disappoint')
        set_scene_skip(state=두번째연출_ready, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작_PC대사01()


class 연출시작_PC대사01(state.State):
    def on_enter(self):
        face_emotion(spawnId=0, emotionName='Trigger_disappoint')
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__0$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__1$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 연출시작_조디대사01()


class 연출시작_조디대사01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)
        face_emotion(spawnId=1001, emotionName='Trigger_Talk_A')
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__2$', duration=3000)
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__3$', duration=3000)
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__4$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 첫번째연출_PC대사02()


class 첫번째연출_PC대사02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        face_emotion(spawnId=0, emotionName='Trigger_panic')
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__5$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 첫번째연출_조디대사02()


class 첫번째연출_조디대사02(state.State):
    def on_enter(self):
        face_emotion(spawnId=1001, emotionName='Trigger_Talk03_A')
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__7$', duration=3000)
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__8$', duration=3000)
        face_emotion(spawnId=1001, emotionName='Trigger_Talk02_A')
        add_cinematic_talk(npcId=11003344, illustId='Peach_normal', msg='$52010026_QD__MAIN__9$', duration=3000, align='Right')
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__10$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 첫번째연출_PC대사03()


class 첫번째연출_PC대사03(state.State):
    def on_enter(self):
        face_emotion(spawnId=0, emotionName='Trigger_serious')
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__11$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 첫번째연출_조디대사03()


class 첫번째연출_조디대사03(state.State):
    def on_enter(self):
        face_emotion(spawnId=1001, emotionName='Trigger_Talk01_A')
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__12$', duration=3000)
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__13$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 첫번째연출_PC대사04()


class 첫번째연출_PC대사04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        face_emotion(spawnId=0, emotionName='Trigger_serious')
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__14$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 조디_카메라01()


class 조디_카메라01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 첫번째연출_조디대사04()


class 첫번째연출_조디대사04(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False)
        face_emotion(spawnId=1001, emotionName='Trigger_Idle02_A')
        set_npc_emotion_loop(spawnId=1001, sequenceName='Trigger_Idle_A', duration=10000)
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__15$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 첫번째연출_조디대사05()


class 첫번째연출_조디대사05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        set_onetime_effect(id=301, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__16$', duration=3000)
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__17$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 첫번째연출_PC대사05()

    def on_exit(self):
        visible_my_pc(isVisible=True)


class 첫번째연출_PC대사05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        face_emotion(spawnId=0, emotionName='Trigger_serious')
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__18$', duration=3000)
        set_npc_emotion_loop(spawnId=1001, sequenceName='Trigger_Idle_A', duration=10000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 조디_카메라02()


class 조디_카메라02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 첫번째연출_조디대사06()


class 첫번째연출_조디대사06(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        face_emotion(spawnId=1001, emotionName='Idle_A')
        set_pc_emotion_loop(sequenceName='Idle_A', duration=1000)
        add_cinematic_talk(npcId=11003344, msg='$52010026_QD__MAIN__19$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__20$', duration=3000)
        set_event_ui(type=1, arg2='$52010026_QD__MAIN__21$', arg3='8000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 두번째연출_ready()

    def on_exit(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_sound(triggerId=7001, arg2=False)
        set_scene_skip()


class 두번째연출_ready(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=100)
        reset_camera(interpolationTime=0.5)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2101]):
            return 두번째연출_black()


class 두번째연출_black(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4501], returnView=False)
        create_monster(spawnIds=[1000], arg2=False, arg3=30000)
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)
        create_monster(spawnIds=[101], arg2=False, arg3=0)
        create_monster(spawnIds=[102], arg2=False, arg3=0)
        set_npc_emotion_loop(spawnId=1000, sequenceName='Down_Idle_A', duration=70000)
        set_scene_skip(state=두번째연출_피치전투01, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 두번째연출_피치발견01()


class 두번째연출_피치발견01(state.State):
    def on_enter(self):
        set_onetime_effect(id=201, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003343, msg='$52010026_QD__MAIN__22$', duration=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 두번째연출_피치발견02()


class 두번째연출_피치발견02(state.State):
    def on_enter(self):
        set_onetime_effect(id=201, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        add_balloon_talk(spawnId=0, msg='$52010026_QD__MAIN__47$', duration=1000, delayTick=0)
        select_camera_path(pathIds=[4501,4502], returnView=False)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 두번째연출_피치전투01()


class 두번째연출_피치전투01(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_balloon_talk(spawnId=1000, msg='$52010026_QD__MAIN__24$', duration=1000, delayTick=0)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52010026_QD__MAIN__25$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 두번째연출_피치전투02()


class 두번째연출_피치전투02(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102]):
            return 두번째연출_딜레이01()


class 두번째연출_딜레이01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        add_balloon_talk(spawnId=1000, msg='$52010026_QD__MAIN__26$', duration=2000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 두번째연출_피치전투03()


class 두번째연출_피치전투03(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=1000, msg='$52010026_QD__MAIN__27$', duration=2000, delayTick=0)
        set_onetime_effect(id=202, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_effect(triggerIds=[5003], visible=True)
        set_effect(triggerIds=[5004], visible=True)
        set_effect(triggerIds=[5005], visible=True)
        create_monster(spawnIds=[103], arg2=False, arg3=0)
        create_monster(spawnIds=[104], arg2=False, arg3=0)
        create_monster(spawnIds=[105], arg2=False, arg3=0)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103,104,105]):
            return 두번째연출_딜레이02()


class 두번째연출_딜레이02(state.State):
    def on_enter(self):
        set_onetime_effect(id=202, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[5005], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 두번째연출_PC대사01()


class 두번째연출_PC대사01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__28$', duration=3000)
        set_scene_skip(state=Skip, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 두번째연출_잠시쉬기()


class Skip(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=4)
        create_monster(spawnIds=[111], arg2=False, arg3=6000)
        create_monster(spawnIds=[112], arg2=False, arg3=6000)
        create_monster(spawnIds=[113], arg2=False, arg3=6000)
        create_monster(spawnIds=[114], arg2=False, arg3=6000)
        create_monster(spawnIds=[115], arg2=False, arg3=6000)
        create_monster(spawnIds=[121], arg2=False, arg3=5000)
        create_monster(spawnIds=[122], arg2=False, arg3=5000)
        create_monster(spawnIds=[123], arg2=False, arg3=5000)
        create_monster(spawnIds=[124], arg2=False, arg3=5000)
        create_monster(spawnIds=[125], arg2=False, arg3=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 세번째연출_대사01()


class 두번째연출_잠시쉬기(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        add_cinematic_talk(npcId=11003343, illustId='Peach_normal', align='Left', msg='$52010026_QD__MAIN__29$', duration=2000)
        add_cinematic_talk(npcId=11003343, msg='$52010026_QD__MAIN__30$', duration=2000)
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__48$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 세번째연출_포털개방()


class 세번째연출_포털개방(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4201], returnView=False)
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_ambient_light(primary=[128,128,128])
        set_effect(triggerIds=[201], visible=True)
        set_onetime_effect(id=998, enable=True, path='BG/sound/Eff_DevilPortal_01.xml')
        create_monster(spawnIds=[111], arg2=False, arg3=6000)
        create_monster(spawnIds=[112], arg2=False, arg3=6000)
        create_monster(spawnIds=[113], arg2=False, arg3=6000)
        create_monster(spawnIds=[114], arg2=False, arg3=6000)
        create_monster(spawnIds=[115], arg2=False, arg3=6000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세번째연출_포털개방02()


class 세번째연출_포털개방02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4301], returnView=False)
        set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_effect(triggerIds=[211], visible=True)
        create_monster(spawnIds=[121], arg2=False, arg3=5000)
        create_monster(spawnIds=[122], arg2=False, arg3=5000)
        create_monster(spawnIds=[123], arg2=False, arg3=5000)
        create_monster(spawnIds=[124], arg2=False, arg3=5000)
        create_monster(spawnIds=[125], arg2=False, arg3=5000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 세번째연출_대사01()


class 세번째연출_대사01(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        add_balloon_talk(spawnId=0, msg='$52010026_QD__MAIN__32$', duration=2000, delayTick=0)
        set_npc_emotion_sequence(spawnId=1000, sequenceName='ChatUP_A')
        add_balloon_talk(spawnId=1000, msg='$52010026_QD__MAIN__33$', duration=2000, delayTick=2000)
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52010026_QD__MAIN__34$', arg3='2000', arg4='4000')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 피치탈출()


class 피치탈출(state.State):
    def on_enter(self):
        move_npc(spawnId=1000, patrolName='MS2PatrolData_3002')
        add_balloon_talk(spawnId=1000, msg='$52010026_QD__MAIN__42$', duration=2000, delayTick=0)
        add_buff(boxIds=[2101], skillId=70000123, level=1, arg4=False, arg5=False)
        set_effect(triggerIds=[5101], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111,112,113,114,115,121,122,123,124,125]):
            return 세번째연출_대사02()


class 세번째연출_대사02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[201], visible=False)
        set_effect(triggerIds=[221], visible=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=998, enable=False, path='BG/sound/Eff_DevilPortal_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 세번째연출_대사02_1()


class 세번째연출_대사02_1(state.State):
    def on_enter(self):
        set_scene_skip(state=skip_a, arg2='nextState')
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__35$', duration=2000)
        add_cinematic_talk(npcId=11003343, msg='$52010026_QD__MAIN__36$', duration=2000)
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__49$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 다섯번째연출_ready()


class 다섯번째연출_ready(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4402], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 다섯번째연출_엘리트몬스터()


class skip_a(state.State):
    def on_enter(self):
        set_scene_skip()
        create_monster(spawnIds=[131], arg2=True, arg3=0)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 다섯번째연출_엘리트몬스터대사()


class 다섯번째연출_엘리트몬스터(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=1000, sequenceName='Trigger_Hurt_A', duration=28000)
        select_camera_path(pathIds=[4401], returnView=False)
        set_onetime_effect(id=7, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52010026, portalId=6002)
        set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=997, enable=True, path='BG/sound/Eff_BossRegen_01.xml')
        create_monster(spawnIds=[131], arg2=True, arg3=0)
        show_caption(scale=2.3, type='NameCaption', title='$52010026_QD__MAIN__50$', desc='$52010026_QD__MAIN__51$', align='centerLeft', offsetRateX=-0.15, duration=4000)
        set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 다섯번째연출_엘리트몬스터대사()


class 다섯번째연출_엘리트몬스터대사(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52010026_QD__MAIN__38$', arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 다섯번째연출_전투()


class 다섯번째연출_전투(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_onetime_effect(id=997, enable=False, path='BG/sound/Eff_BossRegen_01.xml')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[131]):
            return 다섯번째연출_마지막()


class 다섯번째연출_마지막(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=Warp, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 다섯번째연출_대화02()


class 다섯번째연출_대화02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        face_emotion(spawnId=0, emotionName='Trigger_disappoint')
        set_pc_emotion_loop(sequenceName='Down_B', duration=18000)
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[5201], visible=True)
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__43$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010026_QD__MAIN__44$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 다섯번째연출_암전()


class 다섯번째연출_암전(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 다섯번째연출_의문의목소리암전()


class 다섯번째연출_의문의목소리암전(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003145, msg='$52010026_QD__MAIN__45$', duration=3000)
        add_cinematic_talk(npcId=11003145, msg='$52010026_QD__MAIN__46$', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Warp()


class Warp(state.State):
    def on_enter(self):
        move_user(mapId=63000042, portalId=10)


