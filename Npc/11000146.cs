using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000146: Andy
/// </summary>
public class _11000146 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:0831180407000622$
    // - Oh, no...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000625$
                // - I'm getting tired of ending up in unfamiliar places!
                return -1;
            case (40, 0):
                // $script:0831180407000626$
                // - I want out of this jungle the first chance I get. I can't wait to go back home.
                return -1;
            case (50, 0):
                // $script:0831180407000627$
                // - Sigh, I'm tired of traveling through time. I always end up in places that I don't want to be
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
