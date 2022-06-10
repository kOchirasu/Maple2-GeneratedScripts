using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000650: Prisoner 170122
/// </summary>
public class _11000650 : NpcScript {
    internal _11000650(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002663$ 
                // - When can I get out of here? 
                return true;
            case 40:
                // $script:0831180407002667$ 
                // - Huh? You don't look like an inmate. 
                switch (selection) {
                    // $script:0831180407002668$
                    // - What are you doing?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002669$ 
                // - Are you blind? I'm working! I have to pull a million weeds to have my sentence reduced. Ugh, I'll grow old before I can pull that many weeds. 
                return true;
            case 50:
                // $script:1210061907004920$ 
                // - Huh? You don't look like an inmate. 
                switch (selection) {
                    // $script:1210061907004921$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1214232707004979$ 
                // - How do you know <i>that man</i>? 
                switch (selection) {
                    // $script:1214232707004980$
                    // - I'm working with him.
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:1214232707004981$ 
                // - Hm... Yes, there is something special about you. What brings you here, then? 
                switch (selection) {
                    // $script:1214232707004982$
                    // - I'm here on $npcName:11001231[gender:0]$'s behalf.
                    case 0:
                        Id = 53;
                        return false;
                }
                return true;
            case 53:
                // $script:1214232707004983$ 
                // - He's just as impatient as the supervisor, eh? Well, if you're here on business, you better talk to him. 
                switch (selection) {
                    // $script:1214232707004984$
                    // - Who is this supervisor?
                    case 0:
                        Id = 54;
                        return false;
                }
                return true;
            case 54:
                // $script:1214232707004985$ 
                // - $npcName:11000651[gender:0]$. But he doesn't talk to nobody without the password. That's the rule. And, to keep things nice and secure, we change it every three days. 
                switch (selection) {
                    // $script:1214232707004986$
                    // - What's the password?
                    case 0:
                        Id = 55;
                        return false;
                }
                return true;
            case 55:
                // $script:1214232707004987$ 
                // - I wrote it down somewhere. Ahem. "In the middle of the shadows..." Drat! The rest got erased. 
                // $script:1214232707004988$ 
                // - Sorry, that's all I know. You'll have to ask someone else for the rest of the password. 
                return true;
            default:
                return true;
        }
    }
}
