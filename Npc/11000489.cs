using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000489: Hani
/// </summary>
public class _11000489 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002142$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002145$
                // - He's so hot, and his voice is amaaazing. When I hear him sing, I can hardly control myself!
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
