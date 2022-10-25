""" trigger/02000334_bf/wave_01_warning.xml """
import common


# 플레이어 감지
class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=90099, spawnIds=[150]):
            return 차타이머1(self.ctx)
        if self.monster_dead(boxIds=[999]):
            return 게임오버(self.ctx)


class 차타이머1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='30', seconds=30)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='30'):
            return 돌격(self.ctx)


# 몬스터 돌격 생성
class 돌격(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98001], visible=True)
        self.move_npc(spawnId=190, patrolName='MS2PatrolData_3501') # 바라하 빡침 모션
        self.set_conversation(type=1, spawnId=190, script='$02000334_BF__WAVE__0$', arg4=3) # 보스 대사
        self.create_monster(spawnIds=[991,992,993], animationEffect=True)
        self.set_timer(timerId='3', seconds=3)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='3'):
            return 카메라 복구(self.ctx)


class 카메라 복구(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[98006], visible=True)
        self.move_npc(spawnId=199, patrolName='MS2PatrolData_3502') # 오스칼 대응 모션
        self.add_buff(boxIds=[90001], skillId=70000068, level=1) # 이속 버프를 걸어준다
        self.set_conversation(type=1, spawnId=199, script='$02000334_BF__WAVE__1$', arg4=3) # 오스칼 대사
        self.select_camera_path(pathIds=[8017], returnView=False)


class 게임오버(common.Trigger):
    pass


initial_state = 시작
