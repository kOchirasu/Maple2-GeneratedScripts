using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003210: Zeta
/// </summary>
public class _11003210 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0404083307008239$
    // - I came to repay you for saving my brother. Now we're even.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0404083307008240$
                // - Don't say I never did nothing for you.
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
