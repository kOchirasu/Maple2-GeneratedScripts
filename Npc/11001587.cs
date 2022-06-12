using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001587: Ishura
/// </summary>
public class _11001587 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20;30
    }

    // Select 0:
    // $script:0504151707006075$
    // - Ah, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006123$
                // - There must be something about the power $npcName:11001231[gender:0]$  seeks in our ancestors' records.
                switch (selection) {
                    // $script:0515180307006124$
                    // - Why are you so sure?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0515180307006125$
                // - I encountered Holstatt in the Land of Darkness once. He said that Arazaad had kept a secret from us. That the real legacy of our ancestors was elsewhere. 
                return 11;
            case (11, 1):
                // $script:0515180307006126$
                // - I don't know if he was lying or not. But if he wasn't, then the old records, which only Arazaad could read, must hold clue about the secret. Something to point us towards this so-called legacy. 
                return -1;
            case (20, 0):
                // $script:0517210007006136$
                // - Why are you staring at me?
                switch (selection) {
                    // $script:0517210007006137$
                    // - I just wanted to see you.
                    case 0:
                        return 21;
                    // $script:0517210007006138$
                    // - I missed you so much!
                    case 1:
                        return 22;
                    // $script:0517210007006139$
                    // - Play with me.
                    case 2:
                        return 23;
                    // $script:0517210007006140$
                    // - There's something I need to tell you.
                    case 3:
                        return 24;
                }
                return -1;
            case (21, 0):
                // $script:0517210007006141$
                // - Ha... Weirdo... 
                return -1;
            case (22, 0):
                // $script:0517210007006142$
                // - Y-you did? So did I. Ahem.
                return -1;
            case (23, 0):
                // $script:0517210007006143$
                // - Now is <i>not</i> the time for such things!
                return -1;
            case (24, 0):
                // $script:0517210007006144$
                // - I'm a little busy right now.
                return -1;
            case (30, 0):
                // $script:0524142307006216$
                // - There must be something about the power $npcName:11001231[gender:0]$ seeks in our ancestors' records.
                switch (selection) {
                    // $script:0524142307006217$
                    // - Why are you so sure?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0524142307006218$
                // - I encountered Holstatt in the Land of Darkness once. He said that Arazaad had kept a secret from us. That the real legacy of our ancestors was elsewhere. 
                return -1;
            case (32, 0):
                // $script:0524142307006219$
                // - I don't know if he was lying or not. But if he wasn't, then the old records, which only Arazaad could read, must hold some clue about the secret. Something to point us towards this so-called legacy. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Close,
            (23, 0) => NpcTalkButton.Close,
            (24, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
