using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000144: Tristan
/// </summary>
public class _11000144 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;50;60
    }

    // Select 0:
    // $script:0831180407000587$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000589$
                // - How did you make it this far?
                switch (selection) {
                    // $script:0831180407000590$
                    // - I walked.
                    case 0:
                        return 21;
                    // $script:0831180407000591$
                    // - I ran.
                    case 1:
                        return 21;
                    // $script:0831180407000592$
                    // - I flew.
                    case 2:
                        return 21;
                    // $script:0831180407000593$
                    // - It just happened.
                    case 3:
                        return 22;
                }
                return -1;
            case (21, 0):
                // $script:0831180407000594$
                // - You know that's not the answer I wanted. You think this is all a big joke, don't you? Well, let me give you some advice.
                return 21;
            case (21, 1):
                // $script:0831180407000595$
                // - Go back to where you came from. You're too young to die like a rat out here.
                return -1;
            case (22, 0):
                // $script:0831180407000596$
                // - Then turn around and leave. It's too dangerous for you to hang around here.
                return -1;
            case (50, 0):
                // $script:0831180407000598$
                // - Mm? Are you here to find the $map:02000037$ where $npcName:23090005[gender:0]$ is sealed?
                switch (selection) {
                    // $script:0831180407000599$
                    // - Yep!
                    case 0:
                        return 51;
                    // $script:0831180407000600$
                    // - Nope!
                    case 1:
                        return 53;
                }
                return -1;
            case (51, 0):
                // $script:0831180407000601$
                // - What is your purpose? Is there someone that you want to protect? Or do you covet $npcName:23090005[gender:0]$'s treasure?
                switch (selection) {
                    // $script:0831180407000602$
                    // - I'm here to protect all of Maple World.
                    case 0:
                        return 52;
                    // $script:0831180407000603$
                    // - I want treasure!
                    case 1:
                        return 54;
                }
                return -1;
            case (52, 0):
                // $script:0831180407000604$
                // - The whole world, eh? What a ridiculous goal...
                return 52;
            case (52, 1):
                // $script:0831180407000605$
                // - But goals like that keep a $male:man,female:woman$ going against impossible odds. I can respect that. Don't you dare fail!
                return 52;
            case (52, 2):
                // $script:0831180407000606$
                // - I'm jealous, actually. Jealous that you can still have a bold dream like that. I've seen too many battles to even comprehend a dream like that...
                return 52;
            case (52, 3):
                // $script:0831180407000607$
                // - Ah, to be young and foolish again.
                return -1;
            case (53, 0):
                // $script:0831180407000610$
                // - Not that it's my place to judge, mind. Your life is yours to throw away as you please.
                return -1;
            case (54, 0):
                // $script:0831180407000608$
                // - Another treasure seeker, then...
                return 54;
            case (54, 1):
                // $script:0831180407000609$
                // - The treasure is great, to be certain. But is it worth risking your life over?
                return -1;
            case (60, 0):
                // $script:1026170307004301$
                // - If $item:30000419$ is what you're after, you should talk to $npcName:11001210[gender:0]$ in $map:02000023$. I'm sure he can help you.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Next,
            (21, 1) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.Next,
            (52, 1) => NpcTalkButton.Next,
            (52, 2) => NpcTalkButton.Next,
            (52, 3) => NpcTalkButton.Close,
            (53, 0) => NpcTalkButton.Close,
            (54, 0) => NpcTalkButton.Next,
            (54, 1) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
