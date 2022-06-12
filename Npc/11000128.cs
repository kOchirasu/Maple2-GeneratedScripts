using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000128: Gary
/// </summary>
public class _11000128 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000549$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000551$
                // - I heard this path was dangerous. I didn't know it was this bad. You'd better be careful. 
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
