using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000242: Viola
/// </summary>
public class _11000242 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001023$
    // - Welcome! Ho, ho, ho.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001026$
                // - Did you come alone? Our guests usually arrive as couples. Ho, ho, ho.
                return 30;
            case (30, 1):
                // $script:0831180407001027$
                // - Have a seat. I hope you don't feel out of place. We do get singles up here once in awhile. Sometimes they even find someone to leave with!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
