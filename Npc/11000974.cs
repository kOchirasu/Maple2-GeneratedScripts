using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000974: Mani
/// </summary>
public class _11000974 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003370$
    // - Welcome, and thank you for coming all the way here.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003372$
                // - It gives me tremendous pleasure to watch people enjoying my food. Ho, ho!
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
