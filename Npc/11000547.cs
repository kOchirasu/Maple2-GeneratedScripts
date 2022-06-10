using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000547: Eka
/// </summary>
public class _11000547 : NpcScript {
    internal _11000547(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002320$ 
                // - Ugh... 
                return true;
            case 20:
                // $script:0831180407002322$ 
                // - Checkpoint... under attack... $map:02000076$... in danger...
                return true;
            case 30:
                // $script:0831180407002323$ 
                // - I-I'm okay... 
                return true;
            default:
                return true;
        }
    }
}
