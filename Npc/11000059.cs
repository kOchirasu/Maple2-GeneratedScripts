using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000059: Oyako
/// </summary>
public class _11000059 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000261$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000264$
                // - Do you live here?
                switch (selection) {
                    // $script:0831180407000265$
                    // - Yep!
                    case 0:
                        return 31;
                    // $script:0831180407000266$
                    // - Nope!
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000267$
                // - I knew it! I can tell you're from the city by your looks. How much money do you have to make to live in a neighborhood like this?
                return -1;
            case (32, 0):
                // $script:0831180407000268$
                // - Oh, no. You look so pale, I-I thought you lived here. I've never been to such a big place before, and everything is so amazing here. And I think I've seen more people today than I've ever seen in my hometown.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
