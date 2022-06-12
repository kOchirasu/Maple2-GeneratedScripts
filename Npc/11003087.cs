using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003087: Orde
/// </summary>
public class _11003087 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0207122607007928$
    // - Ugh, I hate field duty...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0207122607007929$
                // - It's dangerous outside the blanket, $MyPCName$.
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
