""" trigger/52000096_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001514], questStates=[1]):
            # 50001514 퀘스트 진행 중 상태!
            return 몹소환01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50100040], questStates=[1]):
            # 50100040 퀘스트 진행 중 상태!
            return 몹소환01(self.ctx)


class 몹소환01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.create_monster(spawnIds=[1001], animationEffect=False) # 몬스터 스폰포인트 1
        self.create_monster(spawnIds=[1002], animationEffect=False) # 몬스터 스폰포인트 2
        self.create_monster(spawnIds=[1003], animationEffect=False) # 몬스터 스폰포인트 3
        self.create_monster(spawnIds=[1004], animationEffect=False) # 몬스터 스폰포인트 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 위협당함01(self.ctx)


class 위협당함01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=1001, script='$52000096_QD__MAIN__0$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 위협당함02(self.ctx)


class 위협당함02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=1002, script='$52000096_QD__MAIN__1$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 위협당함03(self.ctx)


class 위협당함03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=1003, script='$52000096_QD__MAIN__2$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 위협당함04(self.ctx)


class 위협당함04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=1004, script='$52000096_QD__MAIN__3$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 시점이동(self.ctx)


class 시점이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 경로이동(self.ctx)


class 경로이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='$52000096_QD__MAIN__4$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 몹말풍선01(self.ctx)


class 몹말풍선01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=3)
        self.set_conversation(type=1, spawnId=1003, script='$52000096_QD__MAIN__5$', arg4=2, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_PC_01')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 몬스터재스폰(self.ctx)


class 몬스터재스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1001], animationEffect=True) # 몬스터 스폰포인트 1
        self.create_monster(spawnIds=[1002], animationEffect=True) # 몬스터 스폰포인트 2
        self.create_monster(spawnIds=[1003], animationEffect=True) # 몬스터 스폰포인트 3
        self.create_monster(spawnIds=[1004], animationEffect=True) # 몬스터 스폰포인트 4

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
