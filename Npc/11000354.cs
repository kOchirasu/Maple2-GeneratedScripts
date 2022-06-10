using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000354: Chairman Goldus
/// </summary>
public class _11000354 : NpcScript {
    internal _11000354(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001472$ 
                // - Grr...
                return true;
            case 30:
                // $script:0831180407001475$ 
                // - Ah, I'm finally safe! You're my savior.
                return true;
            case 40:
                // $script:0831180407001476$ 
                // - I thought I was going to die. I used to think I was untouchable. But after they took me so easily...
                return true;
            case 50:
                // $script:0831180407001477$ 
                // - I can't believe you came to save me... Thank you. I'll live an honest life from now on. I'll donate to charities, pay all my taxes, and volunteer at the soup kitchens.
                return true;
            default:
                return true;
        }
    }
}
