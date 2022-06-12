using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000112: Burfy
/// </summary>
public class _11000112 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407000463$
    // - What's up?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000464$
                // - Look at this. Terrible, isn't it? Geez, I've never seen such a big fissure.
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
