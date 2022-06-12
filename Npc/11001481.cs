using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001481: Dunba
/// </summary>
public class _11001481 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0106111607005769$
    // - Ugh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0106111607005770$
                // - When $npcName:23000068[gender:0]$ returns... Aww... $npcName:11001472[gender:1]$ has to get better soon...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
