using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000997: Ravel
/// </summary>
public class _11000997 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003425$
    // - Ring, ring! Out of the way!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003428$
                // - Whew, that was close. You almost startled me right off the clock!
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
