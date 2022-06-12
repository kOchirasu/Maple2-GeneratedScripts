using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001337: Lequan
/// </summary>
public class _11001337 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005267$
    // - You have something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005270$
                // - You here to talk, or you here to skate? Heh... Good luck.
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
