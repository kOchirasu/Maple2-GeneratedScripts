using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000311: Isaac
/// </summary>
public class _11000311 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1121222006000825$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1121222006000826$
                // - I'm going to be rich, no matter what it takes!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
