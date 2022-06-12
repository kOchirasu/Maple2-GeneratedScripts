using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004108: Lanemone
/// </summary>
public class _11004108 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720125407010457$
    // - Hah... Well, that opened up a can of worms.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720125407010458$
                // - This had better be important.
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
