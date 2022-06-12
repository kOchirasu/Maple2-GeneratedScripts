using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000005: Anne
/// </summary>
public class _11000005 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 80;90
    }

    // Select 0:
    // $script:0831180407000020$
    // - Let's see... So, this book goes... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (80, 0):
                // $script:0116174407009791$
                // - Is there anything that you can't learn in a book?
                return 80;
            case (80, 1):
                // $script:0116174407009792$
                // - Here's a familiar face. Have you finally decided to focus on higher education? I knew you'd come around eventually.
                switch (selection) {
                    // $script:0116174407009793$
                    // - Actually, I'm here to do some research on Orbis.
                    case 0:
                        return 81;
                }
                return -1;
            case (81, 0):
                // $script:0116174407009794$
                // - Ah, the floating city. It was world-famous for its astonishing vistas. Unfortunately, it was destroyed in the war.
                return 81;
            case (81, 1):
                // $script:0116174407009795$
                // - Even though the city is in ruins, the city center still burns to this day. Not a very pleasant place to live these days.
                switch (selection) {
                    // $script:0116174407009796$
                    // - What else can you tell me about it?
                    case 0:
                        return 82;
                }
                return -1;
            case (82, 0):
                // $script:0116174407009797$
                // - That depends. What, specifically, do you want to know?
                switch (selection) {
                    // $script:0116174407009798$
                    // - If Orbis is still on fire, where is the heat coming from?
                    case 0:
                        return 83;
                }
                return -1;
            case (83, 0):
                // $script:0116174407009799$
                // - Ah, now that is a curious question! I think I read something about that once...
                return 83;
            case (83, 1):
                // $script:0116174407009800$
                // - In Orbis, the floating city, a very special cave exists. A cave where magma flows endlessly.
                switch (selection) {
                    // $script:0116174407009801$
                    // - Do you know where the cave is?
                    case 0:
                        return 84;
                }
                return -1;
            case (84, 0):
                // $script:0116174407009802$
                // - No, but it shouldn't be too hard for me to find out. Actually getting to Orbis, however, is a fool's errand. I doubt anybody could survive there for long.
                switch (selection) {
                    // $script:0116174407009803$
                    // - It's a good thing I'm not just anybody.
                    case 0:
                        return 85;
                }
                return -1;
            case (85, 0):
                // $script:0116174407009804$
                // - Hopelessly reckless, as usual. I'll tell you where to go, but that's it. I'll have nothing more to do with this.
                switch (selection) {
                    // $script:0116174407009805$
                    // - Thank you for your time.
                    case 0:
                        return 86;
                }
                return -1;
            case (86, 0):
                // $script:0116174407009806$
                // - Don't mention it. Please. You'll forgive me for not seeing you off...
                return -1;
            case (90, 0):
                // $script:0504174607009860$
                // - Is there nothing you can't learn from a book?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (80, 0) => NpcTalkButton.Next,
            (80, 1) => NpcTalkButton.SelectableDistractor,
            (81, 0) => NpcTalkButton.Next,
            (81, 1) => NpcTalkButton.SelectableDistractor,
            (82, 0) => NpcTalkButton.SelectableDistractor,
            (83, 0) => NpcTalkButton.Next,
            (83, 1) => NpcTalkButton.SelectableDistractor,
            (84, 0) => NpcTalkButton.SelectableDistractor,
            (85, 0) => NpcTalkButton.SelectableDistractor,
            (86, 0) => NpcTalkButton.Close,
            (90, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
