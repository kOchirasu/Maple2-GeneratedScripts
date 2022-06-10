using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001454: Lanpir
/// </summary>
public class _11001454 : NpcScript {
    internal _11001454(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1122123706000873$ 
                // - What is it? 
                return true;
            case 10:
                // $script:1122123706000874$ 
                // - What is it? 
                return true;
            default:
                return true;
        }
    }
}
