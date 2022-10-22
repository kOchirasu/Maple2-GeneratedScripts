""" trigger/02000334_bf/wave_01_warning.xml """
from common import *
import state


#  플레이어 감지 
class 시작(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=90099, spawnIds=[150]):
            return 차타이머1()
        if monster_dead(boxIds=[999]):
            return 게임오버()


class 차타이머1(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 돌격()


#  몬스터 돌격 생성 
class 돌격(state.State):
    def on_enter(self):
        set_effect(triggerIds=[98001], visible=True)
        move_npc(spawnId=190, patrolName='MS2PatrolData_3501') # 바라하 빡침 모션
        set_conversation(type=1, spawnId=190, script='$02000334_BF__WAVE__0$', arg4=3) # 보스 대사
        create_monster(spawnIds=[991,992,993], arg2=True)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 카메라 복구()


class 카메라 복구(state.State):
    def on_enter(self):
        set_effect(triggerIds=[98006], visible=True)
        move_npc(spawnId=199, patrolName='MS2PatrolData_3502') # 오스칼 대응 모션
        add_buff(boxIds=[90001], skillId=70000068, level=1) # 이속 버프를 걸어준다
        set_conversation(type=1, spawnId=199, script='$02000334_BF__WAVE__1$', arg4=3) # 오스칼 대사
        select_camera_path(pathIds=[8017], returnView=False)


class 게임오버(state.State):
    pass


