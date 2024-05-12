""" trigger/52000025_qd/main.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[202], animationEffect=False) # 렌듀비앙
        self.set_effect(triggerIds=[7001], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[20002235], questStates=[1], jobCode=90):
            return start(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[20002235], questStates=[2], jobCode=90):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[20002235], questStates=[3], jobCode=90):
            return start_B(self.ctx)


class start_B(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[202,299], animationEffect=False) # 이슈라 퀘스트
        self.destroy_monster(spawnIds=[203,204,205])


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[201,203,204], animationEffect=False) # 이슈라
        self.create_monster(spawnIds=[101,102], animationEffect=False) # 적 몬스터 1차

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102]):
            return start_02(self.ctx)

    def on_exit(self) -> None:
        self.set_conversation(type=1, spawnId=201, script='$52000025_QD__MAIN__0$', arg4=2, arg5=1)


class start_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[111,112,113,114,115,116], animationEffect=False) # 적 몬스터 2차
        self.set_conversation(type=1, spawnId=201, script='$52000025_QD__MAIN__1$', arg4=2, arg5=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[111,112,113,114,115,116]):
            return start_03(self.ctx)


class start_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001244, script='$52000025_QD__MAIN__2$', arg4=4) # 음성 코드 00001288
        self.set_effect(triggerIds=[7001], visible=True) # 음성 코드 00001288

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_04(self.ctx)


class start_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2000') # 이슈라를 이동시킨다
        self.set_conversation(type=2, spawnId=11001244, script='$52000025_QD__MAIN__3$', arg4=6) # 음성 코드 00001289
        self.set_effect(triggerIds=[7004], visible=True) # 음성 코드 00001289

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return start_05(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=4)


class start_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[203,204,205])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Start_06(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52000025, portalId=99)


class Start_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2001') # 이슈라를 이동시킨다
        self.move_user_path(patrolName='MS2PatrolData_2002') # 유저를 이동시킨다
        self.select_camera_path(pathIds=[8001,8002], returnView=False) # 카메라 뒤로 당김

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Start_07(self.ctx)


class Start_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001575, script='$52000025_QD__MAIN__4$', arg4=3) # 렌듀비앙 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return Start_08(self.ctx)


class Start_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001244, script='$52000025_QD__MAIN__5$', arg4=5)
        self.set_effect(triggerIds=[7002], visible=True) # 음성 코드 00001290

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return Start_09(self.ctx)


class Start_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001575, script='$52000025_QD__MAIN__6$', arg4=4) # 렌듀비앙 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Start_10(self.ctx)


class Start_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001575, script='$52000025_QD__MAIN__7$', arg4=3) # 렌듀비앙 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return Start_11(self.ctx)

    def on_exit(self) -> None:
        # self.select_camera_path(pathIds=[8001], returnView=False)
        # 카메라 뒤로 당김
        self.select_camera(triggerId=8001, enable=False)
        # 카메라 초기화


class Start_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[201]) # 이슈라
        self.create_monster(spawnIds=[299], animationEffect=False) # 이슈라 퀘스트
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(triggerId=701, type='trigger', achieve='SweepthePriates')


initial_state = idle
