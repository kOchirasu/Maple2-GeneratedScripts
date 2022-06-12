using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001868: Rachael
/// </summary>
public class _11001868 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1213150207007549$
    // - Ah, nice to see you!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1213150207007551$
                // - This mine is run by the Nerman Guild. We've got all the materials a blacksmith might need.
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
