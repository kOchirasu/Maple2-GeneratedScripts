""" trigger/02010052_bf/torchlight_04.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,6065,6066], visible=False, arg3=800, delay=100, scale=8) # 벽 해제
        self.set_effect(triggerIds=[7004], visible=False) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=707, minUsers='1'):
            return Event_04(self.ctx)


class Event_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[104], animationEffect=True) # 화로 104 생성
        # 길이 막혔습니다. [b:화로]를 찾아보세요.
        self.show_guide_summary(entityId=200, textId=20105204)
        self.set_effect(triggerIds=[7541], visible=True) # 얼음이 어는 소리
        self.set_mesh(triggerIds=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,6065,6066], visible=True, arg3=80, delay=100, scale=8) # 얼음!
        self.move_npc(spawnId=994, patrolName='MS2PatrolData_1006') # 카나의 분신 994 (이동)
        self.set_conversation(type=1, spawnId=994, script='$02010052_BF__MAIN__6$', arg4=3) # 카나 말풍선 대사

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[104]):
            return burn_state(self.ctx)


class burn_state(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[7504], visible=True) # 얼음 녹는 소리
        self.set_mesh(triggerIds=[6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,6065,6066], visible=False, arg3=800, delay=100, scale=8) # 벽 해제
        self.set_event_ui(type=1, arg2='$02010052_BF__TORCHLIGHT_04__0$', arg3='3000')
        self.set_effect(triggerIds=[7004], visible=True) # 횃불에 불이 붙는 이펙트
        self.set_timer(timerId='1', seconds=1, interval=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return spawn_state(self.ctx)


class spawn_state(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=200)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=80003, enable=True)
        self.set_conversation(type=2, spawnId=21800073, script='$02010052_BF__TORCHLIGHT_04__1$', arg4=2) # 카나 대사
        self.set_timer(timerId='2', seconds=2)
        self.set_skip(state=run)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return run(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()
        # 레터박스, 플레이어 조작 불가능 해제
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_cinematic_ui(type=7)
        self.select_camera(triggerId=80003, enable=False)


class run(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=707, minUsers='1'):
            return run_01(self.ctx)


class run_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=200, textId=20105202) # 카나를 쫓아가세요
        self.set_conversation(type=1, spawnId=994, script='$02010052_BF__TORCHLIGHT_04__2$', arg4=3) # 카나 말풍선 대사
        self.move_npc(spawnId=994, patrolName='MS2PatrolData_1005') # 카나의 분신 994 (이동)
        self.create_monster(spawnIds=[501,502,503,504,505,506], animationEffect=True) # 카나 정령 몬스터 등장


initial_state = start
