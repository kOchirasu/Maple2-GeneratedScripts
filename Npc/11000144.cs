using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000144: Tristan
/// </summary>
public class _11000144 : NpcScript {
    internal _11000144(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000587$ 
                // - What brings you here?
                return true;
            case 20:
                // $script:0831180407000589$ 
                // - How did you make it this far?
                switch (selection) {
                    // $script:0831180407000590$
                    // - I walked.
                    case 0:
                        Id = 21;
                        return false;
                    // $script:0831180407000591$
                    // - I ran.
                    case 1:
                        Id = 21;
                        return false;
                    // $script:0831180407000592$
                    // - I flew.
                    case 2:
                        Id = 21;
                        return false;
                    // $script:0831180407000593$
                    // - It just happened.
                    case 3:
                        Id = 22;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407000594$ 
                // - You know that's not the answer I wanted. You think this is all a big joke, don't you? Well, let me give you some advice.
                // $script:0831180407000595$ 
                // - Go back to where you came from. You're too young to die like a rat out here.
                return true;
            case 22:
                // $script:0831180407000596$ 
                // - Then turn around and leave. It's too dangerous for you to hang around here.
                return true;
            case 50:
                // $script:0831180407000598$ 
                // - Mm? Are you here to find the $map:02000037$ where $npcName:23090005[gender:0]$ is sealed?
                switch (selection) {
                    // $script:0831180407000599$
                    // - Yep!
                    case 0:
                        Id = 51;
                        return false;
                    // $script:0831180407000600$
                    // - Nope!
                    case 1:
                        Id = 53;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407000601$ 
                // - What is your purpose? Is there someone that you want to protect? Or do you covet $npcName:23090005[gender:0]$'s treasure?
                switch (selection) {
                    // $script:0831180407000602$
                    // - I'm here to protect all of Maple World.
                    case 0:
                        Id = 52;
                        return false;
                    // $script:0831180407000603$
                    // - I want treasure!
                    case 1:
                        Id = 54;
                        return false;
                }
                return true;
            case 52:
                // $script:0831180407000604$ 
                // - The whole world, eh? What a ridiculous goal...
                // $script:0831180407000605$ 
                // - But goals like that keep a $male:man,female:woman$ going against impossible odds. I can respect that. Don't you dare fail!
                // $script:0831180407000606$ 
                // - I'm jealous, actually. Jealous that you can still have a bold dream like that. I've seen too many battles to even comprehend a dream like that...
                // $script:0831180407000607$ 
                // - Ah, to be young and foolish again.
                return true;
            case 53:
                // $script:0831180407000610$ 
                // - Not that it's my place to judge, mind. Your life is yours to throw away as you please.
                return true;
            case 54:
                // $script:0831180407000608$ 
                // - Another treasure seeker, then...
                // $script:0831180407000609$ 
                // - The treasure is great, to be certain. But is it worth risking your life over?
                return true;
            case 60:
                // $script:1026170307004301$ 
                // - If $item:30000419$ is what you're after, you should talk to $npcName:11001210[gender:0]$ in $map:02000023$. I'm sure he can help you.
                return true;
            default:
                return true;
        }
    }
}
