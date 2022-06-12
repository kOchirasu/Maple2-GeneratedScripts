using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004033: Orde
/// </summary>
public class _11004033 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010051$
    // - Ugh, I hate field duty...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010052$
                // - It's dangerous outside the blanket, $MyPCName$.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
