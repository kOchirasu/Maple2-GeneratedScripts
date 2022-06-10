using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004055: Oska
/// </summary>
public class _11004055 : NpcScript {
    internal _11004055(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010083$ 
                // - The siege on Madrakan was successful, but it cost us a great deal. 
                return true;
            case 10:
                // $script:0614185307010084$ 
                // - The siege on Madrakan was successful, but it cost us a great deal. 
                return true;
            default:
                return true;
        }
    }
}
