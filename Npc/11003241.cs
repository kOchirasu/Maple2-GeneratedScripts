using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003241: Ralph
/// </summary>
public class _11003241 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008138$
    // - Ugh!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008141$
                // - $MyPCName$? Why?!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
