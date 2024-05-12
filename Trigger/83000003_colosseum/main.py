""" trigger/83000003_colosseum/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # self.set_user_value(triggerId=900001, key='Reset', value=0)
        pass

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MainStart', value=1):
            self.set_user_value(triggerId=900001, key='MainStart', value=0)
            self.destroy_monster(spawnIds=[203])
            self.create_monster(spawnIds=[202], animationEffect=False)
            return WaitRound1(self.ctx)
        if self.user_value(key='MainStart', value=2):
            self.set_user_value(triggerId=900001, key='MainStart', value=0)
            self.destroy_monster(spawnIds=[203])
            self.create_monster(spawnIds=[202], animationEffect=False)
            return ContinuePlayDelay(self.ctx)


class WaitRound1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.set_user_value(triggerId=910001, key='StartRound1', value=1)
            return ResultRound1(self.ctx)
        if self.user_detected(boxIds=[902]):
            self.move_user_to_pos(pos=[300,-225,1500], rot=[0,0,270])
            return WaitRound1(self.ctx)


class ContinuePlayDelay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.lock_my_pc(isLock=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.move_user_to_pos(pos=[300,-225,1500], rot=[0,0,270])
            return ContinuePlayDelay2(self.ctx)


class ContinuePlayDelay2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.move_user_path(patrolName='MS2PatrolData_01')
            return ContinuePlay(self.ctx)


class ContinuePlay(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value_from_dungeon_reward_count(key='ClearRound', dungeonRewardId=24096001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='ClearRound', value=1):
            # self.debug_string(string='이어하기로 2스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910002, key='StartRound2', value=1)
            return ResultRound2(self.ctx)
        if self.user_value(key='ClearRound', value=2):
            # self.debug_string(string='이어하기로 3스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910003, key='StartRound3', value=1)
            return ResultRound3(self.ctx)
        if self.user_value(key='ClearRound', value=3):
            # self.debug_string(string='이어하기로 4스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910004, key='StartRound4', value=1)
            return ResultRound4(self.ctx)
        if self.user_value(key='ClearRound', value=4):
            # self.debug_string(string='이어하기로 5스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910005, key='StartRound5', value=1)
            return ResultRound5(self.ctx)
        if self.user_value(key='ClearRound', value=5):
            # self.debug_string(string='이어하기로 6스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910006, key='StartRound6', value=1)
            return ResultRound6(self.ctx)
        if self.user_value(key='ClearRound', value=6):
            # self.debug_string(string='이어하기로 7스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910007, key='StartRound7', value=1)
            return ResultRound7(self.ctx)
        if self.user_value(key='ClearRound', value=7):
            # self.debug_string(string='이어하기로 8스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910008, key='StartRound8', value=1)
            return ResultRound8(self.ctx)
        if self.user_value(key='ClearRound', value=8):
            # self.debug_string(string='이어하기로 9스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910009, key='StartRound9', value=1)
            return ResultRound9(self.ctx)
        if self.user_value(key='ClearRound', value=9):
            # self.debug_string(string='이어하기로 10스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910010, key='StartRound10', value=1)
            return ResultRound10(self.ctx)
        if self.user_value(key='ClearRound', value=10):
            # self.debug_string(string='이어하기로 11스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910011, key='StartRound11', value=1)
            return ResultRound11(self.ctx)
        if self.user_value(key='ClearRound', value=11):
            # self.debug_string(string='이어하기로 12스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910012, key='StartRound12', value=1)
            return ResultRound12(self.ctx)
        if self.user_value(key='ClearRound', value=12):
            # self.debug_string(string='이어하기로 13스테이지 부터 시작합니다.')
            self.set_user_value(triggerId=910013, key='StartRound13', value=1)
            return ResultRound13(self.ctx)
        if self.user_value(key='ClearRound', value=13):
            # self.debug_string(string='이미 13 스테이지까지 완료 했습니다. 처음부터 시작합니다. ')
            return WaitRound1(self.ctx)


class ResultRound1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound1', value=2):
            self.dungeon_clear_round(round=1)
            self.set_user_value(triggerId=910001, key='StartRound1', value=0)
            self.set_user_value(triggerId=900001, key='StartRound1', value=0)
            return WaitRound2(self.ctx)
        if self.user_value(key='StartRound1', value=3):
            self.dungeon_clear_round(round=0)
            self.set_user_value(triggerId=910001, key='StartRound1', value=0)
            self.set_user_value(triggerId=900001, key='StartRound1', value=0)
            return RoundFail(self.ctx)


class WaitRound2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910002, key='StartRound2', value=1)
            return ResultRound2(self.ctx)


class ResultRound2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound2', value=2):
            self.dungeon_clear_round(round=2)
            self.set_user_value(triggerId=910002, key='StartRound2', value=0)
            self.set_user_value(triggerId=900001, key='StartRound2', value=0)
            return WaitRound3(self.ctx)
        if self.user_value(key='StartRound2', value=3):
            self.set_user_value(triggerId=910002, key='StartRound2', value=0)
            self.set_user_value(triggerId=900001, key='StartRound2', value=0)
            return RoundClear1(self.ctx)


class WaitRound3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910003, key='StartRound3', value=1)
            return ResultRound3(self.ctx)


class ResultRound3(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound3', value=2):
            self.dungeon_clear_round(round=3)
            self.set_user_value(triggerId=910003, key='StartRound3', value=0)
            self.set_user_value(triggerId=900001, key='StartRound3', value=0)
            return WaitRound4(self.ctx)
        if self.user_value(key='StartRound3', value=3):
            self.set_user_value(triggerId=910003, key='StartRound3', value=0)
            self.set_user_value(triggerId=900001, key='StartRound3', value=0)
            return RoundClear2(self.ctx)


class WaitRound4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910004, key='StartRound4', value=1)
            return ResultRound4(self.ctx)


class ResultRound4(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound4', value=2):
            self.dungeon_clear_round(round=4)
            self.set_user_value(triggerId=910004, key='StartRound4', value=0)
            self.set_user_value(triggerId=900001, key='StartRound4', value=0)
            return WaitRound5(self.ctx)
        if self.user_value(key='StartRound4', value=3):
            self.set_user_value(triggerId=910004, key='StartRound4', value=0)
            self.set_user_value(triggerId=900001, key='StartRound4', value=0)
            return RoundClear3(self.ctx)


class WaitRound5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910005, key='StartRound5', value=1)
            return ResultRound5(self.ctx)


class ResultRound5(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound5', value=2):
            self.dungeon_clear_round(round=5)
            self.set_user_value(triggerId=910005, key='StartRound5', value=0)
            self.set_user_value(triggerId=900001, key='StartRound5', value=0)
            return WaitRound6(self.ctx)
        if self.user_value(key='StartRound5', value=3):
            self.set_user_value(triggerId=910005, key='StartRound5', value=0)
            self.set_user_value(triggerId=900001, key='StartRound5', value=0)
            return RoundClear4(self.ctx)


class WaitRound6(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910006, key='StartRound6', value=1)
            return ResultRound6(self.ctx)


class ResultRound6(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound6', value=2):
            self.dungeon_clear_round(round=6)
            self.set_user_value(triggerId=910006, key='StartRound6', value=0)
            self.set_user_value(triggerId=900001, key='StartRound6', value=0)
            return WaitRound7(self.ctx)
        if self.user_value(key='StartRound6', value=3):
            self.set_user_value(triggerId=910006, key='StartRound6', value=0)
            self.set_user_value(triggerId=900001, key='StartRound6', value=0)
            return RoundClear5(self.ctx)


class WaitRound7(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910007, key='StartRound7', value=1)
            return ResultRound7(self.ctx)


class ResultRound7(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound7', value=2):
            self.dungeon_clear_round(round=7)
            self.set_user_value(triggerId=910007, key='StartRound7', value=0)
            self.set_user_value(triggerId=900001, key='StartRound7', value=0)
            return WaitRound8(self.ctx)
        if self.user_value(key='StartRound7', value=3):
            self.set_user_value(triggerId=910007, key='StartRound7', value=0)
            self.set_user_value(triggerId=900001, key='StartRound7', value=0)
            return RoundClear6(self.ctx)


class WaitRound8(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910008, key='StartRound8', value=1)
            return ResultRound8(self.ctx)


class ResultRound8(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound8', value=2):
            self.dungeon_clear_round(round=8)
            self.set_user_value(triggerId=910008, key='StartRound8', value=0)
            self.set_user_value(triggerId=900001, key='StartRound8', value=0)
            return WaitRound9(self.ctx)
        if self.user_value(key='StartRound8', value=3):
            self.set_user_value(triggerId=910008, key='StartRound8', value=0)
            self.set_user_value(triggerId=900001, key='StartRound8', value=0)
            return RoundClear7(self.ctx)


class WaitRound9(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910009, key='StartRound9', value=1)
            return ResultRound9(self.ctx)


class ResultRound9(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound9', value=2):
            self.dungeon_clear_round(round=9)
            self.set_user_value(triggerId=910009, key='StartRound9', value=0)
            self.set_user_value(triggerId=900001, key='StartRound9', value=0)
            return WaitRound10(self.ctx)
        if self.user_value(key='StartRound9', value=3):
            self.set_user_value(triggerId=910009, key='StartRound9', value=0)
            self.set_user_value(triggerId=900001, key='StartRound9', value=0)
            return RoundClear8(self.ctx)


class WaitRound10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910010, key='StartRound10', value=1)
            return ResultRound10(self.ctx)


class ResultRound10(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound10', value=2):
            self.dungeon_clear_round(round=10)
            self.set_user_value(triggerId=910010, key='StartRound10', value=0)
            self.set_user_value(triggerId=900001, key='StartRound10', value=0)
            return WaitRound11(self.ctx)
        if self.user_value(key='StartRound10', value=3):
            self.set_user_value(triggerId=910010, key='StartRound10', value=0)
            self.set_user_value(triggerId=900001, key='StartRound10', value=0)
            return RoundClear9(self.ctx)


class WaitRound11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910011, key='StartRound11', value=1)
            return ResultRound11(self.ctx)


class ResultRound11(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound11', value=2):
            self.dungeon_clear_round(round=11)
            self.set_user_value(triggerId=910011, key='StartRound11', value=0)
            self.set_user_value(triggerId=900001, key='StartRound11', value=0)
            return WaitRound12(self.ctx)
        if self.user_value(key='StartRound11', value=3):
            self.set_user_value(triggerId=910011, key='StartRound11', value=0)
            self.set_user_value(triggerId=900001, key='StartRound11', value=0)
            return RoundClear10(self.ctx)


class WaitRound12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910012, key='StartRound12', value=1)
            return ResultRound12(self.ctx)


class ResultRound12(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound12', value=2):
            self.dungeon_clear_round(round=12)
            self.set_user_value(triggerId=910012, key='StartRound12', value=0)
            self.set_user_value(triggerId=900001, key='StartRound12', value=0)
            return WaitRound13(self.ctx)
        if self.user_value(key='StartRound12', value=3):
            self.set_user_value(triggerId=910012, key='StartRound12', value=0)
            self.set_user_value(triggerId=900001, key='StartRound12', value=0)
            return RoundClear11(self.ctx)


class WaitRound13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_user_value(triggerId=910013, key='StartRound13', value=1)
            return ResultRound13(self.ctx)


class ResultRound13(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='StartRound13', value=2):
            self.dungeon_clear_round(round=13)
            self.set_user_value(triggerId=910013, key='StartRound13', value=0)
            self.set_user_value(triggerId=900001, key='StartRound13', value=0)
            return AllRoundClear(self.ctx)
        if self.user_value(key='StartRound13', value=3):
            self.set_user_value(triggerId=910013, key='StartRound13', value=0)
            self.set_user_value(triggerId=900001, key='StartRound13', value=0)
            return RoundClear12(self.ctx)


class RoundClear1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundClear2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundClear3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundClear4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundClear5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundClear6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundClear7(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundClear8(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundClear9(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundClear10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundClear11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundClear12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear(uiType='None')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class AllRoundClear(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class RoundFail(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_fail()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


initial_state = 대기
