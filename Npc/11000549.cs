using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000549: Tau
/// </summary>
public class _11000549 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407002328$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002331$
                // - Is today some kind of holiday? Why is everyone so busy? I think I've met more people today than in my entire life.
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
