using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003643: Kevin
/// </summary>
public class _11003643 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009142$
    // - Well done, well done.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009143$
                // - You must be the new grad student.
                switch (selection) {
                    // $script:1109121007009144$
                    // - Not exactly...
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009145$
                // - No? Then you must be one of $npcName:11003535[gender:1]$'s $male:men,female:women$. There aren't many other reasons to come to this pit...
                switch (selection) {
                    // $script:1109121007009146$
                    // - This can't be an easy posting.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009147$
                // - It is what it is. Anyway, you're here for a coded message, right? "Queen. Ace of Spades. Ten of Clovers."
                switch (selection) {
                    // $script:1109121007009148$
                    // - I'll pass that along.
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009149$
                // - I really need to take some leave when this is all over.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
