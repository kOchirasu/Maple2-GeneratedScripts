using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000321: Irena
/// </summary>
public class _11000321 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407001258$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407001263$
                // - Can I talk to you about something?
                switch (selection) {
                    // $script:0831180407001264$
                    // - Sure.
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:0831180407001265$
                // - One of the guys in my neighborhood keeps making fun of my face. He says I'm ugly. Am I... really that ugly? Please be honest with me.
                switch (selection) {
                    // $script:0831180407001266$
                    // - Nope!
                    case 0:
                        return 52;
                    // $script:0831180407001267$
                    // - Yep!
                    case 1:
                        return 53;
                }
                return -1;
            case (52, 0):
                // $script:0831180407001268$
                // - Really? You really don't think I'm ugly? Then... do you think he'll think I'm pretty?
                switch (selection) {
                    // $script:0831180407001269$
                    // - Well, I didn't say you're pretty, either.
                    case 0:
                        return 53;
                    // $script:0831180407001270$
                    // - Who is he?
                    case 1:
                        return 54;
                }
                return -1;
            case (53, 0):
                // $script:0831180407001271$
                // - Oh, I see... Then maybe I should really think about getting cosmetic surgery. Thank you... for depressing me further...
                return 53;
            case (53, 1):
                // $script:0831180407001272$
                // - Then do you think I'll look pretty if I get cosmetic surgery? I really want to look pretty for him.
                switch (selection) {
                    // $script:0831180407001273$
                    // - Who is he?
                    case 0:
                        return 54;
                    // $script:0831180407001274$
                    // - Yeah, I mean... maybe that'll work.
                    case 1:
                        return 57;
                }
                return -1;
            case (54, 0):
                // $script:0831180407001275$
                // - I don't know his name. He's one of the travelers who came to $map:02000001$ because of the court.
                return 54;
            case (54, 1):
                // $script:0831180407001276$
                // - Big blue eyes. Beautiful golden hair. He looks so dashing with the sword on his belt! And his polka-dot scarf... it's so cute! Have you ever seen anyone so amazing before?
                switch (selection) {
                    // $script:0831180407001277$
                    // - No.
                    case 0:
                        return 55;
                    // $script:0831180407001278$
                    // - Yes.
                    case 1:
                        return 55;
                }
                return -1;
            case (55, 0):
                // $script:0831180407001279$
                // - You know, sometimes he looks around as if he's waiting for someone. Do you think he has a girlfriend? What if he has a girlfriend?
                switch (selection) {
                    // $script:0831180407001280$
                    // - I don't know.
                    case 0:
                        return 56;
                    // $script:0831180407001281$
                    // - I don't think he has a girlfriend.
                    case 1:
                        return 56;
                }
                return -1;
            case (56, 0):
                // $script:0831180407001282$
                // - So, you don't know. Three times a day, in the morning, at noon, and in the evening, I go out to the main road. I pretend to take a stroll, just to steal a few glances at him. Ah, I want to see him again! Do you think I'm in love?
                return -1;
            case (57, 0):
                // $script:0831180407001283$
                // - Do you think so? Okay, then I really need to go to $map:02000107$...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.Next,
            (53, 1) => NpcTalkButton.SelectableDistractor,
            (54, 0) => NpcTalkButton.Next,
            (54, 1) => NpcTalkButton.SelectableDistractor,
            (55, 0) => NpcTalkButton.SelectableDistractor,
            (56, 0) => NpcTalkButton.Close,
            (57, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
