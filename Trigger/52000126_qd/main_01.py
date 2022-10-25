""" trigger/52000126_qd/main_01.xml """
import common


class idle(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100210], questStates=[2]):
            return ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60100210], questStates=[3]):
            return ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60100215], questStates=[1]):
            return ready(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60100215], questStates=[2]):
            return ready(self.ctx)


# 준비
class ready(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=52000126, portalId=6001)
        self.set_sound(triggerId=7002, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.create_monster(spawnIds=[201], animationEffect=True)
        self.set_scene_skip(state=endwaiting, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return move(self.ctx)


class move(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_3001')
        self.add_balloon_talk(spawnId=201, msg='$52000126_QD__MAIN_01__0$', duration=7000, delayTick=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=7000):
            return talk(self.ctx)


class talk(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Clap_A')
        self.add_balloon_talk(spawnId=201, msg='$52000126_QD__MAIN_01__1$', duration=3000, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return endtalk(self.ctx)


class endtalk(common.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=201, msg='$52000126_QD__MAIN_01__2$', duration=3000, delayTick=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return endwaiting(self.ctx)


class endwaiting(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.destroy_monster(spawnIds=[201])
        self.create_monster(spawnIds=[202], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return end(self.ctx)


class end(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = idle
