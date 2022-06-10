using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000530: Schwanda
/// </summary>
public class _11000530 : NpcScript {
    internal _11000530(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002276$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:0831180407002277$ 
                // - I mostly paint portraits. Would you like to know why?
                // $script:0831180407002278$ 
                // - Because the most beautiful thing in the world is people! That's why I like painting them. 
                return true;
            case 20:
                // $script:0831180407002279$ 
                // - Would you like to know when I started painting?
                // $script:0831180407002280$ 
                // - Well, that's... I don't know. Do you remember when you started eating food on your own? Or when you spoke your first word?
                // $script:0831180407002281$ 
                // - Picking up a brush was as natural to me as picking up a spoon. I was born to paint. I don't need to know exactly when I started doing it.
                return true;
            default:
                return true;
        }
    }
}
