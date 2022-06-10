using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001305: Manovich
/// </summary>
public class _11001305 : NpcScript {
    internal _11001305(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005024$ 
                // - $MyPCName$, what is it?
                return true;
            case 10:
                // $script:1228222807005746$ 
                // - No wonder the empress was in such a hurry to see me. It's always something... 
                return true;
            default:
                return true;
        }
    }
}
