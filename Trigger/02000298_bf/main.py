""" trigger/02000298_bf/main.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[11000004], state=2)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3221,3222,3223], visible=False, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[2099], animationEffect=False)
        self.set_npc_emotion_loop(spawnId=2099, sequenceName='Idle_A', duration=9999999)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_skip(state=암호발급)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라이동(self.ctx)


class 카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # Missing State: State
        self.set_skip()
        self.select_camera(triggerId=300, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라이동후UI노출(self.ctx)


class 카메라이동후UI노출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.add_buff(boxIds=[199], skillId=70000107, level=1, isPlayer=False, isSkillSet=False)
        self.show_guide_summary(entityId=20002991, textId=20002991, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return NPC이동(self.ctx)


class NPC이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=2099, patrolName='MS2PatrolData_2099_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 던전안내01(self.ctx)


class 던전안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3221,3222,3223], visible=True, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000372], state=1)
        self.show_guide_summary(entityId=20002980, textId=20002980, duration=5000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.select_camera(triggerId=301, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 던전안내카메라이동(self.ctx)


class 던전안내카메라이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 던전안내02(self.ctx)


class 던전안내02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entityId=20002981, textId=20002981, duration=4000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_interact_object(triggerIds=[10000372], state=0)
            return 암호발급(self.ctx)


class 암호발급(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_buff(boxId=199, skillId=70000107)
        self.destroy_monster(spawnIds=[2099])
        self.select_camera(triggerId=302, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[601], visible=True)
        self.set_mesh(triggerIds=[3001,3002,3003,3004,3005], visible=False, arg3=0, delay=0, scale=5)
        self.set_mesh(triggerIds=[3221,3222,3223], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.random_condition(rate=5):
            return 소환1279(self.ctx)
        if self.random_condition(rate=5):
            return 소환1238(self.ctx)
        if self.random_condition(rate=5):
            return 소환1358(self.ctx)
        if self.random_condition(rate=5):
            return 소환1489(self.ctx)
        if self.random_condition(rate=5):
            return 소환1567(self.ctx)
        if self.random_condition(rate=5):
            return 소환1679(self.ctx)
        if self.random_condition(rate=5):
            return 소환2389(self.ctx)
        if self.random_condition(rate=5):
            return 소환2347(self.ctx)
        if self.random_condition(rate=5):
            return 소환2478(self.ctx)
        if self.random_condition(rate=5):
            return 소환2456(self.ctx)
        if self.random_condition(rate=5):
            return 소환2569(self.ctx)
        if self.random_condition(rate=5):
            return 소환2678(self.ctx)
        if self.random_condition(rate=5):
            return 소환3458(self.ctx)
        if self.random_condition(rate=5):
            return 소환3589(self.ctx)
        if self.random_condition(rate=5):
            return 소환3679(self.ctx)
        if self.random_condition(rate=5):
            return 소환3789(self.ctx)
        if self.random_condition(rate=5):
            return 소환4567(self.ctx)
        if self.random_condition(rate=5):
            return 소환4578(self.ctx)
        if self.random_condition(rate=5):
            return 소환4689(self.ctx)
        if self.random_condition(rate=5):
            return 소환4789(self.ctx)


class 소환1279(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[1279], animationEffect=False)
            return 종료(self.ctx)


class 소환1238(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[1238], animationEffect=False)
            return 종료(self.ctx)


class 소환1358(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[1358], animationEffect=False)
            return 종료(self.ctx)


class 소환1489(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[1489], animationEffect=False)
            return 종료(self.ctx)


class 소환1567(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[1567], animationEffect=False)
            return 종료(self.ctx)


class 소환1679(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[1679], animationEffect=False)
            return 종료(self.ctx)


class 소환2389(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[2389], animationEffect=False)
            return 종료(self.ctx)


class 소환2347(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[2347], animationEffect=False)
            return 종료(self.ctx)


class 소환2478(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[2478], animationEffect=False)
            return 종료(self.ctx)


class 소환2456(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[2456], animationEffect=False)
            return 종료(self.ctx)


class 소환2569(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[2569], animationEffect=False)
            return 종료(self.ctx)


class 소환2678(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[2678], animationEffect=False)
            return 종료(self.ctx)


class 소환3458(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[3458], animationEffect=False)
            return 종료(self.ctx)


class 소환3589(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[3589], animationEffect=False)
            return 종료(self.ctx)


class 소환3679(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[3679], animationEffect=False)
            return 종료(self.ctx)


class 소환3789(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[3789], animationEffect=False)
            return 종료(self.ctx)


class 소환4567(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[4567], animationEffect=False)
            return 종료(self.ctx)


class 소환4578(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[4578], animationEffect=False)
            return 종료(self.ctx)


class 소환4689(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[4689], animationEffect=False)
            return 종료(self.ctx)


class 소환4789(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            self.create_monster(spawnIds=[4789], animationEffect=False)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
