using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004312: Veliche
/// </summary>
public class _11004312 : NpcScript {
    internal _11004312(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0928133807011350$ 
                // - The future is in our hands. 
                return true;
            case 10:
                // $script:0928133807011351$ 
                // - We're on alien soil. Don't let your guard down. 
                return true;
            case 20:
                // $script:0116153807012734$ 
                // - I have no missions for you right now. 
                return true;
            default:
                return true;
        }
    }
}
