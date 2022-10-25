""" trigger/52000006_qd/tutorial_06_1.xml """
import common


class 엔터대기중(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[100]):
            return 연출세팅(self.ctx)


class 연출세팅(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return PC대사1(self.ctx)


class PC대사1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.set_cinematic_ui(type=3, script='$52000006_QD__TUTORIAL_06_1__0$')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 양등장(self.ctx)


class 양등장(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.select_camera(triggerId=301, enable=True)
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.set_cinematic_ui(type=3, script='$52000006_QD__TUTORIAL_06_1__1$')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 양이동(self.ctx)


class 양이동(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=4)
        self.move_npc(spawnId=201, patrolName='PatrolData_Sheep_01')
        self.set_cinematic_ui(type=3, script='$52000006_QD__TUTORIAL_06_1__2$')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 연출끝(self.ctx)


class 연출끝(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[201])
        self.select_camera(triggerId=302, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = 엔터대기중
