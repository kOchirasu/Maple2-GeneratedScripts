using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003638: Fabien
/// </summary>
public class _11003638 : NpcScript {
    internal _11003638(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009095$ 
                // - Wow! This place is amazing. 
                return true;
            case 10:
                // $script:1109121007009096$ 
                // - Excuse me! Would you mind taking my picture? 
                switch (selection) {
                    // $script:1109121007009097$
                    // - Sure, I'll take one for you.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009098$ 
                // - Okay, great! Now, I'll just pose like this and you pretend you're taking a snapshot like that... And let $npcName:11003535[gender:1]$ know that I say, "Nya-nyah-nya-nya-nyah!" 
                switch (selection) {
                    // $script:1109121007009099$
                    // - Uh...
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009100$ 
                // - Act natural! And be sure to let $npcName:11003535[gender:1]$ know my exact words. Mess this up and the whole operation is done for. 
                switch (selection) {
                    // $script:1109121007009101$
                    // - Understood.
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009102$ 
                // - Wow! The picture came out great. Thank you. 
                return true;
            default:
                return true;
        }
    }
}
