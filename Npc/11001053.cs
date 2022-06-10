using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001053: Houzin
/// </summary>
public class _11001053 : NpcScript {
    internal _11001053(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003596$ 
                // - My emotions got the best of me. 
                return true;
            case 30:
                // $script:0831180407003599$ 
                // - The greatest martial artists aren't always the strongest ones. They're the ones who are humble and always put other people first. 
                return true;
            default:
                return true;
        }
    }
}
