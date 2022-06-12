using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003080: Columbo
/// </summary>
public class _11003080 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0113143107007757$
    // - Ahhh, I want to get better soon so I can go on adventures again!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0113143107007760$
                // - How soon until I can sail again? Cough, cough! I want to be well so I can set off to find the wonders of the world.
                return -1;
            case (40, 0):
                // $script:0113143107007761$
                // - $MyPCName$, thank you for telling me about your adventures! I hope I can get better so I can have my own adventures, too.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
