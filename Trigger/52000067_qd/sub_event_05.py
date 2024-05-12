""" trigger/52000067_qd/sub_event_05.xml """
import trigger_api


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=707, spawnIds=[751]):
            return NPC소멸751(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[752]):
            return NPC소멸752(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[753]):
            return NPC소멸753(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[754]):
            return NPC소멸754(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[755]):
            return NPC소멸755(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[756]):
            return NPC소멸756(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[757]):
            return NPC소멸757(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[758]):
            return NPC소멸758(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[759]):
            return NPC소멸759(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[761]):
            return NPC소멸761(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[762]):
            return NPC소멸762(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[591]):
            return NPC소멸591(self.ctx)
        if self.npc_detected(boxId=707, spawnIds=[592]):
            return NPC소멸592(self.ctx)


class NPC소멸751(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[751])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸752(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[752])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸753(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[753])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸754(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[754])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸755(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[755])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸756(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[756])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸757(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[757])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸758(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[758])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸759(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[759])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸761(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[761])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸762(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[762])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸591(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[591])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


class NPC소멸592(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[592])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return idle(self.ctx)


initial_state = idle
