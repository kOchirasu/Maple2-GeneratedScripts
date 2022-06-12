using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003648: Poppy
/// </summary>
public class _11003648 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009194$
    // - What a creepy place...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009195$
                // - Oh, $MyPCName$! What a pleasant surprise.
                switch (selection) {
                    // $script:1109121007009196$
                    // - Have we met?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009197$
                // - You wound me. We've talked at length, my friend! Of course, I was wearing a different face at the time...
                switch (selection) {
                    // $script:1109121007009198$
                    // - I honestly have no idea who you are.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009199$
                // - A pity. Anyway, you must be here about the dragon-man.
                switch (selection) {
                    // $script:1109121007009200$
                    // - Who said anything about a dragon-man?
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009201$
                // - Don't be so transparent, my friend. I already knew why you were here from the beginning.
                switch (selection) {
                    // $script:1109121007009202$
                    // - $npcName:11003535[gender:1]$ sent me...
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:1109121007009203$
                // - Then please pass my message along to her: "Torch. Jar. Treasure chest."
                switch (selection) {
                    // $script:1109121007009204$
                    // - All right.
                    case 0:
                        return 15;
                }
                return -1;
            case (15, 0):
                // $script:1109121007009205$
                // - I would advise you leave this place as soon as you can. It's most eerie here...
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
            (14, 0) => NpcTalkButton.SelectableDistractor,
            (15, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
