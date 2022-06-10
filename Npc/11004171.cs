using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004171: Startz
/// </summary>
public class _11004171 : NpcScript {
    internal _11004171(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010599$ 
                // - Order now or get a face full of burning oil. Your choice.  
                return true;
            case 10:
                // $script:0806025707010600$ 
                // - Don't get the wrong idea. I'm not here selling churros because my restaurant is doing poorly, I'm just here to enjoy myself. 
                switch (selection) {
                    // $script:0806025707010601$
                    // - So then why ARE you selling churros?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0806025707010602$
                    // - Can I have a churro?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:0806025707010603$ 
                // - Huh? Because I like to cook, obviously. 
                // $script:0806025707010604$ 
                // - Well... If I'm being honest, we all trekked all the way here to $map:02000499$ to take a vacation, but we ran out of money to pay for lodging. 
                return true;
            case 12:
                // $script:0806025707010605$ 
                // - They're not done yet. Come back later. 
                return true;
            default:
                return true;
        }
    }
}
