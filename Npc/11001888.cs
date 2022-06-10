using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001888: Joanna
/// </summary>
public class _11001888 : NpcScript {
    internal _11001888(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1027193507007340$ 
                // - Good, very good! 
                return true;
            case 30:
                // $script:1027193507007341$ 
                // - The filming went smoothly, thanks to you. Anyway, it's getting late, so I'm heading back to the station. I'll see you in $map:02000164$. 
                return true;
            default:
                return true;
        }
    }
}
