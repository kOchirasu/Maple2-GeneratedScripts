""" trigger/02000399_bf/01_abovewall.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3000], visible=True, arg3=0, arg4=0, arg5=0) # InvisibleMesh_forTransparancy
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10001150], state=0) # LeverForLadder01
        set_interact_object(triggerIds=[10001151], state=0) # LeverForRope
        set_interact_object(triggerIds=[10001152], state=0) # LeverForLadder02
        destroy_monster(spawnIds=[901,902,903]) # Mob
        destroy_monster(spawnIds=[910,911,912,920,921,922,930,931,932,940,941,942]) # Mob
        set_ladder(triggerIds=[510], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[511], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[512], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[513], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[514], visible=False, animationEffect=False, animationDelay=0) # Ladder01
        set_ladder(triggerIds=[520], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[521], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[522], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[523], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[524], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[525], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[526], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[527], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_ladder(triggerIds=[528], visible=False, animationEffect=False, animationDelay=0) # Ladder02
        set_rope(triggerId=530, visible=False, animationEffect=False, animationDelay=0) # Rope
        set_rope(triggerId=531, visible=False, animationEffect=False, animationDelay=0) # Rope
        set_rope(triggerId=532, visible=False, animationEffect=False, animationDelay=0) # Rope
        set_rope(triggerId=533, visible=False, animationEffect=False, animationDelay=0) # Rope
        set_rope(triggerId=534, visible=False, animationEffect=False, animationDelay=0) # Rope
        set_rope(triggerId=535, visible=False, animationEffect=False, animationDelay=0) # Rope
        set_rope(triggerId=536, visible=False, animationEffect=False, animationDelay=0) # Rope
        set_rope(triggerId=537, visible=False, animationEffect=False, animationDelay=0) # Rope
        set_rope(triggerId=538, visible=False, animationEffect=False, animationDelay=0) # Rope
        set_rope(triggerId=539, visible=False, animationEffect=False, animationDelay=0) # Rope

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GuideToMove()


class GuideToMove(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039901, textId=20039901, duration=3000) # 가이드 : 성벽을 따라 다음 탑으로 이동하세요.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return MobActorSpawn()


class MobActorSpawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[901,902,903], arg2=False) # Mob
        set_conversation(type=1, spawnId=901, script='$02000399_BF__01_ABOVEWALL__0$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=902, script='$02000399_BF__01_ABOVEWALL__1$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=903, script='$02000399_BF__01_ABOVEWALL__2$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Battle01Start()


class Battle01Start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[930,931,932], arg2=False) # Mob
        set_interact_object(triggerIds=[10001150], state=1) # LeverForLadder01

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001150], arg2=0):
            return Battle02Start()


class Battle02Start(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039902, textId=20039902, duration=3000) # 가이드 : 사다리를 타고 위로 올라가세요.
        set_ladder(triggerIds=[510], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        set_ladder(triggerIds=[511], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        set_ladder(triggerIds=[512], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        set_ladder(triggerIds=[513], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        set_ladder(triggerIds=[514], visible=True, animationEffect=True, animationDelay=2) # Ladder01
        set_ladder(triggerIds=[520], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        create_monster(spawnIds=[910,911,912], arg2=False) # Mob

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9300]):
            return Battle03Start()


class Battle03Start(state.State):
    def on_enter(self):
        set_user_value(triggerId=2, key='TireSpawn', value=1)
        create_monster(spawnIds=[920,921,922], arg2=False) # Mob
        set_interact_object(triggerIds=[10001151], state=1) # LeverForRope

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001151], arg2=0):
            return RopeOn()


class RopeOn(state.State):
    def on_enter(self):
        set_rope(triggerId=530, visible=True, animationEffect=True, animationDelay=2) # Rope
        set_rope(triggerId=531, visible=True, animationEffect=True, animationDelay=2) # Rope
        set_rope(triggerId=532, visible=True, animationEffect=True, animationDelay=2) # Rope
        set_rope(triggerId=533, visible=True, animationEffect=True, animationDelay=2) # Rope
        set_rope(triggerId=534, visible=True, animationEffect=True, animationDelay=2) # Rope
        set_rope(triggerId=535, visible=True, animationEffect=True, animationDelay=2) # Rope
        set_rope(triggerId=536, visible=True, animationEffect=True, animationDelay=2) # Rope
        set_rope(triggerId=537, visible=True, animationEffect=True, animationDelay=2) # Rope
        set_rope(triggerId=538, visible=True, animationEffect=True, animationDelay=2) # Rope
        set_rope(triggerId=539, visible=True, animationEffect=True, animationDelay=2) # Rope
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039906, textId=20039906) # 가이드 : 로프를 타고 탑 위층으로 올라가세요.

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9200]):
            return Battle04Start()


class Battle04Start(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20039906)
        create_monster(spawnIds=[940,941,942], arg2=False) # Mob
        set_interact_object(triggerIds=[10001152], state=1) # LeverForLadder02

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001152], arg2=0):
            return PortalOn()


class PortalOn(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[520], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        set_ladder(triggerIds=[521], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        set_ladder(triggerIds=[522], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        set_ladder(triggerIds=[523], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        set_ladder(triggerIds=[524], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        set_ladder(triggerIds=[525], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        set_ladder(triggerIds=[526], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        set_ladder(triggerIds=[527], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        set_ladder(triggerIds=[528], visible=True, animationEffect=True, animationDelay=2) # Ladder02
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20039804, textId=20039804, duration=5000) # 가이드 : 사다리를 타고 위로 올라가세요.
        set_portal(portalId=2, visible=False, enabled=True, minimapVisible=False)


