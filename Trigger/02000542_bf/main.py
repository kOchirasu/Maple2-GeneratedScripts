""" trigger/02000542_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.enable_spawn_point_pc(spawnId=0, isEnable=True)
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.set_interact_object(triggerIds=[10003142], state=1)
        self.set_interact_object(triggerIds=[10003143], state=0)
        self.set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618], visible=True)
        self.set_mesh(triggerIds=[619,620,621,622,623,624,625,626,627], visible=True)
        self.set_mesh(triggerIds=[628,629,630,631,632,633,634,635,636], visible=True)
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[707], jobCode=0):
            return 문열기오브젝트설정1(self.ctx)


class 문열기오브젝트설정1(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000542_BF__MAIN__0$', arg3='5000')
        self.set_interact_object(triggerIds=[10003142], state=1)
        self.create_monster(spawnIds=[112], animationEffect=False)
        self.add_balloon_talk(spawnId=112, msg='$02000542_BF__MAIN__1$', duration=3500, delayTick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003142], stateValue=0):
            return 감옥문부시기1(self.ctx)


class 감옥문부시기1(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__2$')
        self.destroy_monster(spawnIds=[112])
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(triggerIds=[609], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=0):
            return 몬스터생성하기1(self.ctx)


class 몬스터생성하기1(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 문을열자1(self.ctx)


class 문을열자1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 감옥문부시기2(self.ctx)


class 감옥문부시기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[605], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[702], jobCode=0):
            return 몬스터생성하기2(self.ctx)


class 몬스터생성하기2(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__3$')
        self.create_monster(spawnIds=[102], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[703], jobCode=0):
            return 몬스터생성하기3(self.ctx)


class 몬스터생성하기3(trigger_api.Trigger):
    def on_enter(self):
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__4$')
        self.create_monster(spawnIds=[103], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[704], jobCode=0):
            return 몬스터생성하기4(self.ctx)


class 몬스터생성하기4(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[104], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[102,103,104]):
            return 문열기오브젝트설정2(self.ctx)


class 문열기오브젝트설정2(trigger_api.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000542_BF__MAIN__5$', arg3='5000')
        self.set_interact_object(triggerIds=[10003143], state=1)
        self.create_monster(spawnIds=[113], animationEffect=False)
        self.add_balloon_talk(spawnId=113, msg='$02000542_BF__MAIN__6$', duration=3500)
        self.add_balloon_talk(spawnId=113, msg='$02000542_BF__MAIN__7$', duration=3500, delayTick=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10003143], stateValue=0):
            return 감옥문부시기3(self.ctx)


class 감옥문부시기3(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(triggerIds=[604], visible=False)
        self.destroy_monster(spawnIds=[113])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[708], jobCode=0):
            return 감옥문부시기4(self.ctx)


class 감옥문부시기4(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[116], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[116]):
            return 감옥문부시기5(self.ctx)


class 감옥문부시기5(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[607], visible=False)
        self.create_monster(spawnIds=[121], animationEffect=False)
        self.add_balloon_talk(spawnId=121, msg='$02000542_BF__MAIN__8$', duration=8500, delayTick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[709], jobCode=0):
            return 감옥문부시기6(self.ctx)


class 감옥문부시기6(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[121])
        self.set_mesh(triggerIds=[612], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[705], jobCode=0):
            return 연출NPC스폰(self.ctx)


class 연출NPC스폰(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.create_monster(spawnIds=[105,111], animationEffect=False)
        self.add_balloon_talk(spawnId=105, msg='$02000542_BF__MAIN__9$', duration=3500)
        self.add_balloon_talk(spawnId=105, msg='$02000542_BF__MAIN__10$', duration=4500, delayTick=3500)
        self.add_balloon_talk(spawnId=111, msg='$02000542_BF__MAIN__11$', duration=3500, delayTick=300)
        self.add_balloon_talk(spawnId=111, msg='$02000542_BF__MAIN__12$', duration=4500, delayTick=3800)
        self.create_monster(spawnIds=[114], animationEffect=False)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000542_BF__MAIN__13$')
        self.add_balloon_talk(spawnId=114, msg='$02000542_BF__MAIN__14$', duration=4500, delayTick=1000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[706], jobCode=0):
            return 몬스터다수생성하기(self.ctx)


class 몬스터다수생성하기(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[114])
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=1, isEnable=True)
        self.create_monster(spawnIds=[106,107,108,109], animationEffect=False)
        self.create_monster(spawnIds=[117,118,119,120], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[106,107,108,109]):
            return 보스스폰(self.ctx)


class 보스스폰(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.add_balloon_talk(spawnId=117, msg='$02000542_BF__MAIN__15$', duration=8500, delayTick=500)
        self.add_balloon_talk(spawnId=118, msg='$02000542_BF__MAIN__16$', duration=8500, delayTick=1000)
        self.add_balloon_talk(spawnId=119, msg='$02000542_BF__MAIN__17$', duration=8500, delayTick=1000)
        self.add_balloon_talk(spawnId=120, msg='$02000542_BF__MAIN__18$', duration=8500, delayTick=800)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000542_BF__MAIN__19$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보스스폰2(self.ctx)


class 보스스폰2(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.create_monster(spawnIds=[110], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[110]):
            return 포탈열기(self.ctx)


class 포탈열기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 포탈열기2(self.ctx)


class 포탈열기2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[115], animationEffect=False)
        self.destroy_monster(spawnIds=[117,118,119,120])
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__20$')
        self.add_balloon_talk(spawnId=115, msg='$02000542_BF__MAIN__21$', duration=3500, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 포탈열기3(self.ctx)


class 포탈열기3(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(triggerIds=[601,602], visible=False)
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.destroy_monster(spawnIds=[115])


initial_state = idle
