""" trigger/52000025_qd/main_etc.xml """
import common


class idle(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[7001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[701], questIds=[10002942], questStates=[1], jobCode=30):
            return start(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002942], questStates=[2], jobCode=30):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002942], questStates=[3], jobCode=30):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002951], questStates=[1], jobCode=40):
            return start(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002951], questStates=[2], jobCode=40):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002951], questStates=[3], jobCode=40):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002961], questStates=[1], jobCode=20):
            return start(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002961], questStates=[2], jobCode=20):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002961], questStates=[3], jobCode=20):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002971], questStates=[1], jobCode=50):
            return start(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002971], questStates=[2], jobCode=50):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002971], questStates=[3], jobCode=50):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002981], questStates=[1], jobCode=10):
            return start(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002981], questStates=[2], jobCode=10):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002981], questStates=[3], jobCode=10):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002981], questStates=[1], jobCode=1):
            return start(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002981], questStates=[2], jobCode=1):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002981], questStates=[3], jobCode=1):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002991], questStates=[1], jobCode=60):
            return start(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002991], questStates=[2], jobCode=60):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10002991], questStates=[3], jobCode=60):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003001], questStates=[1], jobCode=70):
            return start(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003001], questStates=[2], jobCode=70):
            return start_B(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[10003001], questStates=[3], jobCode=70):
            return start_B(self.ctx)


class start_B(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202,299], animationEffect=False) # 이슈라 퀘스트
        self.destroy_monster(spawnIds=[203,204,205])


class start(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201,203,204], animationEffect=False)
        self.create_monster(spawnIds=[101,102], animationEffect=False) # 적 몬스터 1차

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101,102]):
            return start_02(self.ctx)

    def on_exit(self):
        self.set_conversation(type=1, spawnId=201, script='$52000025_QD__MAIN_ETC__0$', arg4=2, arg5=1)


class start_02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[111,112,113,114,115,116], animationEffect=False) # 적 몬스터 2차
        self.set_conversation(type=1, spawnId=201, script='$52000025_QD__MAIN_ETC__1$', arg4=2, arg5=5)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[111,112,113,114,115,116]):
            return start_03(self.ctx)


class start_03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=11001244, script='$52000025_QD__MAIN_ETC__2$', arg4=4) # 음성 코드 00001288
        self.set_effect(triggerIds=[7001], visible=True) # 음성 코드 00001288

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_04(self.ctx)


class start_04(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2000') # 이슈라를 이동시킨다
        self.set_conversation(type=2, spawnId=11001244, script='$52000025_QD__MAIN_ETC__3$', arg4=3) # 음성 코드 00001306
        self.set_effect(triggerIds=[7003], visible=True) # 음성 코드 00001306

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return start_05(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=4)


class start_05(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[203,204,205])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Start_06(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52000025, portalId=99)


class Start_06(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_2001') # 이슈라를 이동시킨다
        self.move_user_path(patrolName='MS2PatrolData_2002') # 유저를 이동시킨다
        self.select_camera_path(pathIds=[8001,8002], returnView=False) # 카메라 뒤로 당김

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Start_07(self.ctx)


class Start_07(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001575, script='$52000025_QD__MAIN_ETC__4$', arg4=3) # 렌듀비앙 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Start_08(self.ctx)


class Start_08(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001244, script='$52000025_QD__MAIN_ETC__5$', arg4=5)
        self.set_effect(triggerIds=[7002], visible=True) # 음성 코드 00001290

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return Start_09(self.ctx)


class Start_09(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001575, script='$52000025_QD__MAIN_ETC__6$', arg4=4) # 렌듀비앙 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Start_10(self.ctx)


class Start_10(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001575, script='$52000025_QD__MAIN_ETC__7$', arg4=3) # 렌듀비앙 대사

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return Start_11(self.ctx)

    def on_exit(self):
        self.select_camera(triggerId=8001, enable=False) # 카메라 초기화


class Start_11(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201]) # 이슈라
        self.create_monster(spawnIds=[299], animationEffect=False) # 이슈라 퀘스트
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(triggerId=701, type='trigger', achieve='SweepthePriates')


initial_state = idle
