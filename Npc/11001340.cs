using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001340: Jenk
/// </summary>
public class _11001340 : NpcScript {
    internal _11001340(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005279$ 
                // - Delicious food here! Get your delicious food!
                return true;
            case 40:
                // $script:1217012607005283$ 
                // - All my food is made with 100% love, guaranteed. You'll like 'em so much, you won't even notice if someone drops dead right next to you! They'll change your whole outlook on life!
                return true;
            default:
                return true;
        }
    }
}
