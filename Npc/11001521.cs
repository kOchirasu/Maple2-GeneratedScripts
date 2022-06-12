using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001521: Archer
/// </summary>
public class _11001521 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0515211707006109$
    // - Nice to meet you!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515211707006110$
                // - I didn't expect $map:02000023$ to be quite this beautiful. When the boss told me the Green Hoods were joining this mission, I didn't know what to think. I've never been so far from home before... But I promise I won't let you down!
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
