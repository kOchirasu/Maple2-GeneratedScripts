using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000411: Meminem
/// </summary>
public class _11000411 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001734$
    // - Yo!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001736$
                // - You ask me, tagging is just as much art as sick beats and hot moves. Some people say I'm just some punk, but they don't know what they're talking about.
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
