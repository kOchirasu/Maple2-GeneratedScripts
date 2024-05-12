""" trigger/52020008_qd/52020008_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[9991], enable=False)
        self.set_visible_breakable_object(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009], visible=False)
        self.set_visible_breakable_object(triggerIds=[6001,6002], visible=False)
        self.set_visible_breakable_object(triggerIds=[7001,7002], visible=False)
        self.set_breakable(triggerIds=[6001,6002], enable=False)
        self.set_breakable(triggerIds=[7001,7002], enable=False)
        self.set_portal(portalId=1, visible=False, enable=False)
        self.set_agent(triggerIds=[9001], visible=True)
        self.set_agent(triggerIds=[9002], visible=True)
        self.set_agent(triggerIds=[9003], visible=True)
        self.set_agent(triggerIds=[9004], visible=True)
        self.set_agent(triggerIds=[9005], visible=True)
        self.set_agent(triggerIds=[9006], visible=True)
        self.set_agent(triggerIds=[9007], visible=True)
        self.set_agent(triggerIds=[9008], visible=True)
        self.set_agent(triggerIds=[9009], visible=True)
        self.set_agent(triggerIds=[9010], visible=True)
        self.set_agent(triggerIds=[9011], visible=True)
        self.set_agent(triggerIds=[9012], visible=True)
        self.set_agent(triggerIds=[9013], visible=True)
        self.set_agent(triggerIds=[9014], visible=True)
        self.set_agent(triggerIds=[9015], visible=True)
        self.set_agent(triggerIds=[9016], visible=True)
        self.set_agent(triggerIds=[9017], visible=True)
        self.set_agent(triggerIds=[9018], visible=True)
        self.set_agent(triggerIds=[9019], visible=True)
        self.set_agent(triggerIds=[9020], visible=True)
        self.set_agent(triggerIds=[9021], visible=True)
        self.set_agent(triggerIds=[9022], visible=True)
        self.set_agent(triggerIds=[9023], visible=True)
        self.set_agent(triggerIds=[9024], visible=True)
        self.set_agent(triggerIds=[9025], visible=True)
        self.set_agent(triggerIds=[9026], visible=True)
        self.set_agent(triggerIds=[9027], visible=True)
        self.set_agent(triggerIds=[9028], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 연출카메라1(self.ctx)


class 연출카메라1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=연출종료, action='exit')
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.create_monster(spawnIds=[103], animationEffect=False, animationDelay=30000)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=503, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출카메라1_세리하대사1(self.ctx)


class 연출카메라1_세리하대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003660, script='왕녀는 내가 잘 모실테니 이제 항복하시지?', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출카메라1_크란츠대사1(self.ctx)


class 연출카메라1_크란츠대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=504, enable=True)
        self.set_conversation(type=2, spawnId=11003675, script='아름답지 않은 시중을 받을 생각은 없다!!', arg4=3)
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출카메라1_PC대사1(self.ctx)


class 연출카메라1_PC대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=501, enable=True)
        self.set_conversation(type=1, spawnId=0, script='저녀석은 흑성회의 일원이야! 조심해!', arg4=3)
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Troubled_A'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출카메라1_이오네대사1(self.ctx)


class 연출카메라1_이오네대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=505, enable=True)
        self.set_conversation(type=2, spawnId=11003674, script='시커먼 속내를 가진 건 메이플 연합도 마찬가지 아닌가요? \\n크리티아스의 힘은 누구에게도 이용당하게 두지 않겠어요!', arg4=5)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 연출카메라1_세리하대사2(self.ctx)


class 연출카메라1_세리하대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=503, enable=True)
        self.set_conversation(type=2, spawnId=11003660, script='그 말이 맞는 것 같네?\\n세상에 진짜 선과 악은 없는 법이지~', arg4=3)
        self.set_npc_emotion_sequence(spawnId=103, sequenceName='Bore_B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출카메라1_흑성회등장(self.ctx)


class 연출카메라1_흑성회등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=501, enable=True)
        self.set_conversation(type=2, spawnId=11003660, script='이제 어떻게 하실려나?', arg4=3)
        self.create_monster(spawnIds=[201,202,203,204,205,206,207], animationEffect=False)
        self.create_monster(spawnIds=[104,105,106], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출카메라1_탈출장치(self.ctx)


class 연출카메라1_탈출장치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11003675, script='이오네님 준비하시죠!', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 연출카메라1_벽부수기세팅(self.ctx)


class 연출카메라1_벽부수기세팅(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=507, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출카메라1_레지스탕스등장(self.ctx)


class 연출카메라1_레지스탕스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[9991], enable=True)
        self.set_npc_rotation(spawnId=103, rotation=270)
        self.destroy_monster(spawnIds=[101,102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출카메라1_체키대사1(self.ctx)


class 연출카메라1_체키대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=502, enable=True)
        self.set_conversation(type=2, spawnId=11003661, script='아이고 오늘 정모날인가?', arg4=3)
        self.set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출카메라1_세리하대사3(self.ctx)


class 연출카메라1_세리하대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=504, enable=True)
        self.set_visible_breakable_object(triggerIds=[6001,6002], visible=True)
        self.set_visible_breakable_object(triggerIds=[7001,7002], visible=True)
        self.set_breakable(triggerIds=[6001,6002], enable=True)
        self.set_breakable(triggerIds=[7001,7002], enable=True)
        self.face_emotion(spawnId=103, emotionName='Trigger_bore1')
        self.set_conversation(type=2, spawnId=11003660, script='아으... 귀찮아.', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 연출카메라1_세리하대사4(self.ctx)


class 연출카메라1_세리하대사4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.init_npc_rotation(spawnIds=[103])
        self.face_emotion(spawnId=103, emotionName='Trigger_bore2')
        self.set_conversation(type=2, spawnId=11003660, script='왕녀는 또 어디갔어!! 환장하겠네!!', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출카메라1_체키대사2(self.ctx)


class 연출카메라1_체키대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=502, enable=True)
        self.set_visible_breakable_object(triggerIds=[6001,6002], visible=False)
        self.set_visible_breakable_object(triggerIds=[7001,7002], visible=False)
        self.set_breakable(triggerIds=[6001,6002], enable=False)
        self.set_breakable(triggerIds=[7001,7002], enable=False)
        self.set_conversation(type=2, spawnId=11003661, script='왕녀는 우리가 접수하겠다. 얘들아 처리해라!', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출카메라1_체키대사3(self.ctx)


class 연출카메라1_체키대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_rotation(spawnId=104, rotation=180)
        self.set_npc_rotation(spawnId=105, rotation=180)
        self.set_npc_rotation(spawnId=106, rotation=180)
        self.set_conversation(type=2, spawnId=11003661, script='어서 움직이자!', arg4=3)
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_Chekky')
        self.move_npc(spawnId=105, patrolName='MS2PatrolData_Jigmunt')
        self.move_npc(spawnId=106, patrolName='MS2PatrolData_Henryte')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 연출카메라1_세리하대사5(self.ctx)


class 연출카메라1_세리하대사5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=501, enable=True)
        self.set_conversation(type=1, spawnId=103, script='하늘로 솟은거야?? 탑 위에 뭐가 있나 봐야겠어!!', arg4=3)
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_Seriha')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[9991], enable=True)
        self.set_visible_breakable_object(triggerIds=[6001,6002], visible=False)
        self.set_visible_breakable_object(triggerIds=[7001,7002], visible=False)
        self.set_breakable(triggerIds=[6001,6002], enable=False)
        self.set_breakable(triggerIds=[7001,7002], enable=False)
        self.destroy_monster(spawnIds=[-1])
        self.set_visible_breakable_object(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009], visible=False)
        self.set_breakable(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009], enable=False)
        self.reset_camera(interpolationTime=0.1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_agent(triggerIds=[9001], visible=False)
        self.set_agent(triggerIds=[9002], visible=False)
        self.set_agent(triggerIds=[9003], visible=False)
        self.set_agent(triggerIds=[9004], visible=False)
        self.set_agent(triggerIds=[9005], visible=False)
        self.set_agent(triggerIds=[9006], visible=False)
        self.set_agent(triggerIds=[9007], visible=False)
        self.set_agent(triggerIds=[9008], visible=False)
        self.set_agent(triggerIds=[9009], visible=False)
        self.set_agent(triggerIds=[9010], visible=False)
        self.set_agent(triggerIds=[9011], visible=False)
        self.set_agent(triggerIds=[9012], visible=False)
        self.set_agent(triggerIds=[9013], visible=False)
        self.set_agent(triggerIds=[9014], visible=False)
        self.set_agent(triggerIds=[9015], visible=False)
        self.set_agent(triggerIds=[9016], visible=False)
        self.set_agent(triggerIds=[9017], visible=False)
        self.set_agent(triggerIds=[9018], visible=False)
        self.set_agent(triggerIds=[9019], visible=False)
        self.set_agent(triggerIds=[9020], visible=False)
        self.set_agent(triggerIds=[9021], visible=False)
        self.set_agent(triggerIds=[9022], visible=False)
        self.set_agent(triggerIds=[9023], visible=False)
        self.set_agent(triggerIds=[9024], visible=False)
        self.set_agent(triggerIds=[9025], visible=False)
        self.set_agent(triggerIds=[9026], visible=False)
        self.set_agent(triggerIds=[9027], visible=False)
        self.set_agent(triggerIds=[9028], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return NPC생성(self.ctx)


class NPC생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='세리하를 추적하세요.', arg3='5000')
        self.create_monster(spawnIds=[211,212,213,214,215,216,217])

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=216, patrolName='MS2PatrolData_Robot_B')
        self.move_npc(spawnId=217, patrolName='MS2PatrolData_Robot_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[902]):
            return 계단전투1(self.ctx)


class 계단전투1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[221], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[903]):
            return 계단전투2(self.ctx)


class 계단전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[222], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[211,212,213,214,215,216,217,221,222]):
            return 포탈활성화(self.ctx)


class 포탈활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 감지
