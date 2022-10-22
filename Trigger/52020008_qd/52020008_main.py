""" trigger/52020008_qd/52020008_main.xml """
from common import *
import state


class 감지(state.State):
    def on_enter(self):
        set_skill(triggerIds=[9991], isEnable=False)
        set_visible_breakable_object(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009], arg2=False)
        set_visible_breakable_object(triggerIds=[6001,6002], arg2=False)
        set_visible_breakable_object(triggerIds=[7001,7002], arg2=False)
        set_breakable(triggerIds=[6001,6002], enabled=False)
        set_breakable(triggerIds=[7001,7002], enabled=False)
        set_portal(portalId=1, visible=False, enabled=False)
        set_agent(triggerIds=[9001], visible=True)
        set_agent(triggerIds=[9002], visible=True)
        set_agent(triggerIds=[9003], visible=True)
        set_agent(triggerIds=[9004], visible=True)
        set_agent(triggerIds=[9005], visible=True)
        set_agent(triggerIds=[9006], visible=True)
        set_agent(triggerIds=[9007], visible=True)
        set_agent(triggerIds=[9008], visible=True)
        set_agent(triggerIds=[9009], visible=True)
        set_agent(triggerIds=[9010], visible=True)
        set_agent(triggerIds=[9011], visible=True)
        set_agent(triggerIds=[9012], visible=True)
        set_agent(triggerIds=[9013], visible=True)
        set_agent(triggerIds=[9014], visible=True)
        set_agent(triggerIds=[9015], visible=True)
        set_agent(triggerIds=[9016], visible=True)
        set_agent(triggerIds=[9017], visible=True)
        set_agent(triggerIds=[9018], visible=True)
        set_agent(triggerIds=[9019], visible=True)
        set_agent(triggerIds=[9020], visible=True)
        set_agent(triggerIds=[9021], visible=True)
        set_agent(triggerIds=[9022], visible=True)
        set_agent(triggerIds=[9023], visible=True)
        set_agent(triggerIds=[9024], visible=True)
        set_agent(triggerIds=[9025], visible=True)
        set_agent(triggerIds=[9026], visible=True)
        set_agent(triggerIds=[9027], visible=True)
        set_agent(triggerIds=[9028], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 연출카메라1()


class 연출카메라1(state.State):
    def on_enter(self):
        set_scene_skip(state=연출종료, arg2='exit')
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False, arg3=30000)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=503, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출카메라1_세리하대사1()


class 연출카메라1_세리하대사1(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003660, script='왕녀는 내가 잘 모실테니 이제 항복하시지?', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출카메라1_크란츠대사1()


class 연출카메라1_크란츠대사1(state.State):
    def on_enter(self):
        select_camera(triggerId=504, enable=True)
        set_conversation(type=2, spawnId=11003675, script='아름답지 않은 시중을 받을 생각은 없다!!', arg4=3)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출카메라1_PC대사1()


class 연출카메라1_PC대사1(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)
        set_conversation(type=1, spawnId=0, script='저녀석은 흑성회의 일원이야! 조심해!', arg4=3)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Troubled_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출카메라1_이오네대사1()


class 연출카메라1_이오네대사1(state.State):
    def on_enter(self):
        select_camera(triggerId=505, enable=True)
        set_conversation(type=2, spawnId=11003674, script='시커먼 속내를 가진 건 메이플 연합도 마찬가지 아닌가요? \n크리티아스의 힘은 누구에게도 이용당하게 두지 않겠어요!', arg4=5)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 연출카메라1_세리하대사2()


class 연출카메라1_세리하대사2(state.State):
    def on_enter(self):
        select_camera(triggerId=503, enable=True)
        set_conversation(type=2, spawnId=11003660, script='그 말이 맞는 것 같네?\n세상에 진짜 선과 악은 없는 법이지~', arg4=3)
        set_npc_emotion_sequence(spawnId=103, sequenceName='Bore_B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출카메라1_흑성회등장()


class 연출카메라1_흑성회등장(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)
        set_conversation(type=2, spawnId=11003660, script='이제 어떻게 하실려나?', arg4=3)
        create_monster(spawnIds=[201,202,203,204,205,206,207], arg2=False)
        create_monster(spawnIds=[104,105,106], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출카메라1_탈출장치()


class 연출카메라1_탈출장치(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11003675, script='이오네님 준비하시죠!', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 연출카메라1_벽부수기세팅()


class 연출카메라1_벽부수기세팅(state.State):
    def on_enter(self):
        select_camera(triggerId=507, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출카메라1_레지스탕스등장()


class 연출카메라1_레지스탕스등장(state.State):
    def on_enter(self):
        set_skill(triggerIds=[9991], isEnable=True)
        set_npc_rotation(spawnId=103, rotation=270)
        destroy_monster(spawnIds=[101,102])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출카메라1_체키대사1()


class 연출카메라1_체키대사1(state.State):
    def on_enter(self):
        select_camera(triggerId=502, enable=True)
        set_conversation(type=2, spawnId=11003661, script='아이고 오늘 정모날인가?', arg4=3)
        set_npc_emotion_sequence(spawnId=104, sequenceName='Bore_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출카메라1_세리하대사3()


class 연출카메라1_세리하대사3(state.State):
    def on_enter(self):
        select_camera(triggerId=504, enable=True)
        set_visible_breakable_object(triggerIds=[6001,6002], arg2=True)
        set_visible_breakable_object(triggerIds=[7001,7002], arg2=True)
        set_breakable(triggerIds=[6001,6002], enabled=True)
        set_breakable(triggerIds=[7001,7002], enabled=True)
        face_emotion(spawnId=103, emotionName='Trigger_bore1')
        set_conversation(type=2, spawnId=11003660, script='아으... 귀찮아.', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 연출카메라1_세리하대사4()


class 연출카메라1_세리하대사4(state.State):
    def on_enter(self):
        init_npc_rotation(spawnIds=[103])
        face_emotion(spawnId=103, emotionName='Trigger_bore2')
        set_conversation(type=2, spawnId=11003660, script='왕녀는 또 어디갔어!! 환장하겠네!!', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출카메라1_체키대사2()


class 연출카메라1_체키대사2(state.State):
    def on_enter(self):
        select_camera(triggerId=502, enable=True)
        set_visible_breakable_object(triggerIds=[6001,6002], arg2=False)
        set_visible_breakable_object(triggerIds=[7001,7002], arg2=False)
        set_breakable(triggerIds=[6001,6002], enabled=False)
        set_breakable(triggerIds=[7001,7002], enabled=False)
        set_conversation(type=2, spawnId=11003661, script='왕녀는 우리가 접수하겠다. 얘들아 처리해라!', arg4=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출카메라1_체키대사3()


class 연출카메라1_체키대사3(state.State):
    def on_enter(self):
        set_npc_rotation(spawnId=104, rotation=180)
        set_npc_rotation(spawnId=105, rotation=180)
        set_npc_rotation(spawnId=106, rotation=180)
        set_conversation(type=2, spawnId=11003661, script='어서 움직이자!', arg4=3)
        move_npc(spawnId=104, patrolName='MS2PatrolData_Chekky')
        move_npc(spawnId=105, patrolName='MS2PatrolData_Jigmunt')
        move_npc(spawnId=106, patrolName='MS2PatrolData_Henryte')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출카메라1_세리하대사5()


class 연출카메라1_세리하대사5(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)
        set_conversation(type=1, spawnId=103, script='하늘로 솟은거야?? 탑 위에 뭐가 있나 봐야겠어!!', arg4=3)
        move_npc(spawnId=103, patrolName='MS2PatrolData_Seriha')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출종료()


class 연출종료(state.State):
    def on_enter(self):
        set_skill(triggerIds=[9991], isEnable=True)
        set_visible_breakable_object(triggerIds=[6001,6002], arg2=False)
        set_visible_breakable_object(triggerIds=[7001,7002], arg2=False)
        set_breakable(triggerIds=[6001,6002], enabled=False)
        set_breakable(triggerIds=[7001,7002], enabled=False)
        destroy_monster(spawnIds=[-1])
        set_visible_breakable_object(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009], arg2=False)
        set_breakable(triggerIds=[5001,5002,5003,5004,5005,5006,5007,5008,5009], enabled=False)
        reset_camera(interpolationTime=0.1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_agent(triggerIds=[9001], visible=False)
        set_agent(triggerIds=[9002], visible=False)
        set_agent(triggerIds=[9003], visible=False)
        set_agent(triggerIds=[9004], visible=False)
        set_agent(triggerIds=[9005], visible=False)
        set_agent(triggerIds=[9006], visible=False)
        set_agent(triggerIds=[9007], visible=False)
        set_agent(triggerIds=[9008], visible=False)
        set_agent(triggerIds=[9009], visible=False)
        set_agent(triggerIds=[9010], visible=False)
        set_agent(triggerIds=[9011], visible=False)
        set_agent(triggerIds=[9012], visible=False)
        set_agent(triggerIds=[9013], visible=False)
        set_agent(triggerIds=[9014], visible=False)
        set_agent(triggerIds=[9015], visible=False)
        set_agent(triggerIds=[9016], visible=False)
        set_agent(triggerIds=[9017], visible=False)
        set_agent(triggerIds=[9018], visible=False)
        set_agent(triggerIds=[9019], visible=False)
        set_agent(triggerIds=[9020], visible=False)
        set_agent(triggerIds=[9021], visible=False)
        set_agent(triggerIds=[9022], visible=False)
        set_agent(triggerIds=[9023], visible=False)
        set_agent(triggerIds=[9024], visible=False)
        set_agent(triggerIds=[9025], visible=False)
        set_agent(triggerIds=[9026], visible=False)
        set_agent(triggerIds=[9027], visible=False)
        set_agent(triggerIds=[9028], visible=False)

    def on_tick(self) -> state.State:
        if true():
            return NPC생성()


class NPC생성(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='세리하를 추적하세요.', arg3='5000')
        create_monster(spawnIds=[211,212,213,214,215,216,217])

    def on_tick(self) -> state.State:
        if true():
            return 전투시작()


class 전투시작(state.State):
    def on_enter(self):
        move_npc(spawnId=216, patrolName='MS2PatrolData_Robot_B')
        move_npc(spawnId=217, patrolName='MS2PatrolData_Robot_A')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[902]):
            return 계단전투1()


class 계단전투1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[221], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[903]):
            return 계단전투2()


class 계단전투2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[222], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[211,212,213,214,215,216,217,221,222]):
            return 포탈활성화()


class 포탈활성화(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


