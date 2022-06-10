using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004271: Burgundia
/// </summary>
public class _11004271 : NpcScript {
    internal _11004271(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011241$ 
                // - <font color="#909090">(This squat desert plant drips with a brilliant red sap.)</font>
                return true;
            case 10:
                // $script:0911203207011242$ 
                // - <font color="#909090">(This squat desert plant drips with a brilliant red sap.)</font>
                // $script:0911203207011243$ 
                // - <font color="#909090">(You're pretty sure you've seen this shade of red in the clothes and makeup worn by the people of Karkar.)</font>
                // $script:0911203207011244$ 
                // - <font color="#909090">(You've seen plants like this all over Karkar, but they're especially plentiful here.)</font>
                return true;
            default:
                return true;
        }
    }
}
