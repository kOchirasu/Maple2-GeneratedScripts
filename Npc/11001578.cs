using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001578: Trini
/// </summary>
public class _11001578 : NpcScript {
    internal _11001578(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006066$ 
                // - Welcome. 
                return true;
            case 10:
                // $script:0515180307006120$ 
                // - If we come together...  
                return true;
            default:
                return true;
        }
    }
}
