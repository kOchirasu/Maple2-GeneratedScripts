using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001378: Boh
/// </summary>
public class _11001378 : NpcScript {
    internal _11001378(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217144507005369$ 
                // - Ugh... Who's there?
                return true;
            case 30:
                // $script:1217144507005372$ 
                // - My head is spinning like a top... Or is it the world that's spinning? I feel like... I'm gonna die...
                return true;
            default:
                return true;
        }
    }
}
