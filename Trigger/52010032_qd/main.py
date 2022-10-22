""" trigger/52010032_qd/main.xml """
from common import *
import state


#  치유의 숲 : 52010032  
#  들어오자마자 앉아있는 상태 연출 
class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=True) # 퀘스트 나메드: 11000039
        set_effect(triggerIds=[5001], visible=False) # 나메드 치유 시전 이펙트
        set_effect(triggerIds=[5002], visible=False) # 붉은 늑대의 심장 치유 이펙트

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[10003090], questStates=[1]):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera_path(pathIds=[4001], returnView=False)
        move_user(mapId=52010032, portalId=7001)
        create_monster(spawnIds=[201], arg2=True) # 나메드:

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 치유의식_01()


class 치유의식_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN__0$', duration=3000, illustId='0', align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 치유의식_02()


class 치유의식_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4002,4003], returnView=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_3001')
        move_user_path(patrolName='MS2PatrolData_3002')
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN__1$', duration=3000, illustId='0', align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 치유의식_03()


class 치유의식_03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_B')
        set_effect(triggerIds=[5001], visible=True)
        set_pc_emotion_sequence(sequenceNames=['Emotion_Cry_A'])
        add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN__2$', duration=3000, illustId='0', align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 치유의식_04()


class 치유의식_04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 치유의식_05()


class 치유의식_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003390, msg='$52010032_QD__MAIN__3$', duration=3000, illustId='0', align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return None # Missing State: 의식종료_01


class 의식종료01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None # Missing State: 의식종료_02


class 의식종료02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


