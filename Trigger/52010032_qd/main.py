""" trigger/52010032_qd/main.xml """
import common


# 치유의 숲 : 52010032
# 들어오자마자 앉아있는 상태 연출
class idle(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202], animationEffect=True) # 퀘스트 나메드: 11000039
        self.set_effect(triggerIds=[5001], visible=False) # 나메드 치유 시전 이펙트
        self.set_effect(triggerIds=[5002], visible=False) # 붉은 늑대의 심장 치유 이펙트

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[10003090], questStates=[1]):
            return Ready(self.ctx)


class Ready(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera_path(pathIds=[4001], returnView=False)
        self.move_user(mapId=52010032, portalId=7001)
        self.create_monster(spawnIds=[201], animationEffect=True) # 나메드:

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 치유의식_01(self.ctx)


class 치유의식_01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN__0$', duration=3000, illustId='0', align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 치유의식_02(self.ctx)


class 치유의식_02(common.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4002,4003], returnView=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_3001')
        self.move_user_path(patrolName='MS2PatrolData_3002')
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN__1$', duration=3000, illustId='0', align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 치유의식_03(self.ctx)


class 치유의식_03(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Bore_B')
        self.set_effect(triggerIds=[5001], visible=True)
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Cry_A'])
        self.add_cinematic_talk(npcId=11003389, msg='$52010032_QD__MAIN__2$', duration=3000, illustId='0', align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 치유의식_04(self.ctx)


class 치유의식_04(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_effect(triggerIds=[5002], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 치유의식_05(self.ctx)


class 치유의식_05(common.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003390, msg='$52010032_QD__MAIN__3$', duration=3000, illustId='0', align='Left')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return None # Missing State: 의식종료_01


class 의식종료01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: 의식종료_02


class 의식종료02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
