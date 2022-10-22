""" trigger/52020016_qd/main.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_portal(portalId=95, visible=False, enabled=False)
        set_portal(portalId=96, visible=False, enabled=False)
        set_effect(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=False)
        set_mesh(triggerIds=[5001,5002,5003,5004,5005], visible=False, arg3=0, arg4=0, arg5=0)
        # <action name="이펙트를설정한다" arg1="71001-71016" arg2="0" />
        set_effect(triggerIds=[72001,72002,72003,72004,72005,72006,72007,72008,72009,72010,72011,72012], visible=False)
        set_effect(triggerIds=[73001,73002,73003,73004,73005,73006,73007,73008,73009,73010,73011,73012], visible=False)
        set_mesh(triggerIds=[5103,5104], visible=False, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 시작_2()


class 시작_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        select_camera_path(pathIds=[2000004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 시작_2_2()


class 시작_2_2(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=0, script='이곳은 뭐하는 곳이지?!', arg4=3, arg5=0)
        set_conversation(type=2, spawnId=0, script='미카엘의 기운이 느껴지고 있어!\n서둘러야 해!!', arg4=3, arg5=0)
        set_skip(state=시작_3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 시작_3()


class 시작_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000004], returnView=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 시작_4()


class 시작_4(state.State):
    def on_enter(self):
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)
        set_conversation(type=1, spawnId=0, script='한번 가볼까?', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 인트로()


class 인트로(state.State):
    def on_enter(self):
        set_ambient_light(primary=[0,0,0])
        set_directional_light(diffuseColor=[0,0,0], specularColor=[0,0,0])
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        set_pc_emotion_loop(sequenceName='Stun_A', duration=1500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=400):
            return 인트로_2()


class 인트로_2(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=0, script='???!!!', arg4=2, arg5=0)
        set_conversation(type=2, spawnId=0, script='뭐야!!\n앞이 안보여!!', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 인트로_3()


class 인트로_3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 미카엘등장()


class 미카엘등장(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000001], returnView=False)
        create_monster(spawnIds=[300001], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 미카엘_이동_1()


class 미카엘_이동_1(state.State):
    def on_enter(self):
        move_npc(spawnId=300001, patrolName='MS2PatrolData0_300001_0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대화_1()


class 대화_1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=300001, script='오호...여기까지 오다니...놀랍군요..', arg4=5)
        set_conversation(type=2, spawnId=300001, script='자...그럼 본격적으로 놀아볼까요?', arg4=5)
        set_skip(state=카메라리셋_1)
        set_mesh(triggerIds=[5001,5002,5003,5004,5005], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 카메라리셋_1()


class 카메라리셋_1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000001], returnView=True)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)
        destroy_monster(spawnIds=[300001])
        # <action name="버프를걸어준다" arg1="102" arg2="70000102" arg3="1" />
        set_effect(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이동_1()


class 이동_1(state.State):
    def on_enter(self):
        move_user(mapId=52020016, portalId=90)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 전투페이즈_1()

    def on_exit(self):
        set_ambient_light(primary=[180,180,149])
        set_directional_light(diffuseColor=[219,204,182], specularColor=[219,204,182])
        set_portal(portalId=95, visible=True, enabled=True)
        set_conversation(type=1, spawnId=0, script='갇혀 버렸어!', arg4=3, arg5=0)


class 전투페이즈_1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 전투종료()

    def on_exit(self):
        set_event_ui(type=1, arg2='미카엘이 조종하는 마리오네트 무리들을 처치하세요.', arg3='4000')
        shadow_expedition(type='OpenBossGauge', maxGaugePoint=300, title='몬스터 처치 달성')
        set_user_value(triggerId=901, key='respawn_phase_1', value=1)
        set_user_value(triggerId=902, key='respawn_phase_1', value=1)
        set_user_value(triggerId=903, key='respawn_phase_1', value=1)
        set_user_value(triggerId=904, key='respawn_phase_1', value=1)


class 전투종료(state.State):
    def on_tick(self) -> state.State:
        if shadow_expedition_reach_point(point=300):
            return 페이즈_2_준비()


class 페이즈_2_준비(state.State):
    def on_enter(self):
        shadow_expedition(type='CloseBossGauge')
        set_user_value(triggerId=901, key='respawn_phase_1_end', value=1)
        set_user_value(triggerId=902, key='respawn_phase_1_end', value=1)
        set_user_value(triggerId=903, key='respawn_phase_1_end', value=1)
        set_user_value(triggerId=904, key='respawn_phase_1_end', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 불꺼짐()


class 불꺼짐(state.State):
    def on_enter(self):
        set_portal(portalId=95, visible=False, enabled=False)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        set_ambient_light(primary=[0,0,0])
        set_directional_light(diffuseColor=[0,0,0], specularColor=[0,0,0])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 미카엘등장_2()


class 미카엘등장_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000002], returnView=False)
        create_monster(spawnIds=[300002], arg2=False)
        move_npc(spawnId=300002, patrolName='MS2PatrolData0_300002_1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대화_2()


class 대화_2(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=300002, script='음... 기대 이상인데요?', arg4=5)
        set_conversation(type=2, spawnId=300002, script='이번엔 이분들이 당신과 놀아줄겁니다!!', arg4=5)
        move_user(mapId=52020016, portalId=91)
        set_skip(state=카메라리셋_2)
        set_mesh(triggerIds=[5103,5104], visible=True, arg3=0, arg4=0, arg5=0)
        # <action name="메쉬를설정한다" arg1="5001-5005" arg2="1" arg3="0" arg4="0" arg5="0"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return npc등장연출_1()


class npc등장연출_1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[310001], arg2=False)
        # <action name="메쉬를설정한다" arg1="5001-5005" arg2="1" arg3="0" arg4="0" arg5="0"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return npc등장연출_2()


class npc등장연출_2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[310002], arg2=False)
        # <action name="메쉬를설정한다" arg1="5001-5005" arg2="1" arg3="0" arg4="0" arg5="0"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return npc등장연출_3()


class npc등장연출_3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[310003], arg2=False)
        # <action name="메쉬를설정한다" arg1="5001-5005" arg2="1" arg3="0" arg4="0" arg5="0"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return npc등장연출_4()


class npc등장연출_4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[310004], arg2=False)
        # <action name="메쉬를설정한다" arg1="5001-5005" arg2="1" arg3="0" arg4="0" arg5="0"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라리셋_2()


class 카메라리셋_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000002], returnView=True)
        # <action name="SetDirectionalLight" arg1="193, 180, 137" arg2="100,100,100"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1600):
            return 자기장생성()

    def on_exit(self):
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)


class 자기장생성(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[300002])
        destroy_monster(spawnIds=[310001])
        destroy_monster(spawnIds=[310002])
        destroy_monster(spawnIds=[310003])
        destroy_monster(spawnIds=[310004])
        # <action name="버프를걸어준다" arg1="102" arg2="70000102" arg3="1" />
        set_mesh(triggerIds=[5001,5002,5003,5004,5005], visible=False, arg3=0, arg4=0, arg5=0)
        set_effect(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=False)
        # <action name="이펙트를설정한다" arg1="71001-71016" arg2="1" />
        set_effect(triggerIds=[72001,72002,72003,72004,72005,72006,72007,72008,72009,72010,72011,72012], visible=True)
        set_effect(triggerIds=[73001,73002,73003,73004,73005,73006,73007,73008,73009,73010,73011,73012], visible=True)
        set_ambient_light(primary=[180,180,149])
        set_directional_light(diffuseColor=[219,204,182], specularColor=[219,204,182])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 대화_놀람()


class 대화_놀람(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='아앗! 오스칼과 레드아이, 알론... 그리고 레논?', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 몬스터등장_2()


class 몬스터등장_2(state.State):
    def on_enter(self):
        set_portal(portalId=96, visible=True, enabled=True)
        set_user_value(triggerId=905, key='respawn_phase_2', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터등장_2_2()


class 몬스터등장_2_2(state.State):
    def on_enter(self):
        set_user_value(triggerId=906, key='respawn_phase_2', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터등장_2_3()


class 몬스터등장_2_3(state.State):
    def on_enter(self):
        set_user_value(triggerId=907, key='respawn_phase_2', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 몬스터등장_2_4()


class 몬스터등장_2_4(state.State):
    def on_enter(self):
        set_user_value(triggerId=908, key='respawn_phase_2', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 몬스터사망_1()


class 몬스터사망_1(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 시간종료_3()


class 시간종료_3(state.State):
    def on_enter(self):
        set_ambient_light(primary=[0,0,0])
        set_directional_light(diffuseColor=[193,180,137], specularColor=[100,100,100])
        set_conversation(type=1, spawnId=0, script='모두들...어디로 사라진거야?', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 불꺼짐_2()


class 불꺼짐_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000003], returnView=False)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=1)
        # <action name="연출UI를설정한다" arg1="3"/>
        # <action name="연출UI를설정한다" arg1="1"/>
        # <action name="SetAmbientLight" arg1="0, 0, 0"/>
        # <action name="SetDirectionalLight" arg1="0, 0, 0" arg2="0,0,0"/>

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 몬스터등장_3()

    def on_exit(self):
        set_conversation(type=2, spawnId=4000201, script='자...기대하세요!', arg4=5)
        set_skip(state=몬스터등장_3)


class 몬스터등장_3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[72001,72002,72003,72004,72005,72006,72007,72008,72009,72010,72011,72012], visible=False)
        set_mesh(triggerIds=[5104], visible=False, arg3=0, arg4=0, arg5=0)
        set_conversation(type=1, spawnId=0, script='여기서 쓰러질 순 없어!', arg4=3, arg5=0)
        set_user_value(triggerId=909, key='respawn_phase_3', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2500):
            return 카메라리셋_3()


class 카메라리셋_3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[2000003], returnView=True)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이동_3()


class 이동_3(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 이동_4()

    def on_exit(self):
        set_ambient_light(primary=[180,180,149])
        set_directional_light(diffuseColor=[219,204,182], specularColor=[219,204,182])


class 이동_4(state.State):
    def on_enter(self):
        set_effect(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=True)
        set_mesh(triggerIds=[5001,5002,5003,5004,5005], visible=True, arg3=0, arg4=0, arg5=0)
        set_conversation(type=1, spawnId=0, script='아니! 이 녀석들은??!!', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None


