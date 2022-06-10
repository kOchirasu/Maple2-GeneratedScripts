using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004548: Sleeping Rafflesia
/// </summary>
public class _11004548 : NpcScript {
    internal _11004548(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0111140307012685$ 
                // - <font color="#909090">(The rafflesia is highly toxic. This one seems to be slumbering. Try not to wake it up.)</font>
                return true;
            case 10:
                // $script:0111140307012686$ 
                // - <font color="#909090">(The rafflesia is highly toxic. This one seems to be slumbering. Try not to wake it up.)</font>
                return true;
            default:
                return true;
        }
    }
}
