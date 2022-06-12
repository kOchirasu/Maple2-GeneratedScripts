using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000154: Sophia
/// </summary>
public class _11000154 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000656$
    // - I can't get rid of these chubby cheeks, no matter how hard I try.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000659$
                // - Goodness, just LOOK at those clothes! Did you dig them out of some ancient ruins? Might be nice to wear something made in the last decade.
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
