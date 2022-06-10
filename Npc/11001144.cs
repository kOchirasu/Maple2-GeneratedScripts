using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001144: Machias
/// </summary>
public class _11001144 : NpcScript {
    internal _11001144(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0915220707003955$ 
                // - Come closer! Yes, you my child. 
                return true;
            case 30:
                // $script:0915220707003958$ 
                // - To picture the future clearly, I must make myself one with nature. Focus your senses. The breeze carries with it the scent of flowers. The waterfall quietly roars. 
                // $script:0915222107003979$ 
                // - For an accurate reading, I must focus my mind and keep disruptive thoughts at bay. 
                return true;
            default:
                return true;
        }
    }
}
