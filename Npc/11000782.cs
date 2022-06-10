using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000782: Lavor
/// </summary>
public class _11000782 : NpcScript {
    internal _11000782(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002948$ 
                // - I can see a light shining in your eyes. What can I do for you?
                return true;
            case 30:
                // $script:0831180407002951$ 
                // - Hey there, young $male:fellow,female:lady$. You look like a traveler. I hope you're making the most of your youth and seeing the world. 
                return true;
            default:
                return true;
        }
    }
}
