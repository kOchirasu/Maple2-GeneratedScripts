using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000428: Hatto
/// </summary>
public class _11000428 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001782$
    // - Why are you bothering me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001784$
                // - A true adventurer dives head-first into trouble! He's not afraid of jumping off a cliff into a sea of lava or fighting giant, rampaging monsters!
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
