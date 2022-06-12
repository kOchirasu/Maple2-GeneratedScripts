using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000186: Jack
/// </summary>
public class _11000186 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 50;60
    }

    // Select 0:
    // $script:0831180407000810$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407000813$
                // - I live with my grandma. She said that when I was young, my parents were taken away by demons. Also, my sister was frozen solid alongside the rest of the villagers. You could say my family's had a rough go of it.
                return 50;
            case (50, 1):
                // $script:0831180407000814$
                // - She also said the empire's forces are no better than those demons. They brought ice elementals to fight the demons, but tons of innocent people were frozen during the fight.
                return -1;
            case (60, 0):
                // $script:0831180407000815$
                // - See those red maple trees there? When Grandma planted them, they were seeds as big as your thumbnail. She says they grew twice as fast as I did.
                return 60;
            case (60, 1):
                // $script:0831180407000816$
                // - I've heard only the warmth of $itemPlural:30000028$ can thaw the people frozen below.
                return 60;
            case (60, 2):
                // $script:0831180407000817$
                // - That's because red maple trees are born from the energy of the fire elementals that fell in that terrible battle. I don't know if that's true.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Next,
            (60, 1) => NpcTalkButton.Next,
            (60, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
