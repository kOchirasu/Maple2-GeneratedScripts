using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003639: Greg
/// </summary>
public class _11003639 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009103$
    // - Retiring here is the best choice I ever made!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009104$
                // - You here to see the fight? I never miss a match. I even brought my own binoculars so I can see every drop of sweat and every knocked-out tooth!
                switch (selection) {
                    // $script:1109121007009105$
                    // - Nah, I'm not into blood sports.
                    case 0:
                        return 11;
                    // $script:1109121007009106$
                    // - Sure am! I'm a huge fan.
                    case 1:
                        return 12;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009107$
                // - Really? Huh. Never thought $npcName:11003535[gender:1]$ would recruit an agent with such a weak stomach.
                switch (selection) {
                    // $script:1109121007009108$
                    // - Ah, so you're with Dark Wind.
                    case 0:
                        return 13;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009109$
                // - I knew I liked you the moment I saw you! $npcName:11003535[gender:1]$'s got great taste in agents.
                switch (selection) {
                    // $script:1109121007009110$
                    // - Ah, so you're with Dark Wind.
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009111$
                // - Anyway, you're here for my special message, right? "Mask. Duck butt. Beast."
                switch (selection) {
                    // $script:1109121007009112$
                    // - I'll pass that along.
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:1109121007009113$
                // - Shush! The fight's about to start!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
