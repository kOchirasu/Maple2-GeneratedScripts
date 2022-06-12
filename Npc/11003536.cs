using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003536: Nairin
/// </summary>
public class _11003536 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1126150707011935$
    // - Would you like to take on a mission for Green Hoods?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1126150707011936$
                // - How may I help you today, $male:Sir,female:Ma'am$?
                switch (selection) {
                    // $script:1126150707011937$
                    // - Why are Green Hoods here?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1126150707011938$
                // - That's a good question! Most people think we're simple rangers and woodswomen, wandering the forests of Henesys with our bows.
                return 31;
            case (31, 1):
                // $script:1126150707011939$
                // - But we're so much more than that! We know all about helping people and making sure they have everything they need.
                return 31;
            case (31, 2):
                // $script:1126150707011940$
                // - There's more to keeping the peace than simply being a good fighter. You need to know how to treat a wound and provide a shoulder to cry on.
                return 31;
            case (31, 3):
                // $script:1126150707011941$
                // - That's why we've been entrusted with support operations on Sky Fortress.
                return 31;
            case (31, 4):
                // $script:1126150707011942$
                // - Of course, you know firsthand how good we are in a fight. Even though I'm stationed up here on the bridge, I'm just as good with my bow as Eka!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Next,
            (31, 2) => NpcTalkButton.Next,
            (31, 3) => NpcTalkButton.Next,
            (31, 4) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
