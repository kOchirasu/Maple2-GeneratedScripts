using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001316: Masharr
/// </summary>
public class _11001316 : NpcScript {
    internal _11001316(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005035$ 
                // - What brings you to this place? 
                return true;
            case 40:
                // $script:1227194507005698$ 
                // - I cannot see you, but I know you by voice, scent, and soul. 
                // $script:1227194507005699$ 
                // - Your soul is pure. Maybe you can do it... 
                // $script:1227194507005700$ 
                // - May you be blessed with good vibes. 
                return true;
            default:
                return true;
        }
    }
}
