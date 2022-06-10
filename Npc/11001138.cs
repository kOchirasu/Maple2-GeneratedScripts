using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001138: Neroa
/// </summary>
public class _11001138 : NpcScript {
    internal _11001138(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911192907003893$ 
                // - Have you seen any monsters outside? 
                return true;
            case 30:
                // $script:0911192907003896$ 
                // - As long as I don't give up hope, all this will be behind me one day... I really wish I could believe that... 
                return true;
            default:
                return true;
        }
    }
}
