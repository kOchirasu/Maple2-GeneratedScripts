""" trigger/99999840/team1_battle.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        dungeon_variable(varId=2, value=0)
        dungeon_variable(varId=100, value=0)
        set_interact_object(triggerIds=[10002178], state=1, arg3=False)
        start_combine_spawn(groupId=[510], isStart=False)
        start_combine_spawn(groupId=[511], isStart=False)
        start_combine_spawn(groupId=[512], isStart=False)
        set_user_value(triggerId=99990001, key='Team1Win', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Team1Battle', value=1):
            return 지역선택1()


class 지역선택1(state.State):
    def on_enter(self):
        score_board_create(maxScore=240)
        # <action name="타이머를설정한다" arg1="1" arg2="60" arg3="1" />

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if random_condition(rate=33):
            return A지역1()
        if random_condition(rate=34):
            return B지역1()
        if random_condition(rate=33):
            return C지역1()


class A지역1(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[510], isStart=True)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if score_board_compare(compareOp='GreaterEqual', score=100):
            return 지역선택2_1()
        """
        <condition name="시간이경과했으면" arg1="1" >
        """


class B지역1(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[511], isStart=True)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if score_board_compare(compareOp='GreaterEqual', score=100):
            return 지역선택2_2()
        """
        <condition name="시간이경과했으면" arg1="1" >
        """


class C지역1(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[512], isStart=True)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if score_board_compare(compareOp='GreaterEqual', score=100):
            return 지역선택2_1()
        """
        <condition name="시간이경과했으면" arg1="1" >
        """


class 지역선택2_1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='추가 병력 등장', arg3='4000', arg4='9101')
        # <action name="타이머를설정한다" arg1="2" arg2="60" arg3="1" />

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if random_condition(rate=50):
            return B지역2()
        if random_condition(rate=50):
            return C지역2()


class 지역선택2_2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='추가 병력 등장', arg3='4000', arg4='9101')
        set_timer(timerId='2', seconds=60, clearAtZero=True)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if random_condition(rate=50):
            return A지역2()
        if random_condition(rate=50):
            return C지역2()


class 지역선택2_3(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='추가 병력 등장', arg3='4000', arg4='9101')
        set_timer(timerId='2', seconds=60, clearAtZero=True)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if random_condition(rate=50):
            return A지역2()
        if random_condition(rate=50):
            return B지역2()


class A지역2(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[510], isStart=True)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if score_board_compare(compareOp='GreaterEqual', score=240):
            score_board_remove()
            return 지역선택3_1()
        """
        <condition name="시간이경과했으면" arg1="2" >
        """


class B지역2(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[511], isStart=True)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if score_board_compare(compareOp='GreaterEqual', score=240):
            score_board_remove()
            return 지역선택3_2()
        """
        <condition name="시간이경과했으면" arg1="2" >
        """


class C지역2(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[512], isStart=True)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if score_board_compare(compareOp='GreaterEqual', score=240):
            score_board_remove()
            return 지역선택3_3()
        """
        <condition name="시간이경과했으면" arg1="2" >
        """


class 지역선택3_1(state.State):
    def on_enter(self):
        dungeon_variable(varId=1000, value=1)
        # <action name="이벤트UI를설정한다" arg1="1" arg2="상대편 지역으로 침투할 수 있는 포탈이 생성되었습니다.\n한 명만 갈 수 있습니다." arg3="4000" arg4="9101" />

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if random_condition(rate=50):
            return B지역3()
        if random_condition(rate=50):
            return C지역3()


class 지역선택3_2(state.State):
    def on_enter(self):
        dungeon_variable(varId=1000, value=1)
        # <action name="이벤트UI를설정한다" arg1="1" arg2="상대편 지역으로 침투할 수 있는 포탈이 생성되었습니다.\n한 명만 갈 수 있습니다." arg3="4000" arg4="9101" />

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if random_condition(rate=50):
            return A지역3()
        if random_condition(rate=50):
            return C지역3()


class 지역선택3_3(state.State):
    def on_enter(self):
        dungeon_variable(varId=1000, value=1)
        # <action name="이벤트UI를설정한다" arg1="1" arg2="상대편 지역으로 침투할 수 있는 포탈이 생성되었습니다.\n한 명만 갈 수 있습니다." arg3="4000" arg4="9101" />

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()
        if random_condition(rate=50):
            return A지역3()
        if random_condition(rate=50):
            return B지역3()


class A지역3(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[510], isStart=True)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()


class B지역3(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[511], isStart=True)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()


class C지역3(state.State):
    def on_enter(self):
        start_combine_spawn(groupId=[512], isStart=True)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if object_interacted(interactIds=[10002178], arg2=0):
            return 시작_보스전()


class 시작_보스전(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002175], state=0, arg3=False)
        set_interact_object(triggerIds=[10002176], state=0, arg3=False)
        set_interact_object(triggerIds=[10002177], state=0, arg3=False)
        set_interact_object(triggerIds=[10002178], state=0, arg3=False)
        start_combine_spawn(groupId=[510], isStart=False)
        start_combine_spawn(groupId=[511], isStart=False)
        start_combine_spawn(groupId=[512], isStart=False)
        create_monster(spawnIds=[901], arg2=False)
        dungeon_variable(varId=100, value=1)

    def on_tick(self) -> state.State:
        if dungeon_variable(varID='3', value=1):
            return 종료()
        if monster_dead(boxIds=[901]):
            return 성공()


class 성공(state.State):
    def on_enter(self):
        dungeon_variable(varId=2, value=1)


class 종료(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002175], state=0, arg3=False)
        set_interact_object(triggerIds=[10002176], state=0, arg3=False)
        set_interact_object(triggerIds=[10002177], state=0, arg3=False)
        set_interact_object(triggerIds=[10002178], state=0, arg3=False)
        start_combine_spawn(groupId=[510], isStart=False)
        start_combine_spawn(groupId=[511], isStart=False)
        start_combine_spawn(groupId=[512], isStart=False)
        destroy_monster(spawnIds=[901])


