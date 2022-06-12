using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000129: Alvin
/// </summary>
public class _11000129 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407000552$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407000555$
                // - I took the Royal Road for granted. I've never been on a path so dangerous before. 
                return 40;
            case (40, 1):
                // $script:0831180407000556$
                // - And even if you get through this awful forest, there's a treacherous valley to cross. The cliffs of $map:02000051$ are nothing compared to what's ahead! Ahh, I'm never getting out of here alive...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
