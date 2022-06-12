using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004270: Rainy
/// </summary>
public class _11004270 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011230$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011231$
                // - ...
                return 10;
            case (10, 1):
                // $script:0911203207011232$
                // - Stop stomping around so loudly! You're giving me away!
                switch (selection) {
                    // $script:0911203207011233$
                    // - Sorry. What're you up to?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0911203207011234$
                // - Isn't it obvious? I'm observing! This data is gonna be used in an amazing research paper I'm gonna write.
                switch (selection) {
                    // $script:0911203207011235$
                    // - Sure, but what's with the disguise?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0911203207011236$
                // - Look around! The ecosystem here is an impossible combination of nature and machine. There's so much we don't know about this place.
                return 12;
            case (12, 1):
                // $script:0911203207011237$
                // - Now add in my disguise, and the answer to your question should be obvious, right?
                switch (selection) {
                    // $script:0911203207011238$
                    // - I still don't get it.
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0911203207011239$
                // - Ugh, use your brain! I'm conducting <b>monster research</b>! I'm in costume so they don't flee or attack. Obviously.
                return 13;
            case (13, 1):
                // $script:0911203207011240$
                // - Now that I've answered your question, can you run along? I haven't moved from this spot for a week, and the last thing I want is for you to ruin my research!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Next,
            (13, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
