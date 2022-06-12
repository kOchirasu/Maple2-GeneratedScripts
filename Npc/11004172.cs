using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004172: Dunba
/// </summary>
public class _11004172 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010606$
    // - Ugh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010607$
                // - Blam, blam! Oh, hey. I'm just practicing my aim. I don't want to let my squad down.
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
