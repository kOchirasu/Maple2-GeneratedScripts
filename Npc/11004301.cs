using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004301: Ghost
/// </summary>
public class _11004301 : NpcScript {
    internal _11004301(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1002141907011409$ 
                // - Ooh la la! 
                return true;
            case 30:
                // $script:1002141907011412$ 
                // - Beautiful. Stunning. A gift from the goddess! 
                switch (selection) {
                    // $script:1002141907011413$
                    // - What are you going on about?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1002141907011414$ 
                // - I can't get the woman in purple out of my head! I love a woman with pep. 
                switch (selection) {
                    // $script:1002141907011415$
                    // - You mean $npc:11004289[gender:1]$?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1002141907011416$ 
                // - That's the one! You'd be head-over-heels if you saw her, too. So lithe. And those executive management skills? Ooh la la! 
                // $script:1002141907011417$ 
                // - The other ghosts say she's mean, but I think she's better than the empress herself! A woman like that makes a guy wish he'd died young, so he'd have a handsomer ghost. 
                return true;
            default:
                return true;
        }
    }
}
