using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001303: Luanna
/// </summary>
public class _11001303 : NpcScript {
    internal _11001303(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005022$ 
                // - How may I help you look your best? 
                return true;
            case 10:
                // $script:1228224607005747$ 
                // - The empress has great faith in you, $MyPCName$. Do not disappoint her. 
                return true;
            default:
                return true;
        }
    }
}
