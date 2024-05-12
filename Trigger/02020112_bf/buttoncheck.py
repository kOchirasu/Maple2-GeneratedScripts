""" trigger/02020112_bf/buttoncheck.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=9901, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9902, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9903, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9904, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621], visible=False, arg3=0, delay=20, scale=3)
        self.set_mesh(triggerIds=[1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640], visible=False, arg3=0, delay=20, scale=3)
        self.set_mesh(triggerIds=[1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660], visible=False, arg3=0, delay=20, scale=3)
        self.set_user_value(triggerId=99990016, key='respawn', value=0)
        self.set_user_value(triggerId=99990003, key='Timer', value=0)
        self.set_user_value(triggerId=99990021, key='Reconnect', value=0)
        self.add_buff(boxIds=[916], skillId=70002104, level=1, isSkillSet=False)
        self.set_effect(triggerIds=[8001], visible=True)
        self.set_effect(triggerIds=[8002,8003,8004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GravityRoom', value=1):
            return 작동(self.ctx)


class 작동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_buff(boxIds=[916], skillId=70002104, level=1, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[911], jobCode=0):
            return 감지_1층(self.ctx)


class 감지_1층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8001], visible=False)
        self.set_effect(triggerIds=[8002], visible=True)
        self.set_effect(triggerIds=[8003], visible=True)
        self.set_effect(triggerIds=[8004], visible=True)
        self.set_user_value(triggerId=99990003, key='Timer', value=1)
        self.set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621], visible=True, arg3=0, delay=20, scale=3)
        self.set_mesh(triggerIds=[1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640], visible=True, arg3=0, delay=20, scale=3)
        self.set_mesh(triggerIds=[1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660], visible=True, arg3=0, delay=20, scale=3)
        self.set_actor(triggerId=9901, visible=True, initialSequence='Interaction_Lapentafoothold_A01_On')
        self.set_actor(triggerId=9902, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9903, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9904, visible=True, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.add_buff(boxIds=[916], skillId=70002103, level=1, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerReset', value=1):
            return 대기(self.ctx)
        if self.user_detected(boxIds=[912], jobCode=0):
            return 감지_2층(self.ctx)


class 감지_2층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8002], visible=False)
        self.set_user_value(triggerId=99990016, key='respawn', value=1)
        self.add_buff(boxIds=[916], skillId=70002103, level=1, isSkillSet=False)
        self.set_actor(triggerId=9902, visible=True, initialSequence='Interaction_Lapentafoothold_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerReset', value=1):
            return 대기(self.ctx)
        if self.user_detected(boxIds=[913], jobCode=0):
            return 감지_3층(self.ctx)


class 감지_3층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8003], visible=False)
        self.add_buff(boxIds=[916], skillId=70002103, level=1, isSkillSet=False)
        self.set_actor(triggerId=9903, visible=True, initialSequence='Interaction_Lapentafoothold_A01_On')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerReset', value=1):
            return 대기(self.ctx)
        if self.user_detected(boxIds=[914], jobCode=0):
            return 감지_4층(self.ctx)


class 감지_4층(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[8004], visible=False)
        self.set_actor(triggerId=9904, visible=True, initialSequence='Interaction_Lapentafoothold_A01_On')
        self.add_buff(boxIds=[916], skillId=70002105, level=1, isSkillSet=False)
        self.set_gravity(gravity=-32)
        self.set_event_ui(type=1, arg2='$02020112_BF__BUTTONCHECK__0$', arg3='5000')
        self.set_user_value(triggerId=99990016, key='respawn', value=2)
        # <1층 스폰 중지>
        self.set_user_value(triggerId=99990003, key='Timer', value=2)
        self.set_user_value(triggerId=99990001, key='GravityRoom', value=2)
        self.set_user_value(triggerId=99990021, key='Reconnect', value=1)
        # <재접속 유저를 위해 버프 지속적으로 쏴주기>
        self.set_actor(triggerId=9901, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9902, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9903, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(triggerId=9904, visible=False, initialSequence='Interaction_Lapentafoothold_A01_Off')
        self.set_mesh(triggerIds=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610,1611,1612,1613,1614,1615,1616,1617,1618,1619,1620,1621], visible=False, arg3=0, delay=20, scale=3)
        self.set_mesh(triggerIds=[1621,1622,1623,1624,1625,1626,1627,1628,1629,1630,1631,1632,1633,1634,1635,1636,1637,1638,1639,1640], visible=False, arg3=0, delay=20, scale=3)
        self.set_mesh(triggerIds=[1641,1642,1643,1644,1645,1646,1647,1648,1649,1650,1651,1652,1653,1654,1655,1656,1657,1658,1659,1660], visible=False, arg3=0, delay=20, scale=3)


initial_state = 대기
