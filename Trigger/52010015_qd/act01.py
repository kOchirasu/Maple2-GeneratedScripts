""" trigger/52010015_qd/act01.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[10002824], questStates=[2]):
            return 딜레이01(self.ctx)


class 딜레이01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='100', seconds=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='100'):
            return 미카교체01(self.ctx)


# 1st Quest
class 미카교체01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 미카이동01(self.ctx)


class 미카이동01(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_2020')

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=8000, spawnIds=[202]):
            return 미카소멸01(self.ctx)


class 미카소멸01(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[202])


initial_state = 대기
