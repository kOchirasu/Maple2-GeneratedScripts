using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001467: Morak
/// </summary>
public class _11001467 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1223035407005528$
    // - Let's get to work.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1223035407005531$
                // - We have a saying in the construction industry: safety first. That means that it's none of my business if you do something stupid and get hurt!
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
