using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004495: Joule 
/// </summary>
public class _11004495 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012362$
    // - The gravity, erm, situation in this place is fascinating. Why, these huge structures look as though they might simply float away.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012363$
                // - The gravity, erm, situation in this place is fascinating. Why, these huge structures look as though they might simply float away.
                switch (selection) {
                    // $script:1227192907012364$
                    // - How's the research going?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012365$
                // - It's early to say, but I think this could lead to a second energy revolution.
                return 11;
            case (11, 1):
                // $script:1227192907012366$
                // - Think about it. The vast majority of Sky Fortress's power generation goes into keeping it in the air. How might we use that power if we had aetherine to lift the ship aloft, instead?
                switch (selection) {
                    // $script:0114163707012715$
                    // - That would be incredible.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0114163707012716$
                // - And that's why we've got to learn everything we can about aetherine.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
