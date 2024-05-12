""" trigger/02000207_bf/999109_lavaflow.xml """
import trigger_api


# 계약의 토템에 의해 오른쪽 지점에 용암파도 생성
class 전투체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(spawn_ids=[2001]):
            return 대기(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[600], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='LavaflowRight') >= 1:
            # 오른쪽 용암 담당 계약의 토템이 생성될때, 이 부분 작동,   LavaflowRight 변수는 자쿰몸체 보스한테 LavaflowRight = 1 설정되어서 넘어오는 것임
            return 오른쪽용암생성(self.ctx)
        if self.user_value(key='BattleEnd2') >= 1:
            # BattleEnd2 변수는 보스 생성쪽 트리거 설정 xml 에서 보스가 죽을 경우 BattleEnd2 = 1 설정되어서 넘어오는 것임
            return 종료(self.ctx)


# 오른쪽담당 계약의 토템을 소환하면서 자쿰몸체한테 신호 받아 용암 올라오는 경우임
class 오른쪽용암생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 이 Lavaflow.xml 파일과 연결된  MS2TriggerModel의 TriggerModelID가 999102 임
        # LavaflowRight 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        self.set_user_value(trigger_id=999109, key='LavaflowRight', value=0)
        # ### 올라온 용암 내려가게 할 때 사용하는 LavaflowRightStop 변수 이전에 이미 사용했을 수 있으므로 여기서  0으로 꼭 초기화 해야함
        self.set_user_value(trigger_id=999109, key='LavaflowRightStop', value=0)
        self.set_effect(trigger_ids=[600], visible=True)
        self.spawn_monster(spawn_ids=[1003], auto_target=False)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003A')

    def on_tick(self) -> trigger_api.Trigger:
        # 보스가 죽으면 보스 스폰시키는 트리거 xml 에서 BattleEnd2 = 1 신호를 보내서 올라와 있는 용암을 여기서 바로 제거 시키게 함
        if self.user_value(key='LavaflowRightStop') >= 1:
            return 오른쪽용암내려가기(self.ctx)
        if self.user_value(key='BattleEnd2') >= 1:
            return 종료(self.ctx)


class 오른쪽용암내려가기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # ### 오른쪽용암내려가기  신호받는 대기 상태에서 이 변수가 1이 되는 상황이 생길수도 있기 때문에 만약을 대비해 여기서도 다시한번 0으로 초기화 함
        self.set_user_value(trigger_id=999109, key='LavaflowRight', value=0)
        # LavaflowRightStop 변수 다음에 사용하기 위해서 0으로 꼭 초기화 해야함
        self.set_user_value(trigger_id=999109, key='LavaflowRightStop', value=0)
        self.move_npc(spawn_id=1003, patrol_name='MS2PatrolData_1003C')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            self.destroy_monster(spawn_ids=[1003])
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[1003])


initial_state = 전투체크
