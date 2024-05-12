""" trigger/99999840/team1_battle.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_variable(varId=2, value=0)
        self.dungeon_variable(varId=100, value=0)
        self.set_interact_object(triggerIds=[10002178], state=1, arg3=False)
        self.start_combine_spawn(groupId=[510], isStart=False)
        self.start_combine_spawn(groupId=[511], isStart=False)
        self.start_combine_spawn(groupId=[512], isStart=False)
        self.set_user_value(triggerId=99990001, key='Team1Win', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Team1Battle', value=1):
            return 지역선택1(self.ctx)


class 지역선택1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.score_board_create(maxScore=240)
        # self.set_timer(timerId='1', seconds=60, startDelay=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.random_condition(rate=33):
            return A지역1(self.ctx)
        if self.random_condition(rate=34):
            return B지역1(self.ctx)
        if self.random_condition(rate=33):
            return C지역1(self.ctx)


class A지역1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(groupId=[510], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        # <condition name="시간이경과했으면" arg1="1" >
        if self.score_board_compare(operator='GreaterEqual', score=100):
            return 지역선택2_1(self.ctx)


class B지역1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(groupId=[511], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        # <condition name="시간이경과했으면" arg1="1" >
        if self.score_board_compare(operator='GreaterEqual', score=100):
            return 지역선택2_2(self.ctx)


class C지역1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(groupId=[512], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        # <condition name="시간이경과했으면" arg1="1" >
        if self.score_board_compare(operator='GreaterEqual', score=100):
            return 지역선택2_1(self.ctx)


class 지역선택2_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='추가 병력 등장', arg3='4000', arg4='9101')
        # self.set_timer(timerId='2', seconds=60, startDelay=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(rate=50):
            return B지역2(self.ctx)
        if self.random_condition(rate=50):
            return C지역2(self.ctx)


class 지역선택2_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='추가 병력 등장', arg3='4000', arg4='9101')
        self.set_timer(timerId='2', seconds=60, startDelay=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(rate=50):
            return A지역2(self.ctx)
        if self.random_condition(rate=50):
            return C지역2(self.ctx)


class 지역선택2_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='추가 병력 등장', arg3='4000', arg4='9101')
        self.set_timer(timerId='2', seconds=60, startDelay=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(rate=50):
            return A지역2(self.ctx)
        if self.random_condition(rate=50):
            return B지역2(self.ctx)


class A지역2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(groupId=[510], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        # <condition name="시간이경과했으면" arg1="2" >
        if self.score_board_compare(operator='GreaterEqual', score=240):
            self.score_board_remove()
            return 지역선택3_1(self.ctx)


class B지역2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(groupId=[511], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        # <condition name="시간이경과했으면" arg1="2" >
        if self.score_board_compare(operator='GreaterEqual', score=240):
            self.score_board_remove()
            return 지역선택3_2(self.ctx)


class C지역2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(groupId=[512], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        # <condition name="시간이경과했으면" arg1="2" >
        if self.score_board_compare(operator='GreaterEqual', score=240):
            self.score_board_remove()
            return 지역선택3_3(self.ctx)


class 지역선택3_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_variable(varId=1000, value=1)
        # self.set_event_ui(type=1, arg2='상대편 지역으로 침투할 수 있는 포탈이 생성되었습니다.\\n한 명만 갈 수 있습니다.', arg3='4000', arg4='9101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(rate=50):
            return B지역3(self.ctx)
        if self.random_condition(rate=50):
            return C지역3(self.ctx)


class 지역선택3_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_variable(varId=1000, value=1)
        # self.set_event_ui(type=1, arg2='상대편 지역으로 침투할 수 있는 포탈이 생성되었습니다.\\n한 명만 갈 수 있습니다.', arg3='4000', arg4='9101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(rate=50):
            return A지역3(self.ctx)
        if self.random_condition(rate=50):
            return C지역3(self.ctx)


class 지역선택3_3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_variable(varId=1000, value=1)
        # self.set_event_ui(type=1, arg2='상대편 지역으로 침투할 수 있는 포탈이 생성되었습니다.\\n한 명만 갈 수 있습니다.', arg3='4000', arg4='9101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)
        if self.random_condition(rate=50):
            return A지역3(self.ctx)
        if self.random_condition(rate=50):
            return B지역3(self.ctx)


class A지역3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(groupId=[510], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)


class B지역3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(groupId=[511], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)


class C지역3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(groupId=[512], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.object_interacted(interactIds=[10002178], stateValue=0):
            return 시작_보스전(self.ctx)


class 시작_보스전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10002175], state=0, arg3=False)
        self.set_interact_object(triggerIds=[10002176], state=0, arg3=False)
        self.set_interact_object(triggerIds=[10002177], state=0, arg3=False)
        self.set_interact_object(triggerIds=[10002178], state=0, arg3=False)
        self.start_combine_spawn(groupId=[510], isStart=False)
        self.start_combine_spawn(groupId=[511], isStart=False)
        self.start_combine_spawn(groupId=[512], isStart=False)
        self.create_monster(spawnIds=[901], animationEffect=False)
        self.dungeon_variable(varId=100, value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_variable(varId=3, value=1):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[901]):
            return 성공(self.ctx)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_variable(varId=2, value=1)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10002175], state=0, arg3=False)
        self.set_interact_object(triggerIds=[10002176], state=0, arg3=False)
        self.set_interact_object(triggerIds=[10002177], state=0, arg3=False)
        self.set_interact_object(triggerIds=[10002178], state=0, arg3=False)
        self.start_combine_spawn(groupId=[510], isStart=False)
        self.start_combine_spawn(groupId=[511], isStart=False)
        self.start_combine_spawn(groupId=[512], isStart=False)
        self.destroy_monster(spawnIds=[901])


initial_state = 대기
