""" trigger/02000325_bf/main.xml """
import common

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(common.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10000739], state=2)
        self.set_interact_object(triggerIds=[10000740], state=2)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[611], visible=False)
        self.set_effect(triggerIds=[612], visible=False)
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022], visible=False, arg3=0, delay=0, scale=0)
        self.set_interact_object(triggerIds=[10000752], state=0)
        self.set_interact_object(triggerIds=[13000009], state=2)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return CheckUserCount(self.ctx)


class DungeonStart(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022], visible=True, arg3=0, delay=200, scale=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__0$', arg3='4000', arg4='0')
            return 어나운스02(self.ctx)


class 어나운스02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__1$', arg3='3500', arg4='0')
            return 어나운스03(self.ctx)


class 어나운스03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__2$', arg3='3500', arg4='0')
            return 라운드반응체크1(self.ctx)


class 라운드반응체크1(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000752], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000752], stateValue=0):
            self.set_effect(triggerIds=[601], visible=True)
            return 라운드카운트딜레이1(self.ctx)


class 라운드카운트딜레이1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 라운드카운트1(self.ctx)


class 라운드카운트1(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=True)
        self.set_effect(triggerIds=[611], visible=True)
        self.set_effect(triggerIds=[612], visible=True)
        self.set_interact_object(triggerIds=[10000739], state=1)
        self.set_interact_object(triggerIds=[10000740], state=1)
        self.set_event_ui(type=0, arg2='1,3')
        self.show_count_ui(text='$02000325_BF__MAIN__3$', stage=1, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 라운드1(self.ctx)


class 라운드1(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=5):
            return 소환3001(self.ctx)
        if self.random_condition(rate=5):
            return 소환3002(self.ctx)
        if self.random_condition(rate=5):
            return 소환3003(self.ctx)
        if self.random_condition(rate=5):
            return 소환3004(self.ctx)
        if self.random_condition(rate=5):
            return 소환3005(self.ctx)
        if self.random_condition(rate=5):
            return 소환3006(self.ctx)
        if self.random_condition(rate=5):
            return 소환3007(self.ctx)
        if self.random_condition(rate=5):
            return 소환3008(self.ctx)
        if self.random_condition(rate=5):
            return 소환3009(self.ctx)
        if self.random_condition(rate=5):
            return 소환3010(self.ctx)
        if self.random_condition(rate=5):
            return 소환3011(self.ctx)
        if self.random_condition(rate=5):
            return 소환3012(self.ctx)
        if self.random_condition(rate=5):
            return 소환3013(self.ctx)
        if self.random_condition(rate=5):
            return 소환3014(self.ctx)
        if self.random_condition(rate=5):
            return 소환3015(self.ctx)
        if self.random_condition(rate=5):
            return 소환3016(self.ctx)
        if self.random_condition(rate=5):
            return 소환3017(self.ctx)
        if self.random_condition(rate=5):
            return 소환3018(self.ctx)
        if self.random_condition(rate=5):
            return 소환3019(self.ctx)
        if self.random_condition(rate=5):
            return 소환3020(self.ctx)


class 소환3001(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001], animationEffect=False)
        self.create_monster(spawnIds=[3001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3001]):
            return 라운드대기2(self.ctx)


class 소환3002(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2002], animationEffect=False)
        self.create_monster(spawnIds=[3002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3002]):
            return 라운드대기2(self.ctx)


class 소환3003(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2003], animationEffect=False)
        self.create_monster(spawnIds=[3003], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3003]):
            return 라운드대기2(self.ctx)


class 소환3004(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2004], animationEffect=False)
        self.create_monster(spawnIds=[3004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3004]):
            return 라운드대기2(self.ctx)


class 소환3005(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2005], animationEffect=False)
        self.create_monster(spawnIds=[3005], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3005]):
            return 라운드대기2(self.ctx)


class 소환3006(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2006], animationEffect=False)
        self.create_monster(spawnIds=[3006], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3006]):
            return 라운드대기2(self.ctx)


class 소환3007(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2007], animationEffect=False)
        self.create_monster(spawnIds=[3007], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3007]):
            return 라운드대기2(self.ctx)


class 소환3008(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2008], animationEffect=False)
        self.create_monster(spawnIds=[3008], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3008]):
            return 라운드대기2(self.ctx)


class 소환3009(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2009], animationEffect=False)
        self.create_monster(spawnIds=[3009], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3009]):
            return 라운드대기2(self.ctx)


class 소환3010(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2010], animationEffect=False)
        self.create_monster(spawnIds=[3010], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3010]):
            return 라운드대기2(self.ctx)


class 소환3011(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2011], animationEffect=False)
        self.create_monster(spawnIds=[3011], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3011]):
            return 라운드대기2(self.ctx)


class 소환3012(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2012], animationEffect=False)
        self.create_monster(spawnIds=[3012], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3012]):
            return 라운드대기2(self.ctx)


class 소환3013(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2013], animationEffect=False)
        self.create_monster(spawnIds=[3013], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3013]):
            return 라운드대기2(self.ctx)


class 소환3014(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2014], animationEffect=False)
        self.create_monster(spawnIds=[3014], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3014]):
            return 라운드대기2(self.ctx)


class 소환3015(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2015], animationEffect=False)
        self.create_monster(spawnIds=[3015], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3015]):
            return 라운드대기2(self.ctx)


class 소환3016(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2016], animationEffect=False)
        self.create_monster(spawnIds=[3016], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3016]):
            return 라운드대기2(self.ctx)


class 소환3017(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2017], animationEffect=False)
        self.create_monster(spawnIds=[3017], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3017]):
            return 라운드대기2(self.ctx)


class 소환3018(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2018], animationEffect=False)
        self.create_monster(spawnIds=[3018], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3018]):
            return 라운드대기2(self.ctx)


class 소환3019(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2019], animationEffect=False)
        self.create_monster(spawnIds=[3019], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3019]):
            return 라운드대기2(self.ctx)


class 소환3020(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2020], animationEffect=False)
        self.create_monster(spawnIds=[3020], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3020]):
            return 라운드대기2(self.ctx)


class 라운드대기2(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000739], state=2)
        self.set_interact_object(triggerIds=[10000740], state=2)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[611], visible=False)
        self.set_effect(triggerIds=[612], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 어나운스04(self.ctx)


class 어나운스04(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__4$', arg3='3500', arg4='0')
            return 라운드반응체크2(self.ctx)


class 라운드반응체크2(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000752], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000752], stateValue=0):
            self.set_effect(triggerIds=[601], visible=True)
            return 어나운스04_2(self.ctx)


class 어나운스04_2(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__5$', arg3='3500', arg4='0')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 라운드카운트2(self.ctx)


class 라운드카운트2(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=True)
        self.set_effect(triggerIds=[612], visible=True)
        self.set_interact_object(triggerIds=[10000740], state=1)
        self.set_event_ui(type=0, arg2='2,3')
        self.show_count_ui(text='$02000325_BF__MAIN__6$', stage=2, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 라운드2(self.ctx)


class 라운드2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=5):
            return 소환체크3001(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3002(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3003(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3004(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3005(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3006(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3007(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3008(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3009(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3010(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3011(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3012(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3013(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3014(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3015(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3016(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3017(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3018(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3019(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크3020(self.ctx)


class 소환체크3001(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2001]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2001]):
            return 소환2_3001(self.ctx)


class 소환체크3002(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2002]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2002]):
            return 소환2_3002(self.ctx)


class 소환체크3003(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2003]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2003]):
            return 소환2_3003(self.ctx)


class 소환체크3004(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2004]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2004]):
            return 소환2_3004(self.ctx)


class 소환체크3005(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2005]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2005]):
            return 소환2_3005(self.ctx)


class 소환체크3006(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2006]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2006]):
            return 소환2_3006(self.ctx)


class 소환체크3007(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2007]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2007]):
            return 소환2_3007(self.ctx)


class 소환체크3008(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2008]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2008]):
            return 소환2_3008(self.ctx)


class 소환체크3009(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2009]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2009]):
            return 소환2_3009(self.ctx)


class 소환체크3010(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2010]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2010]):
            return 소환2_3010(self.ctx)


class 소환체크3011(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2011]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2011]):
            return 소환2_3011(self.ctx)


class 소환체크3012(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2012]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2012]):
            return 소환2_3012(self.ctx)


class 소환체크3013(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2013]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2013]):
            return 소환2_3013(self.ctx)


class 소환체크3014(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2014]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2014]):
            return 소환2_3014(self.ctx)


class 소환체크3015(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2015]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2015]):
            return 소환2_3015(self.ctx)


class 소환체크3016(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2016]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2016]):
            return 소환2_3016(self.ctx)


class 소환체크3017(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2017]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2017]):
            return 소환2_3017(self.ctx)


class 소환체크3018(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2018]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2018]):
            return 소환2_3018(self.ctx)


class 소환체크3019(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2019]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2019]):
            return 소환2_3019(self.ctx)


class 소환체크3020(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2020]):
            return 라운드2(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2020]):
            return 소환2_3020(self.ctx)


class 소환2_3001(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001], animationEffect=False)
        self.create_monster(spawnIds=[3001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3001]):
            return 라운드대기3(self.ctx)


class 소환2_3002(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2002], animationEffect=False)
        self.create_monster(spawnIds=[3002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3002]):
            return 라운드대기3(self.ctx)


class 소환2_3003(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2003], animationEffect=False)
        self.create_monster(spawnIds=[3003], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3003]):
            return 라운드대기3(self.ctx)


class 소환2_3004(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2004], animationEffect=False)
        self.create_monster(spawnIds=[3004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3004]):
            return 라운드대기3(self.ctx)


class 소환2_3005(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2005], animationEffect=False)
        self.create_monster(spawnIds=[3005], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3005]):
            return 라운드대기3(self.ctx)


class 소환2_3006(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2006], animationEffect=False)
        self.create_monster(spawnIds=[3006], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3006]):
            return 라운드대기3(self.ctx)


class 소환2_3007(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2007], animationEffect=False)
        self.create_monster(spawnIds=[3007], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3007]):
            return 라운드대기3(self.ctx)


class 소환2_3008(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2008], animationEffect=False)
        self.create_monster(spawnIds=[3008], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3008]):
            return 라운드대기3(self.ctx)


class 소환2_3009(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2009], animationEffect=False)
        self.create_monster(spawnIds=[3009], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3009]):
            return 라운드대기3(self.ctx)


class 소환2_3010(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2010], animationEffect=False)
        self.create_monster(spawnIds=[3010], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3010]):
            return 라운드대기3(self.ctx)


class 소환2_3011(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2011], animationEffect=False)
        self.create_monster(spawnIds=[3011], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3011]):
            return 라운드대기3(self.ctx)


class 소환2_3012(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2012], animationEffect=False)
        self.create_monster(spawnIds=[3012], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3012]):
            return 라운드대기3(self.ctx)


class 소환2_3013(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2013], animationEffect=False)
        self.create_monster(spawnIds=[3013], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3013]):
            return 라운드대기3(self.ctx)


class 소환2_3014(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2014], animationEffect=False)
        self.create_monster(spawnIds=[3014], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3014]):
            return 라운드대기3(self.ctx)


class 소환2_3015(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2015], animationEffect=False)
        self.create_monster(spawnIds=[3015], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3015]):
            return 라운드대기3(self.ctx)


class 소환2_3016(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2016], animationEffect=False)
        self.create_monster(spawnIds=[3016], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3016]):
            return 라운드대기3(self.ctx)


class 소환2_3017(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2017], animationEffect=False)
        self.create_monster(spawnIds=[3017], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3017]):
            return 라운드대기3(self.ctx)


class 소환2_3018(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2018], animationEffect=False)
        self.create_monster(spawnIds=[3018], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3018]):
            return 라운드대기3(self.ctx)


class 소환2_3019(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2019], animationEffect=False)
        self.create_monster(spawnIds=[3019], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3019]):
            return 라운드대기3(self.ctx)


class 소환2_3020(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2020], animationEffect=False)
        self.create_monster(spawnIds=[3020], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3020]):
            return 라운드대기3(self.ctx)


class 라운드대기3(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[612], visible=False)
        self.set_interact_object(triggerIds=[10000740], state=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 어나운스05(self.ctx)


class 어나운스05(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            self.set_event_ui(type=1, arg2='$02000325_BF__MAIN__7$', arg3='3500', arg4='0')
            return 라운드반응체크3(self.ctx)


class 라운드반응체크3(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000752], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000752], stateValue=0):
            self.set_effect(triggerIds=[601], visible=True)
            return 라운드카운트3(self.ctx)


class 라운드카운트3(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=True)
        self.set_effect(triggerIds=[612], visible=False)
        # action name="메쉬를설정한다" arg1="3000-3022" arg2="0" arg3="0" arg4="200" arg5="2" /
        self.set_event_ui(type=0, arg2='3,3')
        self.show_count_ui(text='$02000325_BF__MAIN__9$', stage=3, count=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 라운드3(self.ctx)


class 라운드3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.random_condition(rate=5):
            return 소환체크2_3001(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3002(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3003(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3004(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3005(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3006(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3007(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3008(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3009(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3010(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3011(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3012(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3013(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3014(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3015(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3016(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3017(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3018(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3019(self.ctx)
        if self.random_condition(rate=5):
            return 소환체크2_3020(self.ctx)


class 소환체크2_3001(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2001]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2001]):
            return 소환3_3001(self.ctx)


class 소환체크2_3002(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2002]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2002]):
            return 소환3_3002(self.ctx)


class 소환체크2_3003(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2003]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2003]):
            return 소환3_3003(self.ctx)


class 소환체크2_3004(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2004]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2004]):
            return 소환3_3004(self.ctx)


class 소환체크2_3005(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2005]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2005]):
            return 소환3_3005(self.ctx)


class 소환체크2_3006(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2006]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2006]):
            return 소환3_3006(self.ctx)


class 소환체크2_3007(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2007]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2007]):
            return 소환3_3007(self.ctx)


class 소환체크2_3008(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2008]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2008]):
            return 소환3_3008(self.ctx)


class 소환체크2_3009(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2009]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2009]):
            return 소환3_3009(self.ctx)


class 소환체크2_3010(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2010]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2010]):
            return 소환3_3010(self.ctx)


class 소환체크2_3011(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2011]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2011]):
            return 소환3_3011(self.ctx)


class 소환체크2_3012(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2012]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2012]):
            return 소환3_3012(self.ctx)


class 소환체크2_3013(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2013]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2013]):
            return 소환3_3013(self.ctx)


class 소환체크2_3014(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2014]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2014]):
            return 소환3_3014(self.ctx)


class 소환체크2_3015(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2015]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2015]):
            return 소환3_3015(self.ctx)


class 소환체크2_3016(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2016]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2016]):
            return 소환3_3016(self.ctx)


class 소환체크2_3017(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2017]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2017]):
            return 소환3_3017(self.ctx)


class 소환체크2_3018(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2018]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2018]):
            return 소환3_3018(self.ctx)


class 소환체크2_3019(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2019]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2019]):
            return 소환3_3019(self.ctx)


class 소환체크2_3020(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=199, spawnIds=[2020]):
            return 라운드3(self.ctx)
        if not self.npc_detected(boxId=199, spawnIds=[2020]):
            return 소환3_3020(self.ctx)


class 소환3_3001(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2001], animationEffect=False)
        self.create_monster(spawnIds=[3001], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3001]):
            return 미션성공(self.ctx)


class 소환3_3002(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2002], animationEffect=False)
        self.create_monster(spawnIds=[3002], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3002]):
            return 미션성공(self.ctx)


class 소환3_3003(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2003], animationEffect=False)
        self.create_monster(spawnIds=[3003], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3003]):
            return 미션성공(self.ctx)


class 소환3_3004(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2004], animationEffect=False)
        self.create_monster(spawnIds=[3004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3004]):
            return 미션성공(self.ctx)


class 소환3_3005(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2005], animationEffect=False)
        self.create_monster(spawnIds=[3005], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3005]):
            return 미션성공(self.ctx)


class 소환3_3006(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2006], animationEffect=False)
        self.create_monster(spawnIds=[3006], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3006]):
            return 미션성공(self.ctx)


class 소환3_3007(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2007], animationEffect=False)
        self.create_monster(spawnIds=[3007], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3007]):
            return 미션성공(self.ctx)


class 소환3_3008(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2008], animationEffect=False)
        self.create_monster(spawnIds=[3008], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3008]):
            return 미션성공(self.ctx)


class 소환3_3009(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2009], animationEffect=False)
        self.create_monster(spawnIds=[3009], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3009]):
            return 미션성공(self.ctx)


class 소환3_3010(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2010], animationEffect=False)
        self.create_monster(spawnIds=[3010], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3010]):
            return 미션성공(self.ctx)


class 소환3_3011(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2011], animationEffect=False)
        self.create_monster(spawnIds=[3011], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3011]):
            return 미션성공(self.ctx)


class 소환3_3012(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2012], animationEffect=False)
        self.create_monster(spawnIds=[3012], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3012]):
            return 미션성공(self.ctx)


class 소환3_3013(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2013], animationEffect=False)
        self.create_monster(spawnIds=[3013], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3013]):
            return 미션성공(self.ctx)


class 소환3_3014(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2014], animationEffect=False)
        self.create_monster(spawnIds=[3014], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3014]):
            return 미션성공(self.ctx)


class 소환3_3015(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2015], animationEffect=False)
        self.create_monster(spawnIds=[3015], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3015]):
            return 미션성공(self.ctx)


class 소환3_3016(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2016], animationEffect=False)
        self.create_monster(spawnIds=[3016], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3016]):
            return 미션성공(self.ctx)


class 소환3_3017(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2017], animationEffect=False)
        self.create_monster(spawnIds=[3017], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3017]):
            return 미션성공(self.ctx)


class 소환3_3018(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2018], animationEffect=False)
        self.create_monster(spawnIds=[3018], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3018]):
            return 미션성공(self.ctx)


class 소환3_3019(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2019], animationEffect=False)
        self.create_monster(spawnIds=[3019], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3019]):
            return 미션성공(self.ctx)


class 소환3_3020(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2020], animationEffect=False)
        self.create_monster(spawnIds=[3020], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[3020]):
            return 미션성공(self.ctx)


class 미션성공(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=102, type='trigger', achieve='BraveRace')
        self.set_mesh(triggerIds=[3000,3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022], visible=True, arg3=0, delay=200, scale=2)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[612], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return 라운드보상3(self.ctx)


class 라운드보상3(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 포털생성(self.ctx)


class 포털생성(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
            self.set_event_ui(type=0, arg2='0,0')
            self.dungeon_clear()
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
