""" trigger/02000540_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_ambient_light(primary=[132,195,255], secondary=[0,0,0], tertiary=[0,0,0])
        self.set_directional_light(diffuseColor=[163,115,143], specularColor=[140,140,140])
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=6002, visible=False)
        self.set_portal(portalId=6003, visible=False)
        self.set_portal(portalId=6004, visible=False)
        self.set_portal(portalId=6005, visible=False)
        self.set_interact_object(triggerIds=[10003138], state=0)
        self.set_interact_object(triggerIds=[10003139], state=0)
        self.set_interact_object(triggerIds=[10003140], state=0)
        self.set_interact_object(triggerIds=[10003141], state=0)
        self.enable_spawn_point_pc(spawnId=0, isEnable=True)
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.set_effect(triggerIds=[9000], visible=False)
        self.set_effect(triggerIds=[9001], visible=False)
        self.set_effect(triggerIds=[9002], visible=False)
        self.set_effect(triggerIds=[9003], visible=False)
        self.set_effect(triggerIds=[8000], visible=True)
        self.set_effect(triggerIds=[8001], visible=False)
        self.set_effect(triggerIds=[8002], visible=False)
        self.set_effect(triggerIds=[8003], visible=False)
        self.set_effect(triggerIds=[8004], visible=False)
        self.set_effect(triggerIds=[8005], visible=False)
        self.set_effect(triggerIds=[8006], visible=False)
        self.set_effect(triggerIds=[8007], visible=False)
        self.set_effect(triggerIds=[8008], visible=False)
        self.create_monster(spawnIds=[614], animationEffect=True)
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=104, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=105, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[8000], visible=True)
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__0$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[708], jobCode=0):
            return 전투판으로이동하면(self.ctx)


class 전투판으로이동하면(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[601,6011,6012], animationEffect=True)
        self.add_balloon_talk(spawnId=601, msg='$02000540_BF__MAIN__1$', duration=3500, delayTick=0)
        self.add_balloon_talk(spawnId=6011, msg='$02000540_BF__MAIN__2$', duration=3500, delayTick=1500)
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000540_BF__MAIN__3$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[709], jobCode=0):
            return 전투판으로이동하면2(self.ctx)


class 전투판으로이동하면2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[602,6021,6022,603], animationEffect=True)
        self.add_balloon_talk(spawnId=603, msg='$02000540_BF__MAIN__4$', duration=3500, delayTick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[601,6011,6012,602,6021,6022,603]):
            return 첫번째오브젝트조사(self.ctx)


class 첫번째오브젝트조사(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__5$', arg3='3000')
        self.set_interact_object(triggerIds=[10003138], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003138], stateValue=0):
            return 첫번째불켰음(self.ctx)


class 첫번째불켰음(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8001], visible=True)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__6$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[704], jobCode=0):
            return 두번째몬스터생성(self.ctx)


class 두번째몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[9000], visible=False)
        self.create_monster(spawnIds=[604,6041,6042], animationEffect=False)
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000540_BF__MAIN__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[710], jobCode=0):
            return 두번째전투판으로이동하면(self.ctx)


class 두번째전투판으로이동하면(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[605,6051,6052,606], animationEffect=True)
        self.add_balloon_talk(spawnId=606, msg='$02000540_BF__MAIN__8$', duration=3500, delayTick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[604,6041,6042,605,6051,6052,606]):
            return 두번째오브젝트조사(self.ctx)


class 두번째오브젝트조사(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__9$', arg3='3000')
        self.set_interact_object(triggerIds=[10003139], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003139], stateValue=0):
            return 세번째전투판체크(self.ctx)


class 세번째전투판체크(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8002], visible=True)
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__10$', arg3='3000')
        self.set_effect(triggerIds=[8005], visible=True)
        self.set_effect(triggerIds=[8006], visible=True)
        self.set_portal(portalId=6002, visible=True)
        self.set_portal(portalId=6003, visible=True)
        self.add_balloon_talk(spawnId=614, msg='$02000540_BF__MAIN__11$', duration=6500, delayTick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[705], jobCode=0):
            return 세번째몬스터생성(self.ctx)


class 세번째몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[9001], visible=False)
        self.create_monster(spawnIds=[607,6071,6072], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[711], jobCode=0):
            return 세번째전투판으로이동하면(self.ctx)


class 세번째전투판으로이동하면(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[608,6081,6082,609], animationEffect=True)
        self.add_balloon_talk(spawnId=609, msg='$02000540_BF__MAIN__12$', duration=3500, delayTick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[607,6071,6072,608,6081,6082,609]):
            return 세번째오브젝트조사(self.ctx)


class 세번째오브젝트조사(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__13$', arg3='3000')
        self.set_interact_object(triggerIds=[10003140], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003140], stateValue=0):
            return 네번째전투판체크(self.ctx)


class 네번째전투판체크(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8003], visible=True)
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__14$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[706], jobCode=0):
            return 네번째몬스터생성(self.ctx)


class 네번째몬스터생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[9002], visible=False)
        self.create_monster(spawnIds=[610,6101,6102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[712], jobCode=0):
            return 네번째전투판으로이동하면(self.ctx)


class 네번째전투판으로이동하면(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[611,6111,6112,612], animationEffect=True)
        self.add_balloon_talk(spawnId=612, msg='$02000540_BF__MAIN__15$', duration=3500, delayTick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[610,6101,6102,611,6111,6112,612]):
            return 네번째오브젝트조사(self.ctx)


class 네번째오브젝트조사(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__16$', arg3='3000')
        self.set_interact_object(triggerIds=[10003141], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003141], stateValue=0):
            return 보스전투판완성시키기(self.ctx)


class 보스전투판완성시키기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8004], visible=True)
        self.set_onetime_effect(id=104, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_event_ui(type=1, arg2='$02000540_BF__MAIN__17$', arg3='3000')
        self.set_ambient_light(primary=[237,225,255], secondary=[0,0,0], tertiary=[0,0,0])
        self.set_directional_light(diffuseColor=[232,212,127], specularColor=[140,140,140])
        self.set_portal(portalId=6004, visible=True)
        self.set_portal(portalId=6005, visible=True)
        self.set_effect(triggerIds=[8007], visible=True)
        self.set_effect(triggerIds=[8008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보스등장전에(self.ctx)


class 보스등장전에(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000540_BF__MAIN__18$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[707], jobCode=0):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[9003], visible=False)
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=1, isEnable=True)
        self.set_onetime_effect(id=105, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000540_BF__MAIN__19$')
        self.create_monster(spawnIds=[613], animationEffect=True)
        self.set_portal(portalId=6005, visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[613]):
            return 다리생성(self.ctx)


class 다리생성(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000540_BF__MAIN__20$')
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = idle
