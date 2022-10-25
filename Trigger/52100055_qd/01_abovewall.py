""" trigger/52100055_qd/01_abovewall.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000], visible=True, arg3=0, delay=0, scale=0) # InvisibleMesh_forTransparancy
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10002101], state=0) # LeverForLadder01
        self.set_interact_object(triggerIds=[10002102], state=0) # LeverForRope
        self.set_interact_object(triggerIds=[10002103], state=0) # LeverForLadder02
        self.destroy_monster(spawnIds=[901,902,903]) # Mob
        self.destroy_monster(spawnIds=[910,911,912,920,921,922,930,931,932,940,941,942]) # Mob
        self.set_ladder(triggerIds=[510], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[511], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[512], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[513], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[514], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        self.set_ladder(triggerIds=[520], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[521], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[522], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[523], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[524], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[525], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[526], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[527], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_ladder(triggerIds=[528], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        self.set_rope(triggerId=530, visible=False, animationEffect=False, animationDelay=0) # Rope
        self.set_rope(triggerId=531, visible=False, animationEffect=False, animationDelay=0) # Rope
        self.set_rope(triggerId=532, visible=False, animationEffect=False, animationDelay=0) # Rope
        self.set_rope(triggerId=533, visible=False, animationEffect=False, animationDelay=0) # Rope
        self.set_rope(triggerId=534, visible=False, animationEffect=False, animationDelay=0) # Rope
        self.set_rope(triggerId=535, visible=False, animationEffect=False, animationDelay=0) # Rope
        self.set_rope(triggerId=536, visible=False, animationEffect=False, animationDelay=0) # Rope
        self.set_rope(triggerId=537, visible=False, animationEffect=False, animationDelay=0) # Rope
        self.set_rope(triggerId=538, visible=False, animationEffect=False, animationDelay=0) # Rope
        self.set_rope(triggerId=539, visible=False, animationEffect=False, animationDelay=0) # Rope

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return LoadingDelay(self.ctx)


class LoadingDelay(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return GuideToMove(self.ctx)


class GuideToMove(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039901, textId=20039901, duration=3000) # 가이드 : 성벽을 따라 다음 탑으로 이동하세요.

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9100]):
            return MobActorSpawn(self.ctx)


class MobActorSpawn(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[901,902,903], animationEffect=False) # Mob
        self.set_conversation(type=1, spawnId=901, script='$52100055_QD__01_ABOVEWALL__0$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=902, script='$52100055_QD__01_ABOVEWALL__0$', arg4=2, arg5=1)
        self.set_conversation(type=1, spawnId=903, script='$52100055_QD__01_ABOVEWALL__0$', arg4=2, arg5=1)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return Battle01Start(self.ctx)


class Battle01Start(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[930,931,932], animationEffect=False) # Mob
        self.set_interact_object(triggerIds=[10002101], state=1) # LeverForLadder01

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002101], stateValue=0):
            return Battle02Start(self.ctx)


class Battle02Start(common.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039902, textId=20039902, duration=3000) # 가이드 : 사다리를 타고 위로 올라가세요.
        self.set_ladder(triggerIds=[510], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        self.set_ladder(triggerIds=[511], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        self.set_ladder(triggerIds=[512], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        self.set_ladder(triggerIds=[513], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        self.set_ladder(triggerIds=[514], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        self.set_ladder(triggerIds=[520], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        self.create_monster(spawnIds=[910,911,912], animationEffect=False) # Mob

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9300]):
            return Battle03Start(self.ctx)


class Battle03Start(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=2, key='TireSpawn', value=1)
        self.create_monster(spawnIds=[920,921,922], animationEffect=False) # Mob
        self.set_interact_object(triggerIds=[10002102], state=1) # LeverForRope

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002102], stateValue=0):
            return RopeOn(self.ctx)


class RopeOn(common.Trigger):
    def on_enter(self):
        self.set_rope(triggerId=530, visible=True, animationEffect=True, animationDelay=2) # Rope
        self.set_rope(triggerId=531, visible=True, animationEffect=True, animationDelay=2) # Rope
        self.set_rope(triggerId=532, visible=True, animationEffect=True, animationDelay=2) # Rope
        self.set_rope(triggerId=533, visible=True, animationEffect=True, animationDelay=2) # Rope
        self.set_rope(triggerId=534, visible=True, animationEffect=True, animationDelay=2) # Rope
        self.set_rope(triggerId=535, visible=True, animationEffect=True, animationDelay=2) # Rope
        self.set_rope(triggerId=536, visible=True, animationEffect=True, animationDelay=2) # Rope
        self.set_rope(triggerId=537, visible=True, animationEffect=True, animationDelay=2) # Rope
        self.set_rope(triggerId=538, visible=True, animationEffect=True, animationDelay=2) # Rope
        self.set_rope(triggerId=539, visible=True, animationEffect=True, animationDelay=2) # Rope
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039906, textId=20039906) # 가이드 : 로프를 타고 탑 위층으로 올라가세요.

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9200]):
            return Battle04Start(self.ctx)


class Battle04Start(common.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20039906)
        self.create_monster(spawnIds=[940,941,942], animationEffect=False) # Mob
        self.set_interact_object(triggerIds=[10002103], state=1) # LeverForLadder02

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002103], stateValue=0):
            return PortalOn(self.ctx)


class PortalOn(common.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[520], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        self.set_ladder(triggerIds=[521], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        self.set_ladder(triggerIds=[522], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        self.set_ladder(triggerIds=[523], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        self.set_ladder(triggerIds=[524], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        self.set_ladder(triggerIds=[525], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        self.set_ladder(triggerIds=[526], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        self.set_ladder(triggerIds=[527], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        self.set_ladder(triggerIds=[528], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20039804, textId=20039804, duration=5000) # 가이드 : 사다리를 타고 위로 올라가세요.
        self.set_portal(portalId=2, visible=False, enable=True, minimapVisible=False)


initial_state = Wait
