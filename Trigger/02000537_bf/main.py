""" trigger/02000537_bf/main.xml """
from common import *
import state


#  심연의 성채 
#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[5000], visible=True)
        set_mesh(triggerIds=[8900], visible=True)
        set_mesh(triggerIds=[8901], visible=True)
        set_mesh(triggerIds=[8902], visible=True)
        set_mesh(triggerIds=[8903], visible=True)
        set_mesh(triggerIds=[8904], visible=True)
        set_mesh(triggerIds=[8905], visible=True)
        set_effect(triggerIds=[8000], visible=False)
        set_effect(triggerIds=[8001], visible=False)
        set_skill(triggerIds=[9000], isEnable=False)
        enable_spawn_point_pc(spawnId=0, isEnable=True)
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=False)
        enable_spawn_point_pc(spawnId=3, isEnable=False)
        enable_spawn_point_pc(spawnId=4, isEnable=False)
        enable_spawn_point_pc(spawnId=5, isEnable=False)
        enable_spawn_point_pc(spawnId=6, isEnable=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701], jobCode=0):
            return ready()


#  첫번째 발판
class ready(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000537_BF__MAIN__0$', arg3='3000')
        create_monster(spawnIds=[101,1011,1012,1013,1014,1017,1018,1019], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,1011,1012,1013,1014,1017,1018,1019]):
            return 도마뱀스폰1()


class 도마뱀스폰1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8900], visible=False)
        create_monster(spawnIds=[1015,1016], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702], jobCode=0):
            return 시작702()


class 시작702(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=1, isEnable=True)
        create_monster(spawnIds=[102,1022,1023,1024,1025], arg2=True)
        side_npc_talk(npcId=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='$02000537_BF__MAIN__1$')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102,1022,1023,1024,1025]):
            return 마무리1_702()


class 마무리1_702(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8901], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마무리2_702()


class 마무리2_702(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__2$')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[703], jobCode=0):
            return 시작703()


class 시작703(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1026])
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 진행703()


class 진행703(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000537_BF__MAIN__3$', arg3='3000')
        create_monster(spawnIds=[109], arg2=True)
        create_monster(spawnIds=[103,1031,1032,1033,1034], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103,1031,1032,1033,1034]):
            return 마무리1_703()


class 마무리1_703(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8902], visible=False)
        create_monster(spawnIds=[1035], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 마무리2_703()


class 마무리2_703(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000537_BF__MAIN__4$')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[704], jobCode=0):
            return 시작704()


class 시작704(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=2, isEnable=False)
        enable_spawn_point_pc(spawnId=3, isEnable=True)
        create_monster(spawnIds=[104,1041,1042,1043,1044], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 진행704()


class 진행704(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__5$')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[104,1041,1042,1043,1044]):
            return 마무리704()


class 마무리704(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8903], visible=False)
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__6$')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[705], jobCode=0):
            return 시작705()


class 시작705(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=3, isEnable=False)
        enable_spawn_point_pc(spawnId=4, isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 진행705()


class 진행705(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105,1051,1052,1053,1054], arg2=True)
        side_npc_talk(npcId=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='$02000537_BF__MAIN__7$')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[105,1051,1052,1053,1054]):
            return 마무리705()


class 마무리705(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8904], visible=False)
        create_monster(spawnIds=[1036], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[708], jobCode=0):
            return 버프걸어주기()


class 버프걸어주기(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000537_BF__MAIN__8$')
        set_skill(triggerIds=[9000], isEnable=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[706], jobCode=0):
            return 시작706()


class 시작706(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__9$')
        enable_spawn_point_pc(spawnId=4, isEnable=False)
        enable_spawn_point_pc(spawnId=5, isEnable=True)
        create_monster(spawnIds=[106,1061,1063,1064,1065], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[106,1061,1063,1064,1065]):
            return 마무리706()


class 마무리706(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[8905], visible=False)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000537_BF__MAIN__10$')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[707], jobCode=0):
            return 시작707()


class 시작707(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=5, isEnable=False)
        enable_spawn_point_pc(spawnId=6, isEnable=True)
        create_monster(spawnIds=[108], arg2=True)
        side_npc_talk(npcId=22600006, illust='DesertDragonBigBlue_normal', duration=4000, script='$02000537_BF__MAIN__11$')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[108]):
            return 포털생성전()


class 포털생성전(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[109])
        create_monster(spawnIds=[1091], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 포털생성전2()


class 포털생성전2(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[109])
        create_monster(spawnIds=[1091], arg2=True)
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=4000, script='$02000537_BF__MAIN__12$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 포털생성()


class 포털생성(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


