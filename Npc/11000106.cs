using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000106: Cecilia
/// </summary>
public class _11000106 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:0831180407000433$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000436$
                // - Don't talk to me.
                return -1;
            case (40, 0):
                // $script:0831180407000437$
                // - Eww. Stranger danger!
                return -1;
            case (50, 0):
                // $script:1215101207009666$
                // - What?
                return 50;
            case (50, 1):
                // $script:1215101207009667$
                // - Don't talk to me.
                switch (selection) {
                    // $script:1215101207009668$
                    // - What can you tell me about trading airships?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1215101207009669$
                // - Airships? I don't know anything about that.
                switch (selection) {
                    // $script:1215101207009670$
                    // - Are you sure you haven't heard <i>ANYTHING</i>?
                    case 0:
                        return 52;
                }
                return -1;
            case (52, 0):
                // $script:1215101207009671$
                // - Ugh, how annoying. That weird guy from earlier was asking the same questions.
                switch (selection) {
                    // $script:1215101207009672$
                    // - I'm going to keep bothering you until you talk to me...
                    case 0:
                        return 53;
                }
                return -1;
            case (53, 0):
                // $script:1215101207009673$
                // - Ugh! Fine! There are some rumors flying around about airships going missing, but I don't remember any of the details because they were boring. 
                return 53;
            case (53, 1):
                // $script:1215101207009674$
                // - I don't even know if they're the same airships you're talking about, just that some have supposedly gone missing. There, are you happy?
                switch (selection) {
                    // $script:1215101207009675$
                    // - Thanks. You've been a <i>biiig</i> help.
                    case 0:
                        return 54;
                }
                return -1;
            case (54, 0):
                // $script:1215101207009676$
                // - Don't act like we're friends now.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.Next,
            (53, 1) => NpcTalkButton.SelectableDistractor,
            (54, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
