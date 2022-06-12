using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001124: Hanu
/// </summary>
public class _11001124 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0910171307003840$
    // - Did you come to see me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0915113107003932$
                // - I've been studying artificial intelligence. Androids in particular. Do you think that my androids are capable of thinking like we do?
                switch (selection) {
                    // $script:0915113107003933$
                    // - I don't see why not.
                    case 0:
                        return 31;
                    // $script:0915113107003934$
                    // - I don't think so.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0915113107003935$
                // - Haha! I wasn't expecting a real answer. After all, it's a question I struggle with myself.
                return -1;
            case (32, 0):
                // $script:0915113107003936$
                // - Hmm? You can't just say something like that and leave it at that! Then tell me, what do you think I should do to make my androids as smart as you and me?
                switch (selection) {
                    // $script:0915113107003937$
                    // - Data isn't enough. They have to learn through experience.
                    case 0:
                        return 33;
                    // $script:0915113107003938$
                    // - Just cram them full of as much data as you can.
                    case 1:
                        return 34;
                    // $script:0915113107003939$
                    // - (Mumble inaudibly.)
                    case 2:
                        return 35;
                }
                return -1;
            case (33, 0):
                // $script:0915113107003940$
                // - Don't you think I tried that already? Well, thanks for your input in any case. As a professional in the field of android research, I'm sure I'll come up with a solution on my own.
                return -1;
            case (34, 0):
                // $script:0915113107003941$
                // - Yes, I've thought much the same. Perhaps if I build a database based on what my androids learn from various stimuli, much as humans learn from their own experience. Thanks for your input, in any case.
                return -1;
            case (35, 0):
                // $script:0915113107003942$
                // - What? Hmph. I really thought you had something of value to say on the topic. Next time someone asks for your opinion, you should just be honest with them.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.Close,
            (35, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
