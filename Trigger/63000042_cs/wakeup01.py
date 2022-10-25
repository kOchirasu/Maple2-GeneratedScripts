""" trigger/63000042_cs/wakeup01.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001484], questStates=[2]):
            return LodingDelay00(self.ctx)


class LodingDelay00(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LodingDelay01(self.ctx)


class LodingDelay01(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000042, portalId=10)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return LodingDelay02(self.ctx)


class LodingDelay02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.select_camera(triggerId=500, enable=True)
        self.set_pc_emotion_loop(sequenceName='Down_Idle_D', duration=6000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCDownIdle01(self.ctx)


class PCDownIdle01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=PCDownIdle02)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCDownIdle02(self.ctx)


class PCDownIdle02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return DoctorTalk01(self.ctx)


class DoctorTalk01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11000038, script='$63000042_CS__WAKEUP01__0$', arg4=4)
        self.set_skip(state=DoctorTalk01Skip)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return DoctorTalk01Skip(self.ctx)


class DoctorTalk01Skip(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return LookAround01(self.ctx)


class LookAround01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=500, enable=False)
        self.select_camera(triggerId=501, enable=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')
        self.set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=18000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return LookAround02(self.ctx)


class LookAround02(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return DoctorTalk02(self.ctx)


class DoctorTalk02(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=5000)
        self.set_conversation(type=2, spawnId=11000038, script='$63000042_CS__WAKEUP01__1$', arg4=5)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return DoctorTalk03(self.ctx)


class DoctorTalk03(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=5000)
        self.set_conversation(type=2, spawnId=11000038, script='$63000042_CS__WAKEUP01__2$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return DoctorTalk04(self.ctx)


class DoctorTalk04(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=5000)
        self.set_conversation(type=2, spawnId=11000038, script='$63000042_CS__WAKEUP01__3$', arg4=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return SceneEnd01(self.ctx)


class SceneEnd01(common.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Idle_A')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return SceneEnd02(self.ctx)


class SceneEnd02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=501, enable=False)
        self.set_pc_emotion_sequence(sequenceNames=['Idle_A'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)


initial_state = Wait
