using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004347: Mia
/// </summary>
public class _11004347 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011751$
    // - I must remain calm... I can resolve this... All things in their proper place...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011752$
                // - If there's a problem, solve it! Blaming and complaining won't fix anything!
                switch (selection) {
                    // $script:1109213607011753$
                    // - Things aren't looking so good right now... are you okay?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109213607011754$
                // - Yes, of course! Obviously we just need to remain calm and composed. CALM AND COMPOSED!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
