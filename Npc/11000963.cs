using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000963: Kamil
/// </summary>
public class _11000963 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003345$
    // - There are wounded people here. They need help!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003347$
                // - Folks like me don't make money sitting around on our butts. We're always on the move, looking for new buyers.
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
