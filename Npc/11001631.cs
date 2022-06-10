using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001631: Bravos
/// </summary>
public class _11001631 : NpcScript {
    internal _11001631(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0516130207006133$ 
                // - Cut to the chase.
                return true;
            case 20:
                // $script:0629205207006505$ 
                // - The moment you step out of here, you're a marked $male:man,female:woman$. Capisce?
                switch (selection) {
                    // $script:0629205207006506$
                    // - I have no clue what you're talking about.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0629205207006507$ 
                // - That's fine. You go about your business. You leave the thinking to me.
                // $script:0630212007006533$ 
                // - You better be careful. We're watching you.
                return true;
            default:
                return true;
        }
    }
}
