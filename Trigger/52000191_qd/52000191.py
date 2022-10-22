""" trigger/52000191_qd/52000191.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=False) # 마법진
        set_effect(triggerIds=[6008], visible=False) # 마법진
        set_effect(triggerIds=[6015], visible=False) # 마법진
        set_effect(triggerIds=[6022], visible=False) # 마법진
        set_effect(triggerIds=[6033], visible=False) # 마법진

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003412], questStates=[1]):
            return CameraEffect01()


class CameraEffect01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return CameraEffect02()


class CameraEffect02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)
        set_cinematic_ui(type=1)
        move_user(mapId=52000191, portalId=5001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03()


class CameraEffect03(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=1)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CameraEffect03_3()


class CameraEffect03_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4003], returnView=False)
        move_user_path(patrolName='MS2PatrolData_3001')
        show_caption(type='VerticalCaption', title='$52000191_QD__52000191__0$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 바론과첫만남_01()


class 바론과첫만남_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52000191_QD__52000191__1$', duration=5000)
        add_cinematic_talk(npcId=11004787, msg='$52000191_QD__52000191__2$', align='left', illustId='Baron_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 바론과첫만남_02()


class 바론과첫만남_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005,4006], returnView=False)
        set_pc_emotion_loop(sequenceName='Talk_A', duration=5000)
        add_cinematic_talk(npcId=0, msg='$52000191_QD__52000191__3$', duration=5000)
        add_cinematic_talk(npcId=11004787, msg='$52000191_QD__52000191__4$', align='left', illustId='Baron_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 바론과첫만남_02_02()


class 바론과첫만남_02_02(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Talk_A', duration=5000)
        add_cinematic_talk(npcId=0, msg='$52000191_QD__52000191__5$', duration=5000)
        add_cinematic_talk(npcId=11004787, msg='$52000191_QD__52000191__6$', align='left', illustId='Baron_normal', duration=4000)
        add_cinematic_talk(npcId=11004787, msg='$52000191_QD__52000191__7$', align='left', illustId='Baron_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=13000):
            return 바론과첫만남_03()


class 바론과첫만남_03(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Angry_A'])
        add_cinematic_talk(npcId=0, msg='$52000191_QD__52000191__8$', duration=4000)
        add_cinematic_talk(npcId=11004787, msg='$52000191_QD__52000191__9$', align='left', illustId='Baron_normal', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 전투준비()


class 전투준비(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=False) # 유저 투명 처리
        move_user(mapId=52000191, portalId=5003)
        select_camera_path(pathIds=[4007,4008], returnView=False)
        add_cinematic_talk(npcId=11004787, msg='$52000191_QD__52000191__10$', duration=4000)
        set_effect(triggerIds=[6029], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6030], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6031], visible=True) # 리젠 이펙트
        create_monster(spawnIds=[101]) # 연출용 수하 생성
        create_monster(spawnIds=[102]) # 연출용 수하 생성
        create_monster(spawnIds=[103]) # 연출용 수하 생성

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 전투준비_02()


class 전투준비_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투준비_03()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52000191, portalId=5003)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 전투준비_03()


class 전투준비_03(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        visible_my_pc(isVisible=True) # 유저 투명 처리

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 페이즈1()


class 페이즈1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_effect(triggerIds=[6001], visible=True) # 마법진
        set_effect(triggerIds=[6002], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6003], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6004], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6005], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6006], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6007], visible=True) # 리젠 이펙트
        create_monster(spawnIds=[201]) # 수하 생성
        create_monster(spawnIds=[202]) # 수하 생성
        create_monster(spawnIds=[203]) # 수하 생성
        create_monster(spawnIds=[204]) # 수하 생성
        create_monster(spawnIds=[205]) # 수하 생성
        create_monster(spawnIds=[206]) # 수하 생성
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204,205,206]):
            return 페이즈2()


class 페이즈2(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004787, illust='Baron_normal', script='$52000191_QD__52000191__11$', duration=3000)
        set_effect(triggerIds=[6001], visible=False) # 마법진
        set_effect(triggerIds=[6015], visible=True) # 마법진
        set_effect(triggerIds=[6016], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6017], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6018], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6019], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6020], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6021], visible=True) # 리젠 이펙트
        create_monster(spawnIds=[213]) # 수하 생성
        create_monster(spawnIds=[214]) # 수하 생성
        create_monster(spawnIds=[215]) # 수하 생성
        create_monster(spawnIds=[216]) # 수하 생성
        create_monster(spawnIds=[217]) # 수하 생성
        create_monster(spawnIds=[218]) # 수하 생성

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[213,214,215,216,217,218]):
            return 페이즈3()


class 페이즈3(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004787, illust='Baron_normal', script='$52000191_QD__52000191__12$', duration=3000)
        set_effect(triggerIds=[6015], visible=False) # 마법진
        set_effect(triggerIds=[6008], visible=True) # 마법진
        set_effect(triggerIds=[6009], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6010], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6011], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6012], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6013], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6014], visible=True) # 리젠 이펙트
        create_monster(spawnIds=[207]) # 수하 생성
        create_monster(spawnIds=[208]) # 수하 생성
        create_monster(spawnIds=[209]) # 수하 생성
        create_monster(spawnIds=[210]) # 수하 생성
        create_monster(spawnIds=[211]) # 수하 생성
        create_monster(spawnIds=[212]) # 수하 생성

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[207,208,209,210,211,212]):
            return 페이즈4()


class 페이즈4(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004787, illust='Baron_normal', script='$52000191_QD__52000191__13$', duration=3000)
        set_effect(triggerIds=[6008], visible=False) # 마법진
        set_effect(triggerIds=[6022], visible=True) # 마법진
        set_effect(triggerIds=[6023], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6024], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6025], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6026], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6027], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6028], visible=True) # 리젠 이펙트
        create_monster(spawnIds=[219]) # 수하 생성
        create_monster(spawnIds=[220]) # 수하 생성
        create_monster(spawnIds=[221]) # 수하 생성
        create_monster(spawnIds=[222]) # 수하 생성
        create_monster(spawnIds=[223]) # 수하 생성
        create_monster(spawnIds=[224]) # 수하 생성

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[219,220,221,222,223,224]):
            return 페이즈5()


class 페이즈5(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11004787, illust='Baron_normal', script='$52000191_QD__52000191__14$', duration=3000)
        set_effect(triggerIds=[6022], visible=False) # 마법진
        set_effect(triggerIds=[6033], visible=True) # 마법진
        set_effect(triggerIds=[6032], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6034], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6035], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6036], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6037], visible=True) # 리젠 이펙트
        set_effect(triggerIds=[6038], visible=True) # 리젠 이펙트
        create_monster(spawnIds=[225]) # 수하 생성
        create_monster(spawnIds=[226]) # 수하 생성
        create_monster(spawnIds=[227]) # 수하 생성
        create_monster(spawnIds=[228]) # 수하 생성
        create_monster(spawnIds=[229]) # 수하 생성
        create_monster(spawnIds=[230]) # 수하 생성

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[225,226,227,228,229,230]):
            return 고마해()


class 고마해(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 고마해_02()


class 고마해_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6033], visible=False) # 마법진
        select_camera_path(pathIds=[4009], returnView=False)
        move_user(mapId=52000191, portalId=5002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 고마해_03()


class 고마해_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_scene_skip(state=Skip_2, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 고마해_04()


class 고마해_04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4004], returnView=False)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=5000)
        add_cinematic_talk(npcId=0, msg='$52000191_QD__52000191__15$', duration=3000)
        add_cinematic_talk(npcId=11004787, msg='$52000191_QD__52000191__16$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 고마해_05()


class 고마해_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011,4012], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52000191_QD__52000191__17$', duration=5000)
        add_cinematic_talk(npcId=0, msg='$52000191_QD__52000191__18$', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 고마해_06()


class 고마해_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013,4014], returnView=False)
        add_cinematic_talk(npcId=11004787, msg='$52000191_QD__52000191__19$', duration=4000)
        add_cinematic_talk(npcId=11004787, msg='$52000191_QD__52000191__20$', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 고마해_07()


class Skip_2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 고마해_07()


class 고마해_07(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_achievement(triggerId=2001, achieve='BattlewithBaron')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 그만싸워()


class 그만싸워(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


