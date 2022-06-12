using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000548: Leala
/// </summary>
public class _11000548 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002324$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002327$
                // - The militia will do everything we can to help you. We have to join forces to protect our world.
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
