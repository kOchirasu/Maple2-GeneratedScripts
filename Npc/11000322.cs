using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000322: Clara
/// </summary>
public class _11000322 : NpcScript {
    internal _11000322(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001285$ 
                // - How may I help you?
                return true;
            case 40:
                // $script:0831180407001289$ 
                // - $MyPCName$, are you an adventurer? Have you ever seen a rainbow?
                switch (selection) {
                    // $script:0831180407001290$
                    // - Yep.
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180407001291$
                    // - Nope.
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407001292$ 
                // - Whoa! What does it look like? $npcName:11000174[gender:1]$ says there's always a big rainbow over the dam!
                switch (selection) {
                    // $script:0831180407001293$
                    // - Who is $npcName:11000174[gender:1]$?
                    case 0:
                        Id = 43;
                        return false;
                    // $script:0831180407001294$
                    // - Where is the dam?
                    case 1:
                        Id = 44;
                        return false;
                }
                return true;
            case 42:
                // $script:0831180407001295$ 
                // - Hmm, really? $npcName:11000174[gender:1]$ wrote to me in a letter that there's always a rainbow over the dam!
                switch (selection) {
                    // $script:0831180407001296$
                    // - Who is $npcName:11000174[gender:1]$?
                    case 0:
                        Id = 43;
                        return false;
                    // $script:0831180407001297$
                    // - Where is the dam?
                    case 1:
                        Id = 44;
                        return false;
                }
                return true;
            case 43:
                // $script:0831180407001298$ 
                // - $npcName:11000174[gender:1]$ is my cousin living near the dam. She used to live here until her father had to move there for work. I wish I had to move out there too...
                return true;
            case 44:
                // $script:0831180407001299$ 
                // - Mm, I don't know exactly. $MyPCName$, do you think you could find it? I'd give anything to see it!
                return true;
            default:
                return true;
        }
    }
}
