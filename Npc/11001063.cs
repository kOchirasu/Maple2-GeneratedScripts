using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001063: Pitch
/// </summary>
public class _11001063 : NpcScript {
    internal _11001063(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003621$ 
                // - Brrr...
                return true;
            case 30:
                // $script:0831180407003624$ 
                // - Shush! Keep your voice down! I can't give my position away.
                return true;
            default:
                return true;
        }
    }
}
