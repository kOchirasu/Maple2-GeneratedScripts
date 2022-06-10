using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001107: Vena
/// </summary>
public class _11001107 : NpcScript {
    internal _11001107(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0908154107003719$ 
                // - Mm... T-that's... 
                return true;
            case 30:
                // $script:0908154107003722$ 
                // - Mom was right. She said anything can come true if I pray hard enough. I've prayed every day to be able to go back to her. Now I can!
                return true;
            default:
                return true;
        }
    }
}
