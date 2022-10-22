""" trigger/02000334_bf/wave_03_warning.xml """
from common import *
import state


#  플레이어 감지 
class 시작(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=90099, spawnIds=[152]):
            return 차타이머1()


class 차타이머1(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 돌격()


#  몬스터 돌격 생성 
class 돌격(state.State):
    def on_enter(self):
        set_effect(triggerIds=[98001], visible=True)
        move_npc(spawnId=190, patrolName='MS2PatrolData_3501') # 바라하 빡침 모션
        set_conversation(type=1, spawnId=190, script='$02000334_BF__WAVE__6$', arg4=3) # 보스 대사
        create_monster(spawnIds=[991,996], arg2=True)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 카메라_복구()


class 카메라_복구(state.State):
    def on_enter(self):
        set_effect(triggerIds=[98006], visible=True)
        add_buff(boxIds=[90001], skillId=70000068, level=1) # 이속 버프를 걸어준다
        move_npc(spawnId=199, patrolName='MS2PatrolData_3502') # 오스칼 대응 모션
        set_conversation(type=1, spawnId=199, script='$02000334_BF__WAVE__7$', arg4=3) # 오스칼 대사
        set_timer(timerId='10', seconds=10)
        select_camera_path(pathIds=[8017], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 돌격2()


#  몬스터 2차 돌격 생성 
class 돌격2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[98001], visible=True)
        move_npc(spawnId=190, patrolName='MS2PatrolData_3501') # 바라하 빡침 모션
        set_conversation(type=1, spawnId=190, script='$02000334_BF__WAVE__8$', arg4=3) # 보스 대사
        create_monster(spawnIds=[992,995,997], arg2=True)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 카메라_복구2()


class 카메라_복구2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[98006], visible=True)
        move_npc(spawnId=199, patrolName='MS2PatrolData_3502') # 오스칼 대응 모션
        set_conversation(type=1, spawnId=199, script='$02000334_BF__WAVE__9$', arg4=3) # 오스칼 대사
        add_buff(boxIds=[90001], skillId=70000068, level=1) # 이속 버프를 걸어준다
        set_timer(timerId='10', seconds=10)
        select_camera_path(pathIds=[8017], returnView=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 돌격3()


#  몬스터 3차 돌격 생성 
class 돌격3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[98001], visible=True)
        move_npc(spawnId=190, patrolName='MS2PatrolData_3501') # 바라하 빡침 모션
        set_conversation(type=1, spawnId=190, script='$02000334_BF__WAVE__10$', arg4=3) # 보스 대사
        create_monster(spawnIds=[993,994,996], arg2=True)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 카메라_복구3()


class 카메라_복구3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[98006], visible=True)
        add_buff(boxIds=[90001], skillId=70000068, level=1) # 이속 버프를 걸어준다
        move_npc(spawnId=199, patrolName='MS2PatrolData_3502') # 오스칼 대응 모션
        set_conversation(type=1, spawnId=199, script='$02000334_BF__WAVE__11$', arg4=3) # 오스칼 대사
        select_camera_path(pathIds=[8017], returnView=False)


