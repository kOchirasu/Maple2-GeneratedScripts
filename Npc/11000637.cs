using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000637: Prisoner 140920
/// </summary>
public class _11000637 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407002596$
    // - Get me out of here... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407002599$
                // - Excuse me... Please get me out of here! I promise I'll never misbehave again!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
