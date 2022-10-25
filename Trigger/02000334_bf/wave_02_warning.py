""" trigger/02000334_bf/wave_02_warning.xml """
import common


# 플레이어 감지
class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=90099, spawnIds=[151]):
            return 차타이머1(self.ctx)


class 차타이머1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='15', seconds=15)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='15'):
            return 돌격(self.ctx)


# 몬스터 돌격 생성
class 돌격(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98001], visible=True)
        self.set_conversation(type=1, spawnId=190, script='$02000334_BF__WAVE__2$', arg4=3) # 보스 대사
        self.move_npc(spawnId=190, patrolName='MS2PatrolData_3501') # 바라하 빡침 모션
        self.create_monster(spawnIds=[991,993,994], animationEffect=True)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 카메라_복구(self.ctx)


class 카메라_복구(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98006], visible=True)
        self.add_buff(boxIds=[90001], skillId=70000068, level=1) # 이속 버프를 걸어준다
        self.move_npc(spawnId=199, patrolName='MS2PatrolData_3502') # 오스칼 대응 모션
        self.set_conversation(type=1, spawnId=199, script='$02000334_BF__WAVE__3$', arg4=3) # 오스칼 대사
        self.select_camera_path(pathIds=[8017], returnView=False)
        self.set_timer(timerId='15', seconds=15)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='15'):
            return 돌격2(self.ctx)


# 몬스터 2차 돌격 생성
class 돌격2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98001], visible=True)
        self.move_npc(spawnId=190, patrolName='MS2PatrolData_3501') # 바라하 빡침 모션
        self.set_conversation(type=1, spawnId=190, script='$02000334_BF__WAVE__4$', arg4=3) # 보스 대사
        self.create_monster(spawnIds=[992,995], animationEffect=True)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 카메라_복구2(self.ctx)


class 카메라_복구2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98006], visible=True)
        self.add_buff(boxIds=[90001], skillId=70000068, level=1) # 이속 버프를 걸어준다
        self.move_npc(spawnId=199, patrolName='MS2PatrolData_3502') # 오스칼 대응 모션
        self.set_conversation(type=1, spawnId=199, script='$02000334_BF__WAVE__5$', arg4=3) # 오스칼 대사
        self.select_camera_path(pathIds=[8017], returnView=False)


initial_state = 시작
