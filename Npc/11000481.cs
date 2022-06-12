using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000481: Quarry Worker
/// </summary>
public class _11000481 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407002103$
    // - I'm busy. Why are you bothering me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002108$
                // - I'm busy. If you're not going to help, then at least don't get in my way.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
