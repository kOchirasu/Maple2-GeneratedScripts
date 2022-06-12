using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000322: Clara
/// </summary>
public class _11000322 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407001285$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407001289$
                // - $MyPCName$, are you an adventurer? Have you ever seen a rainbow?
                switch (selection) {
                    // $script:0831180407001290$
                    // - Yep.
                    case 0:
                        return 41;
                    // $script:0831180407001291$
                    // - Nope.
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0831180407001292$
                // - Whoa! What does it look like? $npcName:11000174[gender:1]$ says there's always a big rainbow over the dam!
                switch (selection) {
                    // $script:0831180407001293$
                    // - Who is $npcName:11000174[gender:1]$?
                    case 0:
                        return 43;
                    // $script:0831180407001294$
                    // - Where is the dam?
                    case 1:
                        return 44;
                }
                return -1;
            case (42, 0):
                // $script:0831180407001295$
                // - Hmm, really? $npcName:11000174[gender:1]$ wrote to me in a letter that there's always a rainbow over the dam!
                switch (selection) {
                    // $script:0831180407001296$
                    // - Who is $npcName:11000174[gender:1]$?
                    case 0:
                        return 43;
                    // $script:0831180407001297$
                    // - Where is the dam?
                    case 1:
                        return 44;
                }
                return -1;
            case (43, 0):
                // $script:0831180407001298$
                // - $npcName:11000174[gender:1]$ is my cousin living near the dam. She used to live here until her father had to move there for work. I wish I had to move out there too...
                return -1;
            case (44, 0):
                // $script:0831180407001299$
                // - Mm, I don't know exactly. $MyPCName$, do you think you could find it? I'd give anything to see it!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.Close,
            (44, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
