""" trigger/02000387_bf/01_playparttimejob.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class Wait(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[2000,2001,2002,2003,2004], visible=True, arg3=0, arg4=0, arg5=0) # Barrier
        set_mesh(triggerIds=[2005], visible=True, arg3=0, arg4=0, arg5=0) # Barrier
        set_mesh(triggerIds=[2006], visible=True, arg3=0, arg4=0, arg5=0) # Barrier
        set_mesh(triggerIds=[2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031], visible=True, arg3=0, arg4=0, arg5=0) # Barrier
        set_actor(triggerId=4000, visible=True, initialSequence='ry_functobj_door_E01_off') # RevolvingDoor
        set_actor(triggerId=4001, visible=True, initialSequence='ry_functobj_door_E01_off') # RevolvingDoor
        set_actor(triggerId=4002, visible=True, initialSequence='ry_functobj_door_E01_off') # RevolvingDoor
        set_actor(triggerId=4003, visible=True, initialSequence='ry_functobj_door_E01_off') # RevolvingDoor
        set_effect(triggerIds=[5000], visible=False) # GuideUI
        set_effect(triggerIds=[5101], visible=False) # DownArrow
        set_effect(triggerIds=[5102], visible=False) # DownArrow
        set_effect(triggerIds=[5103], visible=False) # DownArrow
        set_effect(triggerIds=[5104], visible=False) # DownArrow
        set_effect(triggerIds=[5105], visible=False) # DownArrow
        set_effect(triggerIds=[5106], visible=False) # DownArrow

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay()


class LoadingDelay(state.State):
    def on_enter(self):
        create_monster(spawnIds=[100], arg2=False) # 캐시 카탈리나

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_mini_game_area_for_hack(boxId=9001) # 해킹 보안용 시작 box 설정
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GuideTalk01()

state.DungeonStart = DungeonStart


class GuideTalk01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000491, script='$02000387_BF__01_PLAYPARTTIMEJOB__0$', arg4=4) # 잡담에서 캐시마트에 대해 설명해주기
        set_skip(state=GuideTalk01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GuideTalk01Skip()


class GuideTalk01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return GuideTalk02()


class GuideTalk02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000491, script='$02000387_BF__01_PLAYPARTTIMEJOB__1$', arg4=4)
        set_skip(state=GuideTalk02Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GuideTalk02Skip()


class GuideTalk02Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return GuideTalk03()


class GuideTalk03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000491, script='$02000387_BF__01_PLAYPARTTIMEJOB__2$', arg4=4)
        set_skip(state=GuideTalk03Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GuideTalk03Skip()


class GuideTalk03Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return GuideTalk04()


class GuideTalk04(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000491, script='$02000387_BF__01_PLAYPARTTIMEJOB__3$', arg4=4)
        set_skip(state=GuideTalk04Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GuideTalk04Skip()


class GuideTalk04Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PCPlacement01()


class PCPlacement01(state.State):
    def on_enter(self):
        set_user_value(triggerId=10, key='RandomPortalOn', value=1)

    def on_tick(self) -> state.State:
        if count_users(boxId=9005, boxId=1, operator='Equal'):
            return PCPlacement02()


class PCPlacement02(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=9006, boxId=3, operator='Equal'):
            return PCPlacement03()


class PCPlacement03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MartOpen()


class MartOpen(state.State):
    def on_enter(self):
        set_actor(triggerId=4000, visible=True, initialSequence='ry_functobj_door_E01_on') # RevolvingDoor
        set_actor(triggerId=4001, visible=True, initialSequence='ry_functobj_door_E01_on') # RevolvingDoor
        set_actor(triggerId=4002, visible=True, initialSequence='ry_functobj_door_E01_on') # RevolvingDoor
        set_actor(triggerId=4003, visible=True, initialSequence='ry_functobj_door_E01_on') # RevolvingDoor
        set_event_ui(type=1, arg2='$02000387_BF__01_PLAYPARTTIMEJOB__4$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return R01Start()


class R01Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # GuideUI
        set_event_ui(type=1, arg2='$02000387_BF__01_PLAYPARTTIMEJOB__5$', arg3='3000', arg4='0')
        set_event_ui(type=0, arg2='1,3') # Round1
        set_effect(triggerIds=[5105], visible=True) # DownArrow
        set_effect(triggerIds=[5106], visible=True) # DownArrow

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R01Customer01Row03Random()


#  1Round 1번 고객  : 3번 레일 
class R01Customer01Row03Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=10103)

    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return NpcGroup3003()
        if random_condition(rate=33):
            return NpcGroup3007()
        if random_condition(rate=33):
            return NpcGroup3011()


#  1Round 2번 고객  : 2번 레일 
class R01Customer02Row02Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=10202)

    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return NpcGroup2002()
        if random_condition(rate=33):
            return NpcGroup2006()
        if random_condition(rate=33):
            return NpcGroup2010()


#  1Round 3번 고객  : 4번 레일 
class R01Customer03Row04Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=10304)

    def on_tick(self) -> state.State:
        if random_condition(rate=15):
            return None # Missing State: NpcGroup4205
        if random_condition(rate=14):
            return NpcGroup4208()
        if random_condition(rate=14):
            return NpcGroup4212()
        if random_condition(rate=14):
            return NpcGroup4216()
        if random_condition(rate=14):
            return NpcGroup4220()
        if random_condition(rate=14):
            return NpcGroup4224()
        if random_condition(rate=15):
            return NpcGroup4228()


#  1Round 4번 고객  : 1번 레일 
class R01Customer04Row01Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=10401)

    def on_tick(self) -> state.State:
        if random_condition(rate=17):
            return NpcGroup1101()
        if random_condition(rate=17):
            return NpcGroup1105()
        if random_condition(rate=17):
            return NpcGroup1109()
        if random_condition(rate=17):
            return NpcGroup1113()
        if random_condition(rate=16):
            return NpcGroup1117()
        if random_condition(rate=16):
            return NpcGroup1121()


class R01End(state.State):
    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9007, spawnIds=[0]):
            return R02StartDelay01()


class R02StartDelay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R02Start()


class R02Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # GuideUI
        set_event_ui(type=1, arg2='$02000387_BF__01_PLAYPARTTIMEJOB__6$', arg3='3000', arg4='0')
        set_event_ui(type=0, arg2='2,3') # Round2

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return R02Customer01Row02Random()


#  2Round 1번 고객  : 2번 레일 
class R02Customer01Row02Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=20102)

    def on_tick(self) -> state.State:
        if random_condition(rate=17):
            return NpcGroup2102()
        if random_condition(rate=17):
            return NpcGroup2106()
        if random_condition(rate=17):
            return NpcGroup2110()
        if random_condition(rate=17):
            return NpcGroup2114()
        if random_condition(rate=16):
            return NpcGroup2118()
        if random_condition(rate=16):
            return NpcGroup2122()


#  2Round 2번 고객  : 3번 레일 
class R02Customer02Row03Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=20203)

    def on_tick(self) -> state.State:
        if random_condition(rate=15):
            return NpcGroup3203()
        if random_condition(rate=14):
            return NpcGroup3207()
        if random_condition(rate=14):
            return NpcGroup3211()
        if random_condition(rate=14):
            return NpcGroup3215()
        if random_condition(rate=14):
            return NpcGroup3219()
        if random_condition(rate=14):
            return NpcGroup3223()
        if random_condition(rate=15):
            return NpcGroup3227()


#  2Round 3번 고객  : 1번 레일 
class R02Customer03Row01Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=20301)

    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return NpcGroup1001()
        if random_condition(rate=33):
            return NpcGroup1005()
        if random_condition(rate=33):
            return NpcGroup1009()


#  2Round 4번 고객  : 4번 레일 
class R02Customer04Row04Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=20404)

    def on_tick(self) -> state.State:
        if random_condition(rate=17):
            return NpcGroup4104()
        if random_condition(rate=17):
            return NpcGroup4108()
        if random_condition(rate=17):
            return NpcGroup4112()
        if random_condition(rate=17):
            return NpcGroup4116()
        if random_condition(rate=16):
            return NpcGroup4120()
        if random_condition(rate=16):
            return NpcGroup4124()


#  2Round 5번 고객  : 2번 레일 
class R02Customer05Row02Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=20502)

    def on_tick(self) -> state.State:
        if random_condition(rate=15):
            return NpcGroup2202()
        if random_condition(rate=14):
            return NpcGroup2206()
        if random_condition(rate=14):
            return NpcGroup2210()
        if random_condition(rate=14):
            return NpcGroup2214()
        if random_condition(rate=14):
            return NpcGroup2218()
        if random_condition(rate=14):
            return NpcGroup2222()
        if random_condition(rate=15):
            return NpcGroup2226()


#  2Round 6번 고객  : 3번 레일 
class R02Customer06Row03Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=20603)

    def on_tick(self) -> state.State:
        if random_condition(rate=17):
            return NpcGroup3103()
        if random_condition(rate=17):
            return NpcGroup3107()
        if random_condition(rate=17):
            return NpcGroup3111()
        if random_condition(rate=17):
            return NpcGroup3115()
        if random_condition(rate=16):
            return NpcGroup3119()
        if random_condition(rate=16):
            return NpcGroup3123()


#  2Round 7번 고객  : 1번 레일 
class R02Customer07Row01Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=20701)

    def on_tick(self) -> state.State:
        if random_condition(rate=15):
            return NpcGroup1201()
        if random_condition(rate=14):
            return NpcGroup1205()
        if random_condition(rate=14):
            return NpcGroup1209()
        if random_condition(rate=14):
            return NpcGroup1213()
        if random_condition(rate=14):
            return NpcGroup1217()
        if random_condition(rate=14):
            return NpcGroup1221()
        if random_condition(rate=15):
            return NpcGroup1225()


#  2Round 8번 고객  : 4번 레일 
class R02Customer08Row04Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=20804)

    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return NpcGroup4004()
        if random_condition(rate=33):
            return NpcGroup4008()
        if random_condition(rate=33):
            return NpcGroup4012()


class R02End(state.State):
    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9007, spawnIds=[0]):
            return R03StartDelay01()


class R03StartDelay01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return R03Start()


class R03Start(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # GuideUI
        set_event_ui(type=1, arg2='$02000387_BF__01_PLAYPARTTIMEJOB__7$', arg3='3000', arg4='0')
        set_event_ui(type=0, arg2='3,3') # Round3

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return R03Customer01Row04Random()


#  3Round 1번 고객  : 4번 레일 
class R03Customer01Row04Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=30104)

    def on_tick(self) -> state.State:
        if random_condition(rate=17):
            return NpcGroup4104()
        if random_condition(rate=17):
            return NpcGroup4108()
        if random_condition(rate=17):
            return NpcGroup4112()
        if random_condition(rate=17):
            return NpcGroup4116()
        if random_condition(rate=16):
            return NpcGroup4120()
        if random_condition(rate=16):
            return NpcGroup4124()


#  3Round 2번 고객  : 3번 레일 
class R03Customer02Row02Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=30202)

    def on_tick(self) -> state.State:
        if random_condition(rate=15):
            return NpcGroup2202()
        if random_condition(rate=14):
            return NpcGroup2206()
        if random_condition(rate=14):
            return NpcGroup2210()
        if random_condition(rate=14):
            return NpcGroup2214()
        if random_condition(rate=14):
            return NpcGroup2218()
        if random_condition(rate=14):
            return NpcGroup2222()
        if random_condition(rate=15):
            return NpcGroup2226()


#  3Round 3번 고객  : 2번 레일 
class R03Customer03Row03Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=30303)

    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return NpcGroup3003()
        if random_condition(rate=33):
            return NpcGroup3007()
        if random_condition(rate=33):
            return NpcGroup3011()


#  3Round 4번 고객  : 1번 레일 
class R03Customer04Row01Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=30401)

    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return NpcGroup1001()
        if random_condition(rate=33):
            return NpcGroup1005()
        if random_condition(rate=33):
            return NpcGroup1009()


#  3Round 5번 고객  : 2번 레일 
class R03Customer05Row02Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=30502)

    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return NpcGroup2002()
        if random_condition(rate=33):
            return NpcGroup2006()
        if random_condition(rate=33):
            return NpcGroup2010()


#  3Round 6번 고객  : 4번 레일 
class R03Customer06Row04Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=30604)

    def on_tick(self) -> state.State:
        if random_condition(rate=15):
            return NpcGroup4204()
        if random_condition(rate=14):
            return NpcGroup4208()
        if random_condition(rate=14):
            return NpcGroup4212()
        if random_condition(rate=14):
            return NpcGroup4216()
        if random_condition(rate=14):
            return NpcGroup4220()
        if random_condition(rate=14):
            return NpcGroup4224()
        if random_condition(rate=15):
            return NpcGroup4228()


#  3Round 7번 고객  : 3번 레일 
class R03Customer07Row03Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=30703)

    def on_tick(self) -> state.State:
        if random_condition(rate=17):
            return NpcGroup3103()
        if random_condition(rate=17):
            return NpcGroup3107()
        if random_condition(rate=17):
            return NpcGroup3111()
        if random_condition(rate=17):
            return NpcGroup3115()
        if random_condition(rate=16):
            return NpcGroup3119()
        if random_condition(rate=16):
            return NpcGroup3123()


#  3Round 8번 고객  : 1번 레일 
class R03Customer08Row01Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=30801)

    def on_tick(self) -> state.State:
        if random_condition(rate=17):
            return NpcGroup1101()
        if random_condition(rate=17):
            return NpcGroup1105()
        if random_condition(rate=17):
            return NpcGroup1109()
        if random_condition(rate=17):
            return NpcGroup1113()
        if random_condition(rate=16):
            return NpcGroup1117()
        if random_condition(rate=16):
            return NpcGroup1121()


#  3Round 9번 고객  : 1번 레일 
class R03Customer09Row01Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=30901)

    def on_tick(self) -> state.State:
        if random_condition(rate=15):
            return NpcGroup1201()
        if random_condition(rate=14):
            return NpcGroup1205()
        if random_condition(rate=14):
            return NpcGroup1209()
        if random_condition(rate=14):
            return NpcGroup1213()
        if random_condition(rate=14):
            return NpcGroup1217()
        if random_condition(rate=14):
            return NpcGroup1221()
        if random_condition(rate=15):
            return NpcGroup1225()


#  3Round 10번 고객  : 4번 레일 
class R03Customer10Row04Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=31004)

    def on_tick(self) -> state.State:
        if random_condition(rate=33):
            return NpcGroup4004()
        if random_condition(rate=33):
            return NpcGroup4008()
        if random_condition(rate=33):
            return NpcGroup4012()


#  3Round 11번 고객  : 2번 레일 
class R03Customer11Row02Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=31102)

    def on_tick(self) -> state.State:
        if random_condition(rate=17):
            return NpcGroup2102()
        if random_condition(rate=17):
            return NpcGroup2106()
        if random_condition(rate=17):
            return NpcGroup2110()
        if random_condition(rate=17):
            return NpcGroup2114()
        if random_condition(rate=16):
            return NpcGroup2118()
        if random_condition(rate=16):
            return NpcGroup2122()


#  3Round 12번 고객  : 3번 레일 
class R03Customer12Row03Random(state.State):
    def on_enter(self):
        set_user_value(key='RoundCustomerRow', value=31203)

    def on_tick(self) -> state.State:
        if random_condition(rate=15):
            return NpcGroup3203()
        if random_condition(rate=14):
            return NpcGroup3207()
        if random_condition(rate=14):
            return NpcGroup3211()
        if random_condition(rate=14):
            return NpcGroup3215()
        if random_condition(rate=14):
            return NpcGroup3219()
        if random_condition(rate=14):
            return NpcGroup3223()
        if random_condition(rate=15):
            return NpcGroup3227()


class R03End(state.State):
    def on_tick(self) -> state.State:
        if not npc_detected(boxId=9007, spawnIds=[0]):
            return GameEndNotice01()


class GameEndNotice01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=2000387, portalId=1, boxId=9900) # 사무실로 강제 이동
        set_conversation(type=2, spawnId=11000491, script='$02000387_BF__01_PLAYPARTTIMEJOB__8$', arg4=4)
        set_skip(state=GameEndNotice01Skip)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return GameEndNotice01Skip()


class GameEndNotice01Skip(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_user_value(triggerId=10, key='DungeonClear', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return GameWrapUp()


class GameWrapUp(state.State):
    def on_enter(self):
        dungeon_clear()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        unset_mini_game_area_for_hack() # 해킹 보안 종료

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return PCLeave01()


class PCLeave01(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000387_BF__01_PLAYPARTTIMEJOB__10$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return PCLeave02()


class PCLeave02(state.State):
    def on_enter(self):
        move_user(mapId=0, portalId=0)


#  NPC 그룹 랜덤 
class NpcGroup1001(state.State):
    def on_enter(self):
        set_user_value(triggerId=1001, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1005(state.State):
    def on_enter(self):
        set_user_value(triggerId=1005, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1009(state.State):
    def on_enter(self):
        set_user_value(triggerId=1009, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2002(state.State):
    def on_enter(self):
        set_user_value(triggerId=2002, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2006(state.State):
    def on_enter(self):
        set_user_value(triggerId=2006, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2010(state.State):
    def on_enter(self):
        set_user_value(triggerId=2010, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3003(state.State):
    def on_enter(self):
        set_user_value(triggerId=3003, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3007(state.State):
    def on_enter(self):
        set_user_value(triggerId=3007, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3011(state.State):
    def on_enter(self):
        set_user_value(triggerId=3011, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4004(state.State):
    def on_enter(self):
        set_user_value(triggerId=4004, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4008(state.State):
    def on_enter(self):
        set_user_value(triggerId=4008, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4012(state.State):
    def on_enter(self):
        set_user_value(triggerId=4012, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1101(state.State):
    def on_enter(self):
        set_user_value(triggerId=1101, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1105(state.State):
    def on_enter(self):
        set_user_value(triggerId=1105, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1109(state.State):
    def on_enter(self):
        set_user_value(triggerId=1109, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1113(state.State):
    def on_enter(self):
        set_user_value(triggerId=1113, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1117(state.State):
    def on_enter(self):
        set_user_value(triggerId=1117, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1121(state.State):
    def on_enter(self):
        set_user_value(triggerId=1121, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2102(state.State):
    def on_enter(self):
        set_user_value(triggerId=2102, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2106(state.State):
    def on_enter(self):
        set_user_value(triggerId=2106, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2110(state.State):
    def on_enter(self):
        set_user_value(triggerId=2110, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2114(state.State):
    def on_enter(self):
        set_user_value(triggerId=2114, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2118(state.State):
    def on_enter(self):
        set_user_value(triggerId=2118, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2122(state.State):
    def on_enter(self):
        set_user_value(triggerId=2122, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3103(state.State):
    def on_enter(self):
        set_user_value(triggerId=3103, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3107(state.State):
    def on_enter(self):
        set_user_value(triggerId=3107, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3111(state.State):
    def on_enter(self):
        set_user_value(triggerId=3111, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3115(state.State):
    def on_enter(self):
        set_user_value(triggerId=3115, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3119(state.State):
    def on_enter(self):
        set_user_value(triggerId=3119, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3123(state.State):
    def on_enter(self):
        set_user_value(triggerId=3123, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4104(state.State):
    def on_enter(self):
        set_user_value(triggerId=4104, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4108(state.State):
    def on_enter(self):
        set_user_value(triggerId=4108, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4112(state.State):
    def on_enter(self):
        set_user_value(triggerId=4112, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4116(state.State):
    def on_enter(self):
        set_user_value(triggerId=4116, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4120(state.State):
    def on_enter(self):
        set_user_value(triggerId=4120, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4124(state.State):
    def on_enter(self):
        set_user_value(triggerId=4124, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1201(state.State):
    def on_enter(self):
        set_user_value(triggerId=1201, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1205(state.State):
    def on_enter(self):
        set_user_value(triggerId=1205, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1209(state.State):
    def on_enter(self):
        set_user_value(triggerId=1209, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1213(state.State):
    def on_enter(self):
        set_user_value(triggerId=1213, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1217(state.State):
    def on_enter(self):
        set_user_value(triggerId=1217, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1221(state.State):
    def on_enter(self):
        set_user_value(triggerId=1221, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup1225(state.State):
    def on_enter(self):
        set_user_value(triggerId=1225, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2202(state.State):
    def on_enter(self):
        set_user_value(triggerId=2202, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2206(state.State):
    def on_enter(self):
        set_user_value(triggerId=2206, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2210(state.State):
    def on_enter(self):
        set_user_value(triggerId=2210, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2214(state.State):
    def on_enter(self):
        set_user_value(triggerId=2214, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2218(state.State):
    def on_enter(self):
        set_user_value(triggerId=2218, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2222(state.State):
    def on_enter(self):
        set_user_value(triggerId=2222, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup2226(state.State):
    def on_enter(self):
        set_user_value(triggerId=2226, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3203(state.State):
    def on_enter(self):
        set_user_value(triggerId=3203, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3207(state.State):
    def on_enter(self):
        set_user_value(triggerId=3207, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3211(state.State):
    def on_enter(self):
        set_user_value(triggerId=3211, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3215(state.State):
    def on_enter(self):
        set_user_value(triggerId=3215, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3219(state.State):
    def on_enter(self):
        set_user_value(triggerId=3219, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3223(state.State):
    def on_enter(self):
        set_user_value(triggerId=3223, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup3227(state.State):
    def on_enter(self):
        set_user_value(triggerId=3227, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4204(state.State):
    def on_enter(self):
        set_user_value(triggerId=4204, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4208(state.State):
    def on_enter(self):
        set_user_value(triggerId=4208, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4212(state.State):
    def on_enter(self):
        set_user_value(triggerId=4212, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4216(state.State):
    def on_enter(self):
        set_user_value(triggerId=4216, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4220(state.State):
    def on_enter(self):
        set_user_value(triggerId=4220, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4224(state.State):
    def on_enter(self):
        set_user_value(triggerId=4224, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NpcGroup4228(state.State):
    def on_enter(self):
        set_user_value(triggerId=4228, key='CustomerEnter', value=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return NextTurnCheck()


class NextTurnCheck(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='RoundCustomerRow', value=10103):
            return R01Customer02Row02Random()
        if user_value(key='RoundCustomerRow', value=10202):
            return R01Customer03Row04Random()
        if user_value(key='RoundCustomerRow', value=10304):
            return R01Customer04Row01Random()
        if user_value(key='RoundCustomerRow', value=10401): # 2Round
            return R01End()
        if user_value(key='RoundCustomerRow', value=20102):
            return R02Customer02Row03Random()
        if user_value(key='RoundCustomerRow', value=20203):
            return R02Customer03Row01Random()
        if user_value(key='RoundCustomerRow', value=20301):
            return R02Customer04Row04Random()
        if user_value(key='RoundCustomerRow', value=20404):
            return R02Customer05Row02Random()
        if user_value(key='RoundCustomerRow', value=20502):
            return R02Customer06Row03Random()
        if user_value(key='RoundCustomerRow', value=20603):
            return R02Customer07Row01Random()
        if user_value(key='RoundCustomerRow', value=20701):
            return R02Customer08Row04Random()
        if user_value(key='RoundCustomerRow', value=20804): # 3Round
            return R02End()
        if user_value(key='RoundCustomerRow', value=30104):
            return R03Customer02Row02Random()
        if user_value(key='RoundCustomerRow', value=30202):
            return R03Customer03Row03Random()
        if user_value(key='RoundCustomerRow', value=30303):
            return R03Customer04Row01Random()
        if user_value(key='RoundCustomerRow', value=30401):
            return R03Customer05Row02Random()
        if user_value(key='RoundCustomerRow', value=30502):
            return R03Customer06Row04Random()
        if user_value(key='RoundCustomerRow', value=30604):
            return R03Customer07Row03Random()
        if user_value(key='RoundCustomerRow', value=30703):
            return R03Customer08Row01Random()
        if user_value(key='RoundCustomerRow', value=30801):
            return R03Customer09Row01Random()
        if user_value(key='RoundCustomerRow', value=30901):
            return R03Customer10Row04Random()
        if user_value(key='RoundCustomerRow', value=31004):
            return R03Customer11Row02Random()
        if user_value(key='RoundCustomerRow', value=31102):
            return R03Customer12Row03Random()
        if user_value(key='RoundCustomerRow', value=31203):
            return R03End()


