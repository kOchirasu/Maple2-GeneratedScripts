""" trigger/02020112_bf/jumproom.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.set_effect(triggerIds=[8005], visible=False)
        self.set_effect(triggerIds=[8006], visible=False)
        self.set_effect(triggerIds=[8007], visible=False)
        self.set_effect(triggerIds=[8008], visible=False)
        self.set_user_value(triggerId=99990009, key='ButtonSuccess', value=0)
        self.set_user_value(triggerId=99990010, key='ButtonSuccess', value=0)
        self.set_user_value(triggerId=99990011, key='ButtonSuccess', value=0)
        self.set_user_value(triggerId=99990012, key='ButtonSuccess', value=0)
        self.set_user_value(triggerId=99990001, key='MonsterDead', value=0)
        self.set_actor(triggerId=9905, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9906, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9907, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9908, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=931, boxId=4, operator='GreaterEqual'):
            return 감지(self.ctx)
        if self.user_detected(boxIds=[931], jobCode=0):
            return 감지(self.ctx)


class 감지(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8005], visible=True)
        self.set_effect(triggerIds=[8006], visible=True)
        self.set_effect(triggerIds=[8007], visible=True)
        self.set_effect(triggerIds=[8008], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return 성공(self.ctx)


class 성공(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990021, key='Reconnect', value=2) # <재접속 유저를 위해 버프 지속적으로 쏴주기 캔슬>
        self.set_event_ui(type=1, arg2='$02020112_BF__JUMPROOM__0$', arg3='5000')
        self.set_gravity(gravity=0)
        self.set_effect(triggerIds=[8005], visible=False)
        self.set_effect(triggerIds=[8006], visible=False)
        self.set_effect(triggerIds=[8007], visible=False)
        self.set_effect(triggerIds=[8008], visible=False)
        self.add_buff(boxIds=[931], skillId=70002112, level=1, isSkillSet=False)
        self.set_user_value(triggerId=99990009, key='ButtonSuccess', value=1)
        self.set_user_value(triggerId=99990010, key='ButtonSuccess', value=1)
        self.set_user_value(triggerId=99990011, key='ButtonSuccess', value=1)
        self.set_user_value(triggerId=99990012, key='ButtonSuccess', value=1)
        self.set_mesh(triggerIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509], visible=False, arg3=0, delay=20, scale=3)
        self.set_mesh(triggerIds=[1510,1511,1512,1513,1514,1515,1516,1517,1518], visible=False, arg3=0, delay=20, scale=3)
        self.set_mesh(triggerIds=[1519,1520,1521,1522,1523,1524,1525,1526,1527], visible=False, arg3=0, delay=20, scale=3)
        self.set_mesh(triggerIds=[1528,1529,1530,1531,1532,1533,1534,1535,1536], visible=False, arg3=0, delay=20, scale=3)
        self.set_actor(triggerId=9905, visible=False, initialSequence='Interaction_Lapentafoothold_A01_On')
        self.set_actor(triggerId=9906, visible=False, initialSequence='Interaction_Lapentafoothold_A01_On')
        self.set_actor(triggerId=9907, visible=False, initialSequence='Interaction_Lapentafoothold_A01_On')
        self.set_actor(triggerId=9908, visible=False, initialSequence='Interaction_Lapentafoothold_A01_On')
        self.create_monster(spawnIds=[152,153,154,155], animationEffect=False)
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=1, isEnable=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[152,153,154,155]):
            self.set_user_value(triggerId=99990001, key='MonsterDead', value=1)
            return None


initial_state = 대기
