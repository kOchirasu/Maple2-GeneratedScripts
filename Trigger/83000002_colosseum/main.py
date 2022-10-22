""" trigger/83000002_colosseum/main.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='MainStart', value=1):
            set_user_value(triggerId=900001, key='MainStart', value=0)
            destroy_monster(spawnIds=[203])
            create_monster(spawnIds=[202], arg2=False)
            return WaitRound1()
        if user_value(key='MainStart', value=2):
            set_user_value(triggerId=900001, key='MainStart', value=0)
            destroy_monster(spawnIds=[203])
            create_monster(spawnIds=[202], arg2=False)
            return ContinuePlayDelay()


class WaitRound1(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_user_value(triggerId=910001, key='StartRound1', value=1)
            return ResultRound1()
        if user_detected(boxIds=[902]):
            move_user_to_pos(pos=[300,-225,1500], rot=[0,0,270])
            return WaitRound1()


class ContinuePlayDelay(state.State):
    def on_enter(self):
        lock_my_pc(isLock=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            move_user_to_pos(pos=[300,-225,1500], rot=[0,0,270])
            return ContinuePlayDelay2()


class ContinuePlayDelay2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            move_user_path(patrolName='MS2PatrolData_01')
            return ContinuePlay()


class ContinuePlay(state.State):
    def on_enter(self):
        set_user_value_from_dungeon_reward_count(key='ClearRound', dungeonRewardId=24096001)

    def on_tick(self) -> state.State:
        if user_value(key='ClearRound', value=1):
            set_user_value(triggerId=910002, key='StartRound2', value=1)
            return ResultRound2()
        if user_value(key='ClearRound', value=2):
            set_user_value(triggerId=910003, key='StartRound3', value=1)
            return ResultRound3()
        if user_value(key='ClearRound', value=3):
            set_user_value(triggerId=910004, key='StartRound4', value=1)
            return ResultRound4()
        if user_value(key='ClearRound', value=4):
            set_user_value(triggerId=910005, key='StartRound5', value=1)
            return ResultRound5()
        if user_value(key='ClearRound', value=5):
            set_user_value(triggerId=910006, key='StartRound6', value=1)
            return ResultRound6()
        if user_value(key='ClearRound', value=6):
            set_user_value(triggerId=910007, key='StartRound7', value=1)
            return ResultRound7()
        if user_value(key='ClearRound', value=7):
            set_user_value(triggerId=910008, key='StartRound8', value=1)
            return ResultRound8()
        if user_value(key='ClearRound', value=8):
            set_user_value(triggerId=910009, key='StartRound9', value=1)
            return ResultRound9()
        if user_value(key='ClearRound', value=9):
            set_user_value(triggerId=910010, key='StartRound10', value=1)
            return ResultRound10()
        if user_value(key='ClearRound', value=10):
            return WaitRound1()


class ResultRound1(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='StartRound1', value=2):
            dungeon_clear_round(round=1)
            set_user_value(triggerId=910001, key='StartRound1', value=0)
            set_user_value(triggerId=900001, key='StartRound1', value=0)
            return WaitRound2()
        if user_value(key='StartRound1', value=3):
            dungeon_clear_round(round=0)
            set_user_value(triggerId=910001, key='StartRound1', value=0)
            set_user_value(triggerId=900001, key='StartRound1', value=0)
            return RoundFail()


class WaitRound2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=910002, key='StartRound2', value=1)
            return ResultRound2()


class ResultRound2(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='StartRound2', value=2):
            dungeon_clear_round(round=2)
            set_user_value(triggerId=910002, key='StartRound2', value=0)
            set_user_value(triggerId=900001, key='StartRound2', value=0)
            return WaitRound3()
        if user_value(key='StartRound2', value=3):
            set_user_value(triggerId=910002, key='StartRound2', value=0)
            set_user_value(triggerId=900001, key='StartRound2', value=0)
            return RoundClear1()


class WaitRound3(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=910003, key='StartRound3', value=1)
            return ResultRound3()


class ResultRound3(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='StartRound3', value=2):
            dungeon_clear_round(round=3)
            set_user_value(triggerId=910003, key='StartRound3', value=0)
            set_user_value(triggerId=900001, key='StartRound3', value=0)
            return WaitRound4()
        if user_value(key='StartRound3', value=3):
            set_user_value(triggerId=910003, key='StartRound3', value=0)
            set_user_value(triggerId=900001, key='StartRound3', value=0)
            return RoundClear2()


class WaitRound4(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=910004, key='StartRound4', value=1)
            return ResultRound4()


class ResultRound4(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='StartRound4', value=2):
            dungeon_clear_round(round=4)
            set_user_value(triggerId=910004, key='StartRound4', value=0)
            set_user_value(triggerId=900001, key='StartRound4', value=0)
            return WaitRound5()
        if user_value(key='StartRound4', value=3):
            set_user_value(triggerId=910004, key='StartRound4', value=0)
            set_user_value(triggerId=900001, key='StartRound4', value=0)
            return RoundClear3()


class WaitRound5(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=910005, key='StartRound5', value=1)
            return ResultRound5()


class ResultRound5(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='StartRound5', value=2):
            dungeon_clear_round(round=5)
            set_user_value(triggerId=910005, key='StartRound5', value=0)
            set_user_value(triggerId=900001, key='StartRound5', value=0)
            return WaitRound6()
        if user_value(key='StartRound5', value=3):
            set_user_value(triggerId=910005, key='StartRound5', value=0)
            set_user_value(triggerId=900001, key='StartRound5', value=0)
            return RoundClear4()


class WaitRound6(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=910006, key='StartRound6', value=1)
            return ResultRound6()


class ResultRound6(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='StartRound6', value=2):
            dungeon_clear_round(round=6)
            set_user_value(triggerId=910006, key='StartRound6', value=0)
            set_user_value(triggerId=900001, key='StartRound6', value=0)
            return WaitRound7()
        if user_value(key='StartRound6', value=3):
            set_user_value(triggerId=910006, key='StartRound6', value=0)
            set_user_value(triggerId=900001, key='StartRound6', value=0)
            return RoundClear5()


class WaitRound7(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=910007, key='StartRound7', value=1)
            return ResultRound7()


class ResultRound7(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='StartRound7', value=2):
            dungeon_clear_round(round=7)
            set_user_value(triggerId=910007, key='StartRound7', value=0)
            set_user_value(triggerId=900001, key='StartRound7', value=0)
            return WaitRound8()
        if user_value(key='StartRound7', value=3):
            set_user_value(triggerId=910007, key='StartRound7', value=0)
            set_user_value(triggerId=900001, key='StartRound7', value=0)
            return RoundClear6()


class WaitRound8(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=910008, key='StartRound8', value=1)
            return ResultRound8()


class ResultRound8(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='StartRound8', value=2):
            dungeon_clear_round(round=8)
            set_user_value(triggerId=910008, key='StartRound8', value=0)
            set_user_value(triggerId=900001, key='StartRound8', value=0)
            return WaitRound9()
        if user_value(key='StartRound8', value=3):
            set_user_value(triggerId=910008, key='StartRound8', value=0)
            set_user_value(triggerId=900001, key='StartRound8', value=0)
            return RoundClear7()


class WaitRound9(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=910009, key='StartRound9', value=1)
            return ResultRound9()


class ResultRound9(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='StartRound9', value=2):
            dungeon_clear_round(round=9)
            set_user_value(triggerId=910009, key='StartRound9', value=0)
            set_user_value(triggerId=900001, key='StartRound9', value=0)
            return WaitRound10()
        if user_value(key='StartRound9', value=3):
            set_user_value(triggerId=910009, key='StartRound9', value=0)
            set_user_value(triggerId=900001, key='StartRound9', value=0)
            return RoundClear8()


class WaitRound10(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            set_user_value(triggerId=910010, key='StartRound10', value=1)
            return ResultRound10()


class ResultRound10(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='StartRound10', value=2):
            dungeon_clear_round(round=10)
            set_user_value(triggerId=910010, key='StartRound10', value=0)
            set_user_value(triggerId=900001, key='StartRound10', value=0)
            return AllRoundClear()
        if user_value(key='StartRound10', value=3):
            set_user_value(triggerId=910010, key='StartRound10', value=0)
            set_user_value(triggerId=900001, key='StartRound10', value=0)
            return RoundClear9()


class RoundClear1(state.State):
    def on_enter(self):
        dungeon_clear(uiType='None')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class RoundClear2(state.State):
    def on_enter(self):
        dungeon_clear(uiType='None')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class RoundClear3(state.State):
    def on_enter(self):
        dungeon_clear(uiType='None')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class RoundClear4(state.State):
    def on_enter(self):
        dungeon_clear(uiType='None')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class RoundClear5(state.State):
    def on_enter(self):
        dungeon_clear(uiType='None')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class RoundClear6(state.State):
    def on_enter(self):
        dungeon_clear(uiType='None')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class RoundClear7(state.State):
    def on_enter(self):
        dungeon_clear(uiType='None')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class RoundClear8(state.State):
    def on_enter(self):
        dungeon_clear(uiType='None')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class RoundClear9(state.State):
    def on_enter(self):
        dungeon_clear(uiType='None')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class AllRoundClear(state.State):
    def on_enter(self):
        dungeon_clear()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


class RoundFail(state.State):
    def on_enter(self):
        dungeon_fail()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 대기()


