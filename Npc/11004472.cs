using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004472: Coryne
/// </summary>
public class _11004472 : NpcScript {
    internal _11004472(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0104110407012538$ 
                // - Huh? Who're you?
                return true;
            case 10:
                // $script:0104110407012539$ 
                // - Huh? Who're you?
                // $script:0104110407012540$ 
                // - Why're you dressed like that? You look like a big dummy with a side of dummy sauce.
                switch (selection) {
                    // $script:0104110407012541$
                    // - You practicing for a marathon, kid?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0104110407012542$
                    // - This is cutting-edge fashion where I'm from!
                    case 1:
                        Id = 14;
                        return false;
                }
                return true;
            case 11:
                // $script:0104110407012543$ 
                // - I'm training so I can join the resistance! I'm gonna beat up those Tairen doody-heads good.
                // $script:0104110407012544$ 
                // - But Humanitas only lets the strongest people ever join them. That's why I gotta run so much.
                // $script:0104110407012545$ 
                // - You look pretty strong, though. How do you do it?
                switch (selection) {
                    // $script:0104110407012546$
                    // - Just keep training.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0104110407012547$ 
                // - I was afraid you were gonna say that. Hey... If you see my ma and pa, could you rescue them from the bad guys?
                switch (selection) {
                    // $script:0104110407012548$
                    // - Absolutely.
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:0104110407012549$ 
                // - Wow, really? Okay! Then I gotta keep training so I can help you!
                return true;
            case 14:
                // $script:0104110407012550$ 
                // - And where are you from? A butt?
                return true;
            default:
                return true;
        }
    }
}
