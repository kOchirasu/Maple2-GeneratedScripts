""" trigger/02000542_bf/main.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        enable_spawn_point_pc(spawnId=0, isEnable=True)
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        set_interact_object(triggerIds=[10003142], state=1)
        set_interact_object(triggerIds=[10003143], state=0)
        set_mesh(triggerIds=[601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618], visible=True)
        set_mesh(triggerIds=[619,620,621,622,623,624,625,626,627], visible=True)
        set_mesh(triggerIds=[628,629,630,631,632,633,634,635,636], visible=True)
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[707], jobCode=0):
            return 문열기오브젝트설정1()


class 문열기오브젝트설정1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000542_BF__MAIN__0$', arg3='5000')
        set_interact_object(triggerIds=[10003142], state=1)
        create_monster(spawnIds=[112], arg2=False)
        add_balloon_talk(spawnId=112, msg='$02000542_BF__MAIN__1$', duration=3500, delayTick=1500)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10003142], arg2=0):
            return 감옥문부시기1()


class 감옥문부시기1(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__2$')
        destroy_monster(spawnIds=[112])
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_mesh(triggerIds=[609], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701], jobCode=0):
            return 몬스터생성하기1()


class 몬스터생성하기1(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 문을열자1()


class 문을열자1(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 감옥문부시기2()


class 감옥문부시기2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[605], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702], jobCode=0):
            return 몬스터생성하기2()


class 몬스터생성하기2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__3$')
        create_monster(spawnIds=[102], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[703], jobCode=0):
            return 몬스터생성하기3()


class 몬스터생성하기3(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__4$')
        create_monster(spawnIds=[103], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[704], jobCode=0):
            return 몬스터생성하기4()


class 몬스터생성하기4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102,103,104]):
            return 문열기오브젝트설정2()


class 문열기오브젝트설정2(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000542_BF__MAIN__5$', arg3='5000')
        set_interact_object(triggerIds=[10003143], state=1)
        create_monster(spawnIds=[113], arg2=False)
        add_balloon_talk(spawnId=113, msg='$02000542_BF__MAIN__6$', duration=3500)
        add_balloon_talk(spawnId=113, msg='$02000542_BF__MAIN__7$', duration=3500, delayTick=3500)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10003143], arg2=0):
            return 감옥문부시기3()


class 감옥문부시기3(state.State):
    def on_enter(self):
        set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_mesh(triggerIds=[604], visible=False)
        destroy_monster(spawnIds=[113])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[708], jobCode=0):
            return 감옥문부시기4()


class 감옥문부시기4(state.State):
    def on_enter(self):
        create_monster(spawnIds=[116], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[116]):
            return 감옥문부시기5()


class 감옥문부시기5(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[607], visible=False)
        create_monster(spawnIds=[121], arg2=False)
        add_balloon_talk(spawnId=121, msg='$02000542_BF__MAIN__8$', duration=8500, delayTick=1000)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[709], jobCode=0):
            return 감옥문부시기6()


class 감옥문부시기6(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[121])
        set_mesh(triggerIds=[612], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[705], jobCode=0):
            return 연출NPC스폰()


class 연출NPC스폰(state.State):
    def on_enter(self):
        set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        create_monster(spawnIds=[105,111], arg2=False)
        add_balloon_talk(spawnId=105, msg='$02000542_BF__MAIN__9$', duration=3500)
        add_balloon_talk(spawnId=105, msg='$02000542_BF__MAIN__10$', duration=4500, delayTick=3500)
        add_balloon_talk(spawnId=111, msg='$02000542_BF__MAIN__11$', duration=3500, delayTick=300)
        add_balloon_talk(spawnId=111, msg='$02000542_BF__MAIN__12$', duration=4500, delayTick=3800)
        create_monster(spawnIds=[114], arg2=False)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000542_BF__MAIN__13$')
        add_balloon_talk(spawnId=114, msg='$02000542_BF__MAIN__14$', duration=4500, delayTick=1000)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[706], jobCode=0):
            return 몬스터다수생성하기()


class 몬스터다수생성하기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[114])
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=1, isEnable=True)
        create_monster(spawnIds=[106,107,108,109], arg2=False)
        create_monster(spawnIds=[117,118,119,120], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106,107,108,109]):
            return 보스스폰()


class 보스스폰(state.State):
    def on_enter(self):
        set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        add_balloon_talk(spawnId=117, msg='$02000542_BF__MAIN__15$', duration=8500, delayTick=500)
        add_balloon_talk(spawnId=118, msg='$02000542_BF__MAIN__16$', duration=8500, delayTick=1000)
        add_balloon_talk(spawnId=119, msg='$02000542_BF__MAIN__17$', duration=8500, delayTick=1000)
        add_balloon_talk(spawnId=120, msg='$02000542_BF__MAIN__18$', duration=8500, delayTick=800)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000542_BF__MAIN__19$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 보스스폰2()


class 보스스폰2(state.State):
    def on_enter(self):
        set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        create_monster(spawnIds=[110], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[110]):
            return 포탈열기()


class 포탈열기(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 포탈열기2()


class 포탈열기2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[115], arg2=False)
        destroy_monster(spawnIds=[117,118,119,120])
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000542_BF__MAIN__20$')
        add_balloon_talk(spawnId=115, msg='$02000542_BF__MAIN__21$', duration=3500, delayTick=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 포탈열기3()


class 포탈열기3(state.State):
    def on_enter(self):
        set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_mesh(triggerIds=[601,602], visible=False)
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        destroy_monster(spawnIds=[115])


