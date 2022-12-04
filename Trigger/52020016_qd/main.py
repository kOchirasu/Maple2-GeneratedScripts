""" trigger/52020016_qd/main.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=95, visible=False, enable=False)
        self.set_portal(portalId=96, visible=False, enable=False)
        self.set_effect(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=False)
        self.set_mesh(triggerIds=[5001,5002,5003,5004,5005], visible=False, arg3=0, delay=0, scale=0)
        # <action name="이펙트를설정한다" arg1="71001-71016" arg2="0" />
        self.set_effect(triggerIds=[72001,72002,72003,72004,72005,72006,72007,72008,72009,72010,72011,72012], visible=False)
        self.set_effect(triggerIds=[73001,73002,73003,73004,73005,73006,73007,73008,73009,73010,73011,73012], visible=False)
        self.set_mesh(triggerIds=[5103,5104], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 시작_2(self.ctx)


class 시작_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.select_camera_path(pathIds=[2000004], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시작_2_2(self.ctx)


class 시작_2_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=0, script='이곳은 뭐하는 곳이지?!', arg4=3, arg5=0)
        self.set_conversation(type=2, spawnId=0, script='미카엘의 기운이 느껴지고 있어!\n서둘러야 해!!', arg4=3, arg5=0)
        self.set_skip(state=시작_3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 시작_3(self.ctx)


class 시작_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000004], returnView=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 시작_4(self.ctx)


class 시작_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.set_conversation(type=1, spawnId=0, script='한번 가볼까?', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 인트로(self.ctx)


class 인트로(trigger_api.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[0,0,0])
        self.set_directional_light(diffuseColor=[0,0,0], specularColor=[0,0,0])
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.set_pc_emotion_loop(sequenceName='Stun_A', duration=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return 인트로_2(self.ctx)


class 인트로_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=0, script='???!!!', arg4=2, arg5=0)
        self.set_conversation(type=2, spawnId=0, script='뭐야!!\n앞이 안보여!!', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 인트로_3(self.ctx)


class 인트로_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 미카엘등장(self.ctx)


class 미카엘등장(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000001], returnView=False)
        self.create_monster(spawnIds=[300001], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 미카엘_이동_1(self.ctx)


class 미카엘_이동_1(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=300001, patrolName='MS2PatrolData0_300001_0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대화_1(self.ctx)


class 대화_1(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=300001, script='오호...여기까지 오다니...놀랍군요..', arg4=5)
        self.set_conversation(type=2, spawnId=300001, script='자...그럼 본격적으로 놀아볼까요?', arg4=5)
        self.set_skip(state=카메라리셋_1)
        self.set_mesh(triggerIds=[5001,5002,5003,5004,5005], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 카메라리셋_1(self.ctx)


class 카메라리셋_1(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000001], returnView=True)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)
        self.destroy_monster(spawnIds=[300001])
        # <action name="버프를걸어준다" arg1="102" arg2="70000102" arg3="1" />
        self.set_effect(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이동_1(self.ctx)


class 이동_1(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=52020016, portalId=90)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 전투페이즈_1(self.ctx)

    def on_exit(self):
        self.set_ambient_light(primary=[180,180,149])
        self.set_directional_light(diffuseColor=[219,204,182], specularColor=[219,204,182])
        self.set_portal(portalId=95, visible=True, enable=True)
        self.set_conversation(type=1, spawnId=0, script='갇혀 버렸어!', arg4=3, arg5=0)


class 전투페이즈_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 전투종료(self.ctx)

    def on_exit(self):
        self.set_event_ui(type=1, arg2='미카엘이 조종하는 마리오네트 무리들을 처치하세요.', arg3='4000')
        self.shadow_expedition(type='OpenBossGauge', maxGaugePoint=300, title='몬스터 처치 달성')
        self.set_user_value(triggerId=901, key='respawn_phase_1', value=1)
        self.set_user_value(triggerId=902, key='respawn_phase_1', value=1)
        self.set_user_value(triggerId=903, key='respawn_phase_1', value=1)
        self.set_user_value(triggerId=904, key='respawn_phase_1', value=1)


class 전투종료(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.shadow_expedition_reach_point(point=300):
            return 페이즈_2_준비(self.ctx)


class 페이즈_2_준비(trigger_api.Trigger):
    def on_enter(self):
        self.shadow_expedition(type='CloseBossGauge')
        self.set_user_value(triggerId=901, key='respawn_phase_1_end', value=1)
        self.set_user_value(triggerId=902, key='respawn_phase_1_end', value=1)
        self.set_user_value(triggerId=903, key='respawn_phase_1_end', value=1)
        self.set_user_value(triggerId=904, key='respawn_phase_1_end', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 불꺼짐(self.ctx)


class 불꺼짐(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=95, visible=False, enable=False)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        self.set_ambient_light(primary=[0,0,0])
        self.set_directional_light(diffuseColor=[0,0,0], specularColor=[0,0,0])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 미카엘등장_2(self.ctx)


class 미카엘등장_2(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000002], returnView=False)
        self.create_monster(spawnIds=[300002], animationEffect=False)
        self.move_npc(spawnId=300002, patrolName='MS2PatrolData0_300002_1')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 대화_2(self.ctx)


class 대화_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=300002, script='음... 기대 이상인데요?', arg4=5)
        self.set_conversation(type=2, spawnId=300002, script='이번엔 이분들이 당신과 놀아줄겁니다!!', arg4=5)
        self.move_user(mapId=52020016, portalId=91)
        self.set_skip(state=카메라리셋_2)
        self.set_mesh(triggerIds=[5103,5104], visible=True, arg3=0, delay=0, scale=0)
        # <action name="메쉬를설정한다" arg1="5001-5005" arg2="1" arg3="0" arg4="0" arg5="0"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return npc등장연출_1(self.ctx)


class npc등장연출_1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[310001], animationEffect=False)
        # <action name="메쉬를설정한다" arg1="5001-5005" arg2="1" arg3="0" arg4="0" arg5="0"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return npc등장연출_2(self.ctx)


class npc등장연출_2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[310002], animationEffect=False)
        # <action name="메쉬를설정한다" arg1="5001-5005" arg2="1" arg3="0" arg4="0" arg5="0"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return npc등장연출_3(self.ctx)


class npc등장연출_3(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[310003], animationEffect=False)
        # <action name="메쉬를설정한다" arg1="5001-5005" arg2="1" arg3="0" arg4="0" arg5="0"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return npc등장연출_4(self.ctx)


class npc등장연출_4(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[310004], animationEffect=False)
        # <action name="메쉬를설정한다" arg1="5001-5005" arg2="1" arg3="0" arg4="0" arg5="0"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라리셋_2(self.ctx)


class 카메라리셋_2(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000002], returnView=True)
        # <action name="SetDirectionalLight" arg1="193, 180, 137" arg2="100,100,100"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1600):
            return 자기장생성(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)


class 자기장생성(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[300002])
        self.destroy_monster(spawnIds=[310001])
        self.destroy_monster(spawnIds=[310002])
        self.destroy_monster(spawnIds=[310003])
        self.destroy_monster(spawnIds=[310004])
        # <action name="버프를걸어준다" arg1="102" arg2="70000102" arg3="1" />
        self.set_mesh(triggerIds=[5001,5002,5003,5004,5005], visible=False, arg3=0, delay=0, scale=0)
        self.set_effect(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=False)
        # <action name="이펙트를설정한다" arg1="71001-71016" arg2="1" />
        self.set_effect(triggerIds=[72001,72002,72003,72004,72005,72006,72007,72008,72009,72010,72011,72012], visible=True)
        self.set_effect(triggerIds=[73001,73002,73003,73004,73005,73006,73007,73008,73009,73010,73011,73012], visible=True)
        self.set_ambient_light(primary=[180,180,149])
        self.set_directional_light(diffuseColor=[219,204,182], specularColor=[219,204,182])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 대화_놀람(self.ctx)


class 대화_놀람(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='아앗! 오스칼과 레드아이, 알론... 그리고 레논?', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 몬스터등장_2(self.ctx)


class 몬스터등장_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=96, visible=True, enable=True)
        self.set_user_value(triggerId=905, key='respawn_phase_2', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터등장_2_2(self.ctx)


class 몬스터등장_2_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=906, key='respawn_phase_2', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터등장_2_3(self.ctx)


class 몬스터등장_2_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=907, key='respawn_phase_2', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터등장_2_4(self.ctx)


class 몬스터등장_2_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=908, key='respawn_phase_2', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 몬스터사망_1(self.ctx)


class 몬스터사망_1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 시간종료_3(self.ctx)


class 시간종료_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[0,0,0])
        self.set_directional_light(diffuseColor=[193,180,137], specularColor=[100,100,100])
        self.set_conversation(type=1, spawnId=0, script='모두들...어디로 사라진거야?', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 불꺼짐_2(self.ctx)


class 불꺼짐_2(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000003], returnView=False)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=1)
        # <action name="연출UI를설정한다" arg1="3"/>
        # <action name="연출UI를설정한다" arg1="1"/>
        # <action name="SetAmbientLight" arg1="0, 0, 0"/>
        # <action name="SetDirectionalLight" arg1="0, 0, 0" arg2="0,0,0"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 몬스터등장_3(self.ctx)

    def on_exit(self):
        self.set_conversation(type=2, spawnId=4000201, script='자...기대하세요!', arg4=5)
        self.set_skip(state=몬스터등장_3)


class 몬스터등장_3(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[72001,72002,72003,72004,72005,72006,72007,72008,72009,72010,72011,72012], visible=False)
        self.set_mesh(triggerIds=[5104], visible=False, arg3=0, delay=0, scale=0)
        self.set_conversation(type=1, spawnId=0, script='여기서 쓰러질 순 없어!', arg4=3, arg5=0)
        self.set_user_value(triggerId=909, key='respawn_phase_3', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 카메라리셋_3(self.ctx)


class 카메라리셋_3(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[2000003], returnView=True)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이동_3(self.ctx)


class 이동_3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[104]):
            return 이동_4(self.ctx)

    def on_exit(self):
        self.set_ambient_light(primary=[180,180,149])
        self.set_directional_light(diffuseColor=[219,204,182], specularColor=[219,204,182])


class 이동_4(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[70001,70002,70003,70004,70005,70006,70007,70008,70009,70010,70011,70012,70013,70014,70015,70016,70017,70018,70019,70020,70021,70022,70023,70024], visible=True)
        self.set_mesh(triggerIds=[5001,5002,5003,5004,5005], visible=True, arg3=0, delay=0, scale=0)
        self.set_conversation(type=1, spawnId=0, script='아니! 이 녀석들은??!!', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return None


initial_state = 시작
