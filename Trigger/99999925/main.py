""" trigger/99999925/main.xml """
import trigger_api


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[201,202,203,204,205,206,207], animationEffect=False)
        self.create_monster(spawnIds=[211], animationEffect=False)
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.create_monster(spawnIds=[221,222,223,224,225,226,227,228], animationEffect=False)
        self.create_monster(spawnIds=[230,231,232,233], animationEffect=False)
        self.set_mesh(triggerIds=[301], visible=False, arg3=0, delay=0, scale=0)
        self.move_npc(spawnId=230, patrolName='MS2PatrolData0')
        self.move_npc(spawnId=231, patrolName='MS2PatrolData1')
        self.move_npc(spawnId=232, patrolName='MS2PatrolData11')
        self.move_npc(spawnId=233, patrolName='MS2PatrolData2')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData22')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData3')
        self.move_npc(spawnId=208, patrolName='MS2PatrolData4')
        self.move_npc(spawnId=203, patrolName='MS2PatrolData5')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=402, minUsers='1'):
            return LoadingStart(self.ctx)


class LoadingStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Dialogue01(self.ctx)


class Dialogue01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=2, spawnId=1, script='$99999925__MAIN__0$', arg4=3)
        self.set_ai_extra_data(key='BuffStart', value=1, isModify=True)
        self.set_skip(state=Dialogue01Skip)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return Dialogue01Skip(self.ctx)


class Dialogue01Skip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_skip()
        self.select_camera(triggerId=500, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return SwitchRandom(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class SwitchRandom(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=33):
            return switch01(self.ctx)
        if self.random_condition(rate=33):
            return switch02(self.ctx)
        if self.random_condition(rate=33):
            return switch03(self.ctx)


class switch01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[403]):
            return BrokenCheck(self.ctx)


class switch02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[404]):
            return BrokenCheck(self.ctx)


class switch03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[405]):
            return BrokenCheck(self.ctx)


class BrokenCheck(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ai_extra_data(key='BuffStart', value=2, isModify=True)
        self.set_actor(triggerId=601, visible=True, initialSequence='Opened')
        self.set_actor(triggerId=602, visible=True, initialSequence='Opened')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[401]):
            return BrokenWood(self.ctx)


class BrokenWood(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[411], enable=True)
        self.set_skill(triggerIds=[412], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return None # Missing State: EndPlay


initial_state = DungeonStart
