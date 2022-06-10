using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001012: Langley
/// </summary>
public class _11001012 : NpcScript {
    internal _11001012(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003454$ 
                // - Hello. 
                return true;
            case 30:
                // $script:0831180407003457$ 
                // - I'm sure you heard that time stopped here in Ludibrium. Now I don't have to worry about getting old, as long as I stay here. 
                return true;
            default:
                return true;
        }
    }
}
