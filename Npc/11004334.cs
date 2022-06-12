using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004334: Claudine
/// </summary>
public class _11004334 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1010140307011584$
    // - Wow...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1010140307011585$
                // - This place has exceeded my every expectation.
                return 10;
            case (10, 1):
                // $script:1010140307011586$
                // - To think, we're standing in a land where magic has been made to serve technology. It's almost too good to be true!
                return 10;
            case (10, 2):
                // $script:1010140307011587$
                // - See how these magic stones have been reduced to mere tools, like the cogwheel and the level?
                return 10;
            case (10, 3):
                // $script:1010140307011588$
                // - I must learn everything about this place...
                return 10;
            case (10, 4):
                // $script:1010140307011589$
                // - Soon, the Resistance will dominate Maple World using the technology of Kritias!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Next,
            (10, 4) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
