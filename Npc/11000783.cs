using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000783: Loront
/// </summary>
public class _11000783 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002952$
    // - Eh? What in the world is going on?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002955$
                // - What if time never starts flowing again?
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
