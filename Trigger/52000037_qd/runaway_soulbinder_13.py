""" trigger/52000037_qd/runaway_soulbinder_13.xml """
import common


class Wait(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9400], questIds=[50001411], questStates=[2], jobCode=110):
            return 연출시작(self.ctx)


class 연출시작(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=603, enable=True)
        self.move_user(mapId=52000037, portalId=11)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=100):
            return PC말풍선딜레이(self.ctx)


class PC말풍선딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.move_user_path(patrolName='MS2PatrolData_PC1102A')
            return PC말풍선01(self.ctx)


class PC말풍선01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__0$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선02(self.ctx)


class PC말풍선02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__1$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선03(self.ctx)


class PC말풍선03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__2$', arg4=4, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 말풍선딜레이(self.ctx)


class 말풍선딜레이(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            self.move_user_path(patrolName='MS2PatrolData_PC1102B')
            return PC말풍선04(self.ctx)


class PC말풍선04(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__3$', arg4=4, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return PC말풍선05(self.ctx)


class PC말풍선05(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__4$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return NPC등장(self.ctx)


class NPC등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[211,212,213], animationEffect=False)
        self.select_camera(triggerId=604, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return NPC대사01(self.ctx)


class NPC대사01(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001727, script='$52000037_QD__RUNAWAY_SOULBINDER_13__5$', arg4=2)
        self.set_skip(state=NPC대사01스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return NPC대사02(self.ctx)


class NPC대사01스킵(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return NPC대사02(self.ctx)


class NPC대사02(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001725, script='$52000037_QD__RUNAWAY_SOULBINDER_13__6$', arg4=2)
        self.set_skip(state=NPC대사02스킵)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PC도주(self.ctx)


class NPC대사02스킵(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return PC도주(self.ctx)


class PC도주(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.select_camera(triggerId=605, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_PC1102C')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return PC말풍선06(self.ctx)


class PC말풍선06(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=211, patrolName='MS2PatrolData_NPC1102')
        self.move_npc(spawnId=212, patrolName='MS2PatrolData_NPC1102')
        self.move_npc(spawnId=213, patrolName='MS2PatrolData_NPC1102')
        self.set_conversation(type=1, spawnId=0, script='$52000037_QD__RUNAWAY_SOULBINDER_13__7$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 연출종료(self.ctx)


class 연출종료(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=2000043, portalId=5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = Wait
