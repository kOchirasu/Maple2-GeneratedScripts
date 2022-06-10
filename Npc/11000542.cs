using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000542: Tanz
/// </summary>
public class _11000542 : NpcScript {
    internal _11000542(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002311$ 
                // - What is it? 
                return true;
            case 20:
                // $script:0831180407002313$ 
                // - If you're not happy with your life, you should dance. When your body's happy, your mind will be too! 
                return true;
            default:
                return true;
        }
    }
}
