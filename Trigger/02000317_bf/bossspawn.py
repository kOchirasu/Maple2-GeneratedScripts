""" trigger/02000317_bf/bossspawn.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=6, visible=False, enable=False, minimapVisible=False, arg5=False)
        self.set_portal(portalId=5, visible=False, enable=False, minimapVisible=False, arg5=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False, arg5=False)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=101, boxId=1):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=6, visible=False, enable=False, minimapVisible=False, arg5=False)
        self.set_portal(portalId=5, visible=False, enable=False, minimapVisible=False, arg5=False)
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False, arg5=False)
        self.set_mesh(triggerIds=[2001,2002,2003,2004], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Start(self.ctx)


class Start(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Step_1(self.ctx)


class Step_1(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=3, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[1,2,3,4,5,6,7], visible=False) # 다리안보임
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.create_monster(spawnIds=[203], animationEffect=False)
        self.create_monster(spawnIds=[204], animationEffect=False)
        self.create_monster(spawnIds=[205], animationEffect=False)
        self.create_monster(spawnIds=[206], animationEffect=False)
        self.create_monster(spawnIds=[207], animationEffect=False)
        self.create_monster(spawnIds=[208], animationEffect=False)
        self.create_monster(spawnIds=[301], animationEffect=False)
        self.create_monster(spawnIds=[302], animationEffect=False)
        self.create_monster(spawnIds=[303], animationEffect=False)
        self.create_monster(spawnIds=[304], animationEffect=False)
        self.create_monster(spawnIds=[305], animationEffect=False)
        self.create_monster(spawnIds=[306], animationEffect=False)
        self.create_monster(spawnIds=[307], animationEffect=False)
        self.create_monster(spawnIds=[401], animationEffect=False)
        self.create_monster(spawnIds=[402], animationEffect=False)
        self.create_monster(spawnIds=[403], animationEffect=False)
        self.create_monster(spawnIds=[404], animationEffect=False)
        self.create_monster(spawnIds=[405], animationEffect=False)
        self.create_monster(spawnIds=[406], animationEffect=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[105]):
            return Step_1_B_Ready(self.ctx)
        if self.user_detected(boxIds=[104]):
            return Step_2(self.ctx)


class Step_1_B_Ready(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=100, textId=20031701, duration=3000) # 타우스를 처치하세요.

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[205,208]):
            return Step_1_B(self.ctx)


class Step_1_B(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=3, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[106]):
            return Step_1_C(self.ctx)
        if self.user_detected(boxIds=[104]):
            return Step_2(self.ctx)


class Step_1_C(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=100, textId=20031701, duration=3000) # 타우스를 처치하세요.

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[301,302]):
            return Step_1_D_Ready(self.ctx)
        if self.user_detected(boxIds=[104]):
            return Step_2(self.ctx)


class Step_1_D_Ready(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[8,9,10,11], visible=False) # 다리안보임

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[107]):
            return Step_1_D(self.ctx)
        if self.user_detected(boxIds=[104]):
            return Step_2(self.ctx)


class Step_1_D(common.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=100, textId=20031701, duration=3000) # 타우스를 처치하세요.

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[405]):
            return Step_1_E(self.ctx)
        if self.user_detected(boxIds=[104]):
            return Step_2(self.ctx)


class Step_1_E(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=5, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[104]):
            return Step_2(self.ctx)


class Step_2(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=7, visible=True, enable=True, minimapVisible=True)
        self.create_monster(spawnIds=[100], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[100]):
            return 종료체크(self.ctx)

    def on_exit(self):
        self.destroy_monster(spawnIds=[100])


class 종료체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.dungeon_clear()
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=8, visible=True, enable=True, minimapVisible=True)


initial_state = idle
