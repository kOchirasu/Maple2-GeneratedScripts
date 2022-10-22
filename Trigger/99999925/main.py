""" trigger/99999925/main.xml """
from common import *
import state


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        create_monster(spawnIds=[201,202,203,204,205,206,207], arg2=False)
        create_monster(spawnIds=[211], arg2=False)
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[221,222,223,224,225,226,227,228], arg2=False)
        create_monster(spawnIds=[230,231,232,233], arg2=False)
        set_mesh(triggerIds=[301], visible=False, arg3=0, arg4=0, arg5=0)
        move_npc(spawnId=230, patrolName='MS2PatrolData0')
        move_npc(spawnId=231, patrolName='MS2PatrolData1')
        move_npc(spawnId=232, patrolName='MS2PatrolData11')
        move_npc(spawnId=233, patrolName='MS2PatrolData2')
        move_npc(spawnId=202, patrolName='MS2PatrolData22')
        move_npc(spawnId=205, patrolName='MS2PatrolData3')
        move_npc(spawnId=208, patrolName='MS2PatrolData4')
        move_npc(spawnId=203, patrolName='MS2PatrolData5')

    def on_tick(self) -> state.State:
        if count_users(boxId=402, boxId=1):
            return LoadingStart()

state.DungeonStart = DungeonStart


class LoadingStart(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Dialogue01()


class Dialogue01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=2, spawnId=1, script='$99999925__MAIN__0$', arg4=3)
        set_ai_extra_data(key='BuffStart', value=1, isModify=True)
        set_skip(state=Dialogue01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Dialogue01Skip()


class Dialogue01Skip(state.State):
    def on_enter(self):
        set_skip()
        select_camera(triggerId=500, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return SwitchRandom()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class SwitchRandom(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return switch01()
        if random_condition(rate=33):
            return switch02()
        if random_condition(rate=33):
            return switch03()


class switch01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[403]):
            return BrokenCheck()


class switch02(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[404]):
            return BrokenCheck()


class switch03(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[405]):
            return BrokenCheck()


class BrokenCheck(state.State):
    def on_enter(self):
        set_ai_extra_data(key='BuffStart', value=2, isModify=True)
        set_actor(triggerId=601, visible=True, initialSequence='Opened')
        set_actor(triggerId=602, visible=True, initialSequence='Opened')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[401]):
            return BrokenWood()


class BrokenWood(state.State):
    def on_enter(self):
        set_skill(triggerIds=[411], isEnable=True)
        set_skill(triggerIds=[412], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return None # Missing State: EndPlay


