using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000390: Olson
/// </summary>
public class _11000390 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001585$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001587$
                // - We've been busy. People are still checking in, with no idea the empress's gathering has been canceled.
                return -1;
            case (30, 0):
                // $script:0831180407001588$
                // - The empress is no longer holding court, but we're still booked up. I don't think most people have heard the news yet.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
