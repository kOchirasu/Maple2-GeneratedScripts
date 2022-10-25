""" trigger/02000177_bf/horus.xml """
import common


class Horus(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=710, boxId=1):
            return Horus_move_01(self.ctx)


class Horus_move_01(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20001772, textId=20001772, duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Horus_01_broken(self.ctx)


class Horus_01_broken(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=999, patrolName='MS2PatrolData_2004')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Horus_01_End(self.ctx)


class Horus_01_End(common.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[3001], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2300):
            return Horus_01_End_02(self.ctx)
        if self.count_users(boxId=711, boxId=1):
            return Horus_move_02(self.ctx)


class Horus_01_End_02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[999])

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=711, boxId=1):
            return Horus_move_02(self.ctx)


class Horus_move_02(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20001772, textId=20001772, duration=5000)
        self.create_monster(spawnIds=[998], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=751, spawnIds=[998]):
            return Horus_02_End(self.ctx)
        if self.object_interacted(interactIds=[10001060], stateValue=2):
            return Horus_move_03(self.ctx)


class Horus_02_End(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[998])

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=752, boxId=1):
            return Horus_move_03(self.ctx)


class Horus_move_03(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20001772, textId=20001772, duration=5000)
        self.create_monster(spawnIds=[997], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=753, spawnIds=[997]):
            return Horus_03_End(self.ctx)


class Horus_03_End(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[997])


initial_state = Horus
