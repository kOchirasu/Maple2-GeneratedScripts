using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003265: Abandoned Notebook
/// </summary>
public class _11003265 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008210$
    // - <font color="#909090">(This log was tucked away in an inconspicuous corner.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008211$
                // - <font color="#909090">(It looks like this was abandoned, and yet it's suspiciously free of dust.)</font>
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
