using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003257: Cheshire Carmen Bella Jr. II
/// </summary>
public class _11003257 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50;60
    }

    // Select 0:
    // $script:0403155707008184$
    // - Meow!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008185$
                // - What're you staring at? Never see a talking cat before?
                switch (selection) {
                    // $script:0403155707008186$
                    // - Guh...
                    case 0:
                        return 31;
                    // $script:0403155707008187$
                    // - Are you a magic kitty?
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0403155707008188$
                // - Meheh! You're an old-fashioned one, talking animals are all the rage these days! I forgive your ignorance, though... so long as you bring me snacks next time.
                return -1;
            case (32, 0):
                // $script:0403155707008189$
                // - Yep! A magical kitty for a magical place. This is $map:02000023$ after all, land of wonder and imagination. Welcome!
                return -1;
            case (40, 0):
                // $script:0403155707008190$
                // - What's with the sour face?
                switch (selection) {
                    // $script:0530154407008542$
                    // - Send me to $npcName:11003254[gender:1]$.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0530154407008543$
                // - Has my magic failed? Impossible!
                switch (selection) {
                    // $script:0530154407008544$
                    // - Hurry it up!
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // functionID=1 
                // $script:0530154407008545$
                // - I'm trying! Close your eyes. It'll work for sure this time!
                return -1;
            case (50, 0):
                // $script:0530154407008546$
                // - There's something... dark blocking my magic. There's no way to get to Ellinel right now. 
                return -1;
            case (60, 0):
                // $script:0530154407008547$
                // - What's with the sour face?
                switch (selection) {
                    // $script:0808093807008794$
                    // - I'm lost.
                    case 0:
                        return 61;
                    // $script:0808122107008796$
                    // - I'm not depressed.
                    case 1:
                        return 62;
                }
                return -1;
            case (61, 0):
                // $script:0808122107008797$
                // - On to the next portal! Since you've passed through the gate to $map:02000023$, the portal there will open new paths to you. But if there's nowhere to go, the portal won't work.
                return -1;
            case (62, 0):
                // $script:0808122107008798$
                // - You look worried. Go ahead, put your feet up and tell me your troubles.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.Close,
            (62, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
