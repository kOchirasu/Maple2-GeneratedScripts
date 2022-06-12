using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003644: Ranka
/// </summary>
public class _11003644 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009150$
    // - This data just doesn't add up...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009151$
                // - Intern? You the intern? I've been waiting!
                switch (selection) {
                    // $script:1109121007009152$
                    // - I think you've got the wrong person.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009153$
                // - The heck I do! I'm too busy trying to making sense of this data to deal with your shenanigans.
                switch (selection) {
                    // $script:1109121007009154$
                    // - If you say so...
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009155$
                // - I do, indeed! Now, <i>intern</i>, the first thing you'll want to do is memorize a very special phrase.
                switch (selection) {
                    // $script:1109121007009156$
                    // - Oh? Oh! Yes. I'm listening.
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009157$
                // - Listen up! "Bolt. Driver. Scale."
                switch (selection) {
                    // $script:1109121007009158$
                    // - Noted.
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:1109121007009159$
                // - That's all for now, intern. But before you go...
                switch (selection) {
                    // $script:1109121007009160$
                    // - Yes?
                    case 0:
                        return 15;
                }
                return -1;
            case (15, 0):
                // $script:1109121007009161$
                // - Would you tell our mutual friend that I need a new assignment? This place is driving me mad.
                switch (selection) {
                    // $script:1109121007009162$
                    // - I'll let her know.
                    case 0:
                        return 16;
                }
                return -1;
            case (16, 0):
                // $script:1109121007009163$
                // - No more data... No more...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.SelectableDistractor,
            (15, 0) => NpcTalkButton.SelectableDistractor,
            (16, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
