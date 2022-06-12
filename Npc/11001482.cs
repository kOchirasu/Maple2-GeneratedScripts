using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001482: Dunba
/// </summary>
public class _11001482 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0106111607005771$
    // - Ugh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0106111607005774$
                // - W-what do I do now? We finally got the Lumenstone back, but I dropped it into a pool of water. $npcName:11001292[gender:0]$ and $npcName:11001218[gender:1]$ are looking for it... but I can't swim... I feel useless.
                switch (selection) {
                    // $script:0106111607005775$
                    // - You should calm down.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0106111607005776$
                // - If $npcName:23000068[gender:0]$ finds out we lost the Lumenstone, he'll come after us. Could you hold off $npcName:23000068[gender:0]$ until we get the Lumenstone back?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
