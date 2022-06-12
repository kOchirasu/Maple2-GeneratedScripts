using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001111: Lennon
/// </summary>
public class _11001111 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0908154107003736$
    // - Hmm... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0908154107003737$
                // - The soul inside this orb... If it's left alone for too long, it'll be swallowed by the enormous darkness that is the Shadow World.
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
