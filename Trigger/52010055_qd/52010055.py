""" trigger/52010055_qd/52010055.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_effect(triggerIds=[500], visible=False)
        set_effect(triggerIds=[501], visible=False)
        set_effect(triggerIds=[502], visible=False)
        remove_buff(boxId=9002, skillId=99910311) # 포탑으로변신
        destroy_monster(spawnIds=[-1])
        visible_my_pc(isVisible=False) # 캐릭터 숨김

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9002]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_mesh(triggerIds=[10000], visible=True) # 스폰 발판 생성
        set_mesh(triggerIds=[10001], visible=True) # 공습용발판 생성
        set_mesh(triggerIds=[30000], visible=True) # 대포1 생성
        set_mesh(triggerIds=[30001], visible=True) # 대포1 생성
        set_mesh(triggerIds=[30002], visible=True) # 대포1 생성
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[1], arg2=False) # 함교 연출용 블리체
        create_monster(spawnIds=[2], arg2=False) # 함교 연출용 네이린
        create_monster(spawnIds=[3], arg2=False) # 함교 연출용 콘대르
        create_monster(spawnIds=[4], arg2=False) # 함교 연출용 메이슨
        create_monster(spawnIds=[5], arg2=False) # 함교 연출용 샤텐
        create_monster(spawnIds=[10000], arg2=False) # 함교 연출용 해군
        create_monster(spawnIds=[10001], arg2=False) # 함교 연출용 해군
        create_monster(spawnIds=[10002], arg2=False) # 함교 연출용 해군
        create_monster(spawnIds=[100], arg2=False)
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[105], arg2=False)
        create_monster(spawnIds=[106], arg2=False)
        create_monster(spawnIds=[107], arg2=False)
        create_monster(spawnIds=[108], arg2=False)
        create_monster(spawnIds=[109], arg2=False)
        create_monster(spawnIds=[110], arg2=False)
        create_monster(spawnIds=[111], arg2=False)
        create_monster(spawnIds=[112], arg2=False)
        create_monster(spawnIds=[113], arg2=False)
        create_monster(spawnIds=[114], arg2=False)
        create_monster(spawnIds=[115], arg2=False)
        create_monster(spawnIds=[116], arg2=False)
        create_monster(spawnIds=[117], arg2=False)
        create_monster(spawnIds=[118], arg2=False)
        create_monster(spawnIds=[119], arg2=False)
        create_monster(spawnIds=[120], arg2=False)
        create_monster(spawnIds=[121], arg2=False)
        create_monster(spawnIds=[122], arg2=False)
        create_monster(spawnIds=[123], arg2=False)
        move_user(mapId=52010055, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 크림슨발록비춤1()


class 크림슨발록비춤1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_mesh(triggerIds=[10000], visible=False) # 스폰 발판 지움
        set_mesh(triggerIds=[10001], visible=False) # 공습용발판 지움
        set_scene_skip(state=게임시작, arg2='nextState')
        select_camera(triggerId=4001, enable=True)
        add_cinematic_talk(npcId=11003781, msg='$52010055_QD__52010055__0$', duration=3000, align='right')
        add_cinematic_talk(npcId=11003781, msg='$52010055_QD__52010055__1$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 크림슨이동()


class 크림슨이동(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=29000378, msg='$52010055_QD__52010055__2$', duration=3000, align='right')
        move_npc(spawnId=101, patrolName='PatrolDataBalrog_Open_101')
        move_npc(spawnId=102, patrolName='PatrolDataBalrog_Open_102')
        move_npc(spawnId=103, patrolName='PatrolDataBalrog_Open_103')
        move_npc(spawnId=104, patrolName='PatrolDataBalrog_Open_104')
        move_npc(spawnId=105, patrolName='PatrolDataBalrog_Open_105')
        move_npc(spawnId=106, patrolName='PatrolDataBalrog_Open_106')
        move_npc(spawnId=107, patrolName='PatrolDataBalrog_Open_107')
        move_npc(spawnId=108, patrolName='PatrolDataBalrog_Open_108')
        move_npc(spawnId=109, patrolName='PatrolDataBalrog_Open_109')
        move_npc(spawnId=110, patrolName='PatrolDataBalrog_Open_110')
        move_npc(spawnId=111, patrolName='PatrolDataBalrog_Open_111')
        move_npc(spawnId=112, patrolName='PatrolDataBalrog_Open_112')
        move_npc(spawnId=113, patrolName='PatrolDataBalrog_Open_113')
        move_npc(spawnId=114, patrolName='PatrolDataBalrog_Open_114')
        move_npc(spawnId=115, patrolName='PatrolDataBalrog_Open_115')
        move_npc(spawnId=116, patrolName='PatrolDataBalrog_Open_116')
        move_npc(spawnId=117, patrolName='PatrolDataBalrog_Open_117')
        move_npc(spawnId=118, patrolName='PatrolDataBalrog_Open_118')
        move_npc(spawnId=119, patrolName='PatrolDataBalrog_Open_119')
        move_npc(spawnId=120, patrolName='PatrolDataBalrog_Open_120')
        move_npc(spawnId=121, patrolName='PatrolDataBalrog_Open_121')
        move_npc(spawnId=122, patrolName='PatrolDataBalrog_Open_122')
        move_npc(spawnId=123, patrolName='PatrolDataBalrog_Open_123')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 함교비춤1()


class 함교비춤1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123])
        visible_my_pc(isVisible=True) # 캐릭터 보임
        move_user(mapId=52010055, portalId=2)
        select_camera_path(pathIds=[4002,4003], returnView=False)
        set_npc_emotion_sequence(spawnId=2, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003536, illustId='Neirin_surprise', msg='$52010055_QD__52010055__3$', duration=3000, align='left')
        add_cinematic_talk(npcId=11003682, illustId='Bliche_closeEye', msg='$52010055_QD__52010055__4$', duration=4000, align='Center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 함교비춤2()


class 함교비춤2(state.State):
    def on_enter(self):
        set_npc_rotation(spawnId=1, rotation=180)
        set_npc_emotion_sequence(spawnId=1, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010055_QD__52010055__5$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 콘대르대사()


class 콘대르대사(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=3, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52010055_QD__52010055__6$', duration=2000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 콘대르이동()


class 콘대르이동(state.State):
    def on_enter(self):
        move_npc(spawnId=3, patrolName='PatrolDataOpenConder0')
        set_npc_emotion_sequence(spawnId=5, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003584, illustId='Schatten_normal', msg='$52010055_QD__52010055__7$', duration=2000, align='Reft')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 샤텐이동()


class 샤텐이동(state.State):
    def on_enter(self):
        move_npc(spawnId=5, patrolName='PatrolDataOpenSchatten0')
        set_npc_emotion_sequence(spawnId=4, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003586, illustId='Mason_closeEye', msg='$52010055_QD__52010055__8$', duration=3000, align='Left')
        destroy_monster(spawnIds=[3])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 메이슨이동()


class 메이슨이동(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5])
        move_npc(spawnId=4, patrolName='PatrolDataOpenMason0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 함교비춤3()


class 함교비춤3(state.State):
    def on_enter(self):
        set_npc_rotation(spawnId=1, rotation=270)
        set_npc_emotion_sequence(spawnId=1, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010055_QD__52010055__9$', duration=3000, align='right')
        destroy_monster(spawnIds=[4])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 함교비춤4()


class 함교비춤4(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=2, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003536, illustId='Neirin_surprise', msg='$52010055_QD__52010055__10$', duration=2000, align='left')
        set_npc_emotion_sequence(spawnId=1, sequenceName='Talk_A')
        set_npc_rotation(spawnId=1, rotation=170)
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010055_QD__52010055__11$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 함교비춤5()


class 함교비춤5(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Calm_A'])
        init_npc_rotation(spawnIds=[1])
        set_npc_emotion_sequence(spawnId=1, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010055_QD__52010055__12$', duration=3000, align='Left')
        set_npc_emotion_sequence(spawnId=2, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003536, illustId='Neirin_surprise', msg='$52010055_QD__52010055__13$', duration=3000, align='Right')
        set_npc_emotion_sequence(spawnId=1, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010055_QD__52010055__14$', duration=2000, align='right')
        add_cinematic_talk(npcId=11003682, illustId='Bliche_closeEye', msg='$52010055_QD__52010055__15$', duration=2000, align='right')
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010055_QD__52010055__16$', duration=2000, align='right')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=12000):
            return 게임시작()


class 게임시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10002,10003,10004,10005], visible=True) # 1차 전투 링
        select_camera_path(pathIds=[4003,4019], returnView=False)
        visible_my_pc(isVisible=True) # 캐릭터 보임
        reset_camera(interpolationTime=0)
        move_user(mapId=52010055, portalId=3)
        set_local_camera(cameraId=9009, enable=True)
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        side_npc_talk(npcId=11003533, illust='Bliche_closeEye', duration=3000, script='$52010055_QD__52010055__17$', voice='ko/Npc/00002154')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차발록스피어스폰1()


class 차발록스피어스폰1(state.State):
    def on_enter(self):
        select_camera(triggerId=4019, enable=True)
        set_mesh(triggerIds=[10000], visible=False) # 스폰 발판 제거
        create_monster(spawnIds=[1], arg2=False) # 함교 연출용 블리체
        create_monster(spawnIds=[2], arg2=False) # 함교 연출용 네이린
        create_monster(spawnIds=[10000], arg2=False) # 함교 연출용 해군
        create_monster(spawnIds=[10001], arg2=False) # 함교 연출용 해군
        create_monster(spawnIds=[10002], arg2=False) # 함교 연출용 해군
        create_monster(spawnIds=[1000], arg2=False)
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1002], arg2=False)
        create_monster(spawnIds=[1003], arg2=False)
        create_monster(spawnIds=[1004], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1000,1001,1002,1003,1004]):
            return 차발록스피어스폰2()


class 차발록스피어스폰2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)
        create_monster(spawnIds=[1009], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1005,1006,1007,1008,1009]):
            return 차발록스피어스폰3()


class 차발록스피어스폰3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1010], arg2=False)
        create_monster(spawnIds=[1011], arg2=False)
        create_monster(spawnIds=[1012], arg2=False)
        create_monster(spawnIds=[1013], arg2=False)
        create_monster(spawnIds=[1014], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1010,1011,1012,1013,1014]):
            return 차크림슨스폰1()


class 차크림슨스폰1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[200], arg2=False)
        create_monster(spawnIds=[201], arg2=False)
        create_monster(spawnIds=[202], arg2=False)
        create_monster(spawnIds=[203], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[200,201,202,203]):
            return 차크림슨스폰2()


class 차크림슨스폰2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=False)
        create_monster(spawnIds=[205], arg2=False)
        create_monster(spawnIds=[206], arg2=False)
        create_monster(spawnIds=[207], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[204,205,206,207]):
            return 차크림슨스폰3()


class 차크림슨스폰3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1005], arg2=False)
        create_monster(spawnIds=[1006], arg2=False)
        create_monster(spawnIds=[1007], arg2=False)
        create_monster(spawnIds=[1008], arg2=False)
        create_monster(spawnIds=[1009], arg2=False)
        create_monster(spawnIds=[209], arg2=False)
        create_monster(spawnIds=[210], arg2=False)
        create_monster(spawnIds=[211], arg2=False)
        create_monster(spawnIds=[212], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1005,1006,1007,1008,1009,209,210,211,212]):
            return 차크림슨스폰4()


class 차크림슨스폰4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1010], arg2=False)
        create_monster(spawnIds=[1011], arg2=False)
        create_monster(spawnIds=[1012], arg2=False)
        create_monster(spawnIds=[1013], arg2=False)
        create_monster(spawnIds=[1014], arg2=False)
        create_monster(spawnIds=[213], arg2=False)
        create_monster(spawnIds=[214], arg2=False)
        create_monster(spawnIds=[215], arg2=False)
        create_monster(spawnIds=[216], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1010,1011,1012,1013,1014,213,214,215,216]):
            return 보스전연출준비()


class 보스전연출준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        visible_my_pc(isVisible=True) # 캐릭터 보임
        move_user(mapId=52010055, portalId=4)
        remove_buff(boxId=9002, skillId=99910311) # 포탑으로변신
        reset_camera(interpolationTime=0)
        set_mesh(triggerIds=[10002,10003,10004,10005], visible=True) # 1차 전투 링생성
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보스전연출시작()


class 보스전연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        select_camera(triggerId=4006, enable=True)
        create_monster(spawnIds=[1], arg2=False) # 함교 연출용 블리체
        create_monster(spawnIds=[2], arg2=False) # 함교 연출용 네이린
        create_monster(spawnIds=[2000], arg2=False) # 연출용 보스소환

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보스전연출1()


class 보스전연출1(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=2000, sequenceName='Attack_01_A')
        add_cinematic_talk(npcId=29000382, msg='$52010055_QD__52010055__21$', duration=3000, align='right')
        set_pc_emotion_sequence(sequenceNames=['Emotion_Suprise_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 보스전시작()


class 보스전시작(state.State):
    def on_enter(self):
        select_camera(triggerId=4019, enable=True)
        destroy_monster(spawnIds=[2000])
        create_monster(spawnIds=[2001], arg2=True) # 전투용 보스 소환
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2001]):
            return 보스사망체크()


class 보스사망체크(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True) # 캐릭터 보임
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보스전끝크림슨발록대사1()


class 보스전끝크림슨발록대사1(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        set_mesh(triggerIds=[10002,10003,10004,10005], visible=False) # 1차 전투 링 해제
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[1], arg2=False) # 함교 연출용 블리체
        create_monster(spawnIds=[2], arg2=False) # 함교 연출용 네이린
        create_monster(spawnIds=[13], arg2=False) # 엔딩 연출용 콘대르
        create_monster(spawnIds=[14], arg2=False) # 엔딩 연출용 메이슨
        create_monster(spawnIds=[15], arg2=False) # 엔딩 연출용 샤텐
        create_monster(spawnIds=[2002], arg2=False) # 연출용 보스소환
        move_user(mapId=52010055, portalId=5) # 스카이 포트리스 작전실로 텔레포트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 엔딩연출크림슨발록보스1()


class 엔딩연출크림슨발록보스1(state.State):
    def on_enter(self):
        set_npc_rotation(spawnId=14, rotation=-10)
        set_npc_rotation(spawnId=15, rotation=10)
        select_camera(triggerId=4006, enable=True)
        move_user_path(patrolName='PatrolDataEndPC0') # 유저 보스잡고 걸어감
        set_npc_emotion_sequence(spawnId=2002, sequenceName='Dead_01_A')
        add_cinematic_talk(npcId=29000382, msg='$52010055_QD__52010055__22$', duration=3000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 엔딩연출크림슨발록보스2()


class 엔딩연출크림슨발록보스2(state.State):
    def on_enter(self):
        change_monster(removeSpawnId=2002, addSpawnId=2003) # 함교 연출용 블리체
        set_npc_emotion_sequence(spawnId=2003, sequenceName='Dead_01_A')
        set_scene_skip(state=맵이동, arg2='nextState')
        select_camera_path(pathIds=[4007,4008], returnView=False)
        visible_my_pc(isVisible=False) # 캐릭터 숨김
        set_npc_emotion_sequence(spawnId=13, sequenceName='Attack_Idle_A,Attack_Idle_A,Attack_Idle_A,Attack_Idle_A')
        set_npc_emotion_sequence(spawnId=14, sequenceName='Attack_Idle_A,Attack_Idle_A,Attack_Idle_A,Attack_Idle_A')
        set_npc_emotion_sequence(spawnId=15, sequenceName='Attack_Idle_A,Attack_Idle_A,Attack_Idle_A,Attack_Idle_A')
        add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52010055_QD__52010055__23$', duration=2000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 엔딩연출샤텐1()


class 엔딩연출샤텐1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[2002])
        set_npc_emotion_sequence(spawnId=13, sequenceName='Attack_Idle_A')
        set_npc_emotion_sequence(spawnId=14, sequenceName='Attack_Idle_A')
        set_npc_emotion_sequence(spawnId=15, sequenceName='Attack_Idle_A')
        add_cinematic_talk(npcId=11003584, illustId='Schatten_normal', msg='$52010055_QD__52010055__24$', duration=3000, align='Reft')
        select_camera_path(pathIds=[4009,4010], returnView=False)
        select_camera(triggerId=4010, enable=True)
        set_npc_emotion_sequence(spawnId=15, sequenceName='Attack_Idle_A,Attack_01_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 엔딩연출메이슨1()


class 엔딩연출메이슨1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003586, illustId='Mason_closeEye', msg='$52010055_QD__52010055__25$', duration=1500, align='Reft')
        select_camera(triggerId=4014, enable=True)
        select_camera_path(pathIds=[4014,4015], returnView=False)
        set_npc_emotion_sequence(spawnId=13, sequenceName='Attack_Idle_A')
        set_npc_emotion_sequence(spawnId=14, sequenceName='Attack_Idle_A,Attack_01_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 엔딩연출콘대르1()


class 엔딩연출콘대르1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[500], visible=True)
        set_effect(triggerIds=[501], visible=True)
        add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52010055_QD__52010055__26$', duration=3000, align='Reft')
        select_camera_path(pathIds=[4016,4017], returnView=False)
        move_npc(spawnId=13, patrolName='PatrolDataCondorAttack1') # 엔딩 연출용 콘대르 돌진

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 엔딩연출콘대르2()


class 엔딩연출콘대르2(state.State):
    def on_enter(self):
        select_camera(triggerId=4006, enable=True)
        set_effect(triggerIds=[5000], visible=True)
        set_effect(triggerIds=[5000], visible=True)
        set_effect(triggerIds=[502], visible=True)
        set_npc_emotion_sequence(spawnId=13, sequenceName='Attack_01_G,Attack_02_G,Attack_03_G,Attack_06_G')
        set_npc_emotion_sequence(spawnId=2003, sequenceName='Stun_A,Stun_A,Stun_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3002):
            return 엔딩연출클림슨발록사망1()


class 엔딩연출클림슨발록사망1(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=2003, sequenceName='Dead_01_A')
        add_cinematic_talk(npcId=29000382, msg='$52010055_QD__52010055__27$', duration=3000, align='right') # 크아악

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 엔딩연출준비1()


class 엔딩연출준비1(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        destroy_monster(spawnIds=[2003], arg2=False) # 엔딩연출용크림슨발록
        destroy_monster(spawnIds=[13]) # 엔딩 연출용 콘대르
        destroy_monster(spawnIds=[14]) # 엔딩 연출용 콘대르
        destroy_monster(spawnIds=[15]) # 엔딩 연출용 콘대르
        move_user(mapId=52010055, portalId=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 엔딩연출준비2()


class 엔딩연출준비2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 크림슨대사준비1()


class 크림슨대사준비1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[700], arg2=False)
        create_monster(spawnIds=[701], arg2=False)
        create_monster(spawnIds=[702], arg2=False)
        create_monster(spawnIds=[703], arg2=False)
        create_monster(spawnIds=[704], arg2=False)
        create_monster(spawnIds=[705], arg2=False)
        create_monster(spawnIds=[706], arg2=False)
        create_monster(spawnIds=[707], arg2=False)
        visible_my_pc(isVisible=False) # 캐릭터 숨김
        move_user(mapId=52010055, portalId=7) # 유저를 포탑으로 텔레포트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 엔딩연출크림슨카메라1()


class 엔딩연출크림슨카메라1(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml') # 암전
        select_camera(triggerId=4023, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 엔딩연출크림슨대사1()


class 엔딩연출크림슨대사1(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=29000378, msg='$52010055_QD__52010055__29$', duration=3000, align='right')
        move_npc(spawnId=700, patrolName='PatrolData700') # 엔딩 연출용 크림슨도망
        move_npc(spawnId=701, patrolName='PatrolData701') # 엔딩 연출용 크림슨도망
        move_npc(spawnId=702, patrolName='PatrolData702') # 엔딩 연출용 크림슨도망
        move_npc(spawnId=703, patrolName='PatrolData703') # 엔딩 연출용 크림슨도망
        move_npc(spawnId=704, patrolName='PatrolData704') # 엔딩 연출용 크림슨도망
        move_npc(spawnId=705, patrolName='PatrolData705') # 엔딩 연출용 크림슨도망
        move_npc(spawnId=706, patrolName='PatrolData706') # 엔딩 연출용 크림슨도망
        move_npc(spawnId=707, patrolName='PatrolData707') # 엔딩 연출용 크림슨도망

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 엔딩이동준비1()


class 엔딩이동준비1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        destroy_monster(spawnIds=[-1])
        move_user(mapId=52010055, portalId=8, boxId=9002)
        visible_my_pc(isVisible=True) # 캐릭터 보임

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 엔딩이동준비2()


class 엔딩이동준비2(state.State):
    def on_enter(self):
        select_camera(triggerId=4024, enable=True)
        create_monster(spawnIds=[1], arg2=False) # 함교 연출용 블리체
        create_monster(spawnIds=[2], arg2=False) # 함교 연출용 네이린
        create_monster(spawnIds=[13], arg2=False) # 함교 연출용 콘대르
        create_monster(spawnIds=[14], arg2=False) # 함교 연출용 블리체
        create_monster(spawnIds=[15], arg2=False) # 함교 연출용 네이린
        create_monster(spawnIds=[10001], arg2=False) # 함교 연출용 해군
        create_monster(spawnIds=[10002], arg2=False) # 함교 연출용 해군

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 엔딩NPC이동1()


class 엔딩NPC이동1(state.State):
    def on_enter(self):
        move_user_path(patrolName='PatrolDataEndPC2') # 엔딩 연출용 유저 이동
        move_npc(spawnId=13, patrolName='PatrolDataEndCondor1') # 엔딩 연출용 콘대르 이동
        move_npc(spawnId=14, patrolName='PatrolDataEndMason1') # 엔딩 연출용 메이슨 이동
        move_npc(spawnId=15, patrolName='PatrolDataEndSchatten1') # 엔딩 연출용 샤텐 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 엔딩대사콘대르1()


class 엔딩대사콘대르1(state.State):
    def on_enter(self):
        set_npc_rotation(spawnId=15, rotation=60)
        set_npc_rotation(spawnId=14, rotation=330)
        set_npc_emotion_sequence(spawnId=13, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003776, illustId='Conder_normal', msg='$52010055_QD__52010055__30$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 엔딩대사샤텐1()


class 엔딩대사샤텐1(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=15, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003584, illustId='Schatten_normal', msg='$52010055_QD__52010055__31$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 엔딩대사메이슨1()


class 엔딩대사메이슨1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10000], visible=False)
        set_mesh(triggerIds=[10001], visible=False)
        set_mesh(triggerIds=[10002], visible=False)
        set_mesh(triggerIds=[10003], visible=False)
        set_mesh(triggerIds=[10004], visible=False)
        set_npc_emotion_sequence(spawnId=14, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003586, illustId='Mason_closeEye', msg='$52010055_QD__52010055__32$', duration=3000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 함교로카메라전환1()


class 함교로카메라전환1(state.State):
    def on_enter(self):
        select_camera(triggerId=4025, enable=True)
        visible_my_pc(isVisible=False) # 캐릭터 숨김
        move_user(mapId=52010055, portalId=2) # 함교 내부로 텔레포트
        set_onetime_effect(id=10, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=300):
            return 엔딩대사네이린1()


class 엔딩대사네이린1(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=22, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003536, illustId='Neirin_normal', msg='$52010055_QD__52010055__33$', duration=4000, align='right')
        add_cinematic_talk(npcId=11003536, illustId='Neirin_normal', msg='$52010055_QD__52010055__34$', duration=4000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 엔딩대사블리체1()


class 엔딩대사블리체1(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=21, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010055_QD__52010055__35$', duration=3000, align='right')
        add_cinematic_talk(npcId=11003533, illustId='Bliche_normal', msg='$52010055_QD__52010055__36$', duration=5000, align='right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 엔딩연출종료1()


class 엔딩연출종료1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 맵이동()


class 맵이동(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        visible_my_pc(isVisible=True) # 캐릭터 보임
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=9002, type='trigger', achieve='rescueskyfortress')
        set_onetime_effect(id=12, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')
        move_user(mapId=52010052) # 스카이 포트리스 작전실로 텔레포트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None # Missing State: 


